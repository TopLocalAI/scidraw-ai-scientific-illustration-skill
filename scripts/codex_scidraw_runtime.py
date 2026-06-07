#!/usr/bin/env python3
"""Runtime helper for scidraw scientific figure skill.

Keeps shared Python venv and API configuration in:
  SCIDRAW_FIGURE_HOME (default ~/.scidraw-figure-skill)
"""

from __future__ import annotations

import argparse
import json
import os
import stat
import subprocess
import sys
import urllib.error
import urllib.request
import venv
from pathlib import Path
from typing import Dict, Optional

DEFAULT_RUNTIME_HOME = "~/.scidraw-figure-skill"
DEFAULT_MODEL = "gpt-image-2"
ENV_FIELDS = (
    "OPENAI_API_KEY",
    "OPENAI_BASE_URL",
    "SCIDRAW_FIGURE_MODEL",
)


def _runtime_home() -> Path:
    return Path(os.getenv("SCIDRAW_FIGURE_HOME", DEFAULT_RUNTIME_HOME)).expanduser()


def _venv_python(home: Path) -> Path:
    if os.name == "nt":
        return home / ".venv" / "Scripts" / "python.exe"
    return home / ".venv" / "bin" / "python"


def _env_path(home: Path) -> Path:
    return home / ".env"


def _requirements_path() -> Path:
    return Path(__file__).resolve().parents[1] / "requirements.txt"


def _die(message: str, code: int = 1) -> None:
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(code)


def _ensure_dirs(home: Path) -> None:
    for child in (home, home / "cache", home / "logs"):
        child.mkdir(parents=True, exist_ok=True)


def _parse_env_file(path: Path) -> Dict[str, str]:
    if not path.exists():
        return {}
    values: Dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            values[key] = value
    return values


def _load_env_values(home: Path) -> Dict[str, str]:
    values = _parse_env_file(_env_path(home))
    for key in ENV_FIELDS:
        if os.getenv(key):
            values[key] = os.environ[key]
    return values


def _mask_secret(value: str) -> str:
    if not value:
        return "<unset>"
    if len(value) <= 8:
        return "****"
    return f"{value[:4]}...{value[-4:]}"


def _quote_env_value(value: str) -> str:
    if not value:
        return ""
    if any(ch.isspace() for ch in value) or "#" in value or '"' in value:
        return json.dumps(value)
    return value


def _write_env_file(path: Path, values: Dict[str, str]) -> None:
    lines = [
        "# scidraw scientific figure shared runtime configuration",
        "# Used by Codex/agent fallback mode.",
    ]
    for key in ENV_FIELDS:
        value = values.get(key, "")
        if value:
            lines.append(f"{key}={_quote_env_value(value)}")
    lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    try:
        path.chmod(stat.S_IRUSR | stat.S_IWUSR)
    except OSError:
        pass


def _bootstrap(_: argparse.Namespace) -> int:
    home = _runtime_home()
    _ensure_dirs(home)
    python = _venv_python(home)

    if not python.exists():
        print(f"Creating virtualenv: {home / '.venv'}")
        venv.EnvBuilder(with_pip=True, clear=False).create(home / ".venv")
    else:
        print(f"Virtualenv already exists: {home / '.venv'}")

    requirements = _requirements_path()
    if not requirements.exists():
        _die(f"requirements.txt not found: {requirements}")

    cmd = [str(python), "-m", "pip", "install", "-r", str(requirements)]
    print(f"Installing dependencies: {requirements}")
    subprocess.run(cmd, check=True)
    print(f"Runtime ready: {home}")
    return 0


def _config(args: argparse.Namespace) -> int:
    home = _runtime_home()
    _ensure_dirs(home)
    values = _load_env_values(home)

    if args.api_key:
        values["OPENAI_API_KEY"] = args.api_key
    if args.base_url is not None:
        values["OPENAI_BASE_URL"] = args.base_url.strip()
    if args.model is not None:
        values["SCIDRAW_FIGURE_MODEL"] = args.model.strip()
    if args.clear_base_url:
        values.pop("OPENAI_BASE_URL", None)

    _write_env_file(_env_path(home), values)
    print(f"Wrote {_env_path(home)}")
    for key in ENV_FIELDS:
        value = values.get(key, "")
        if key == "OPENAI_API_KEY":
            value = _mask_secret(value)
        print(f"{key}={value or '<unset>'}")
    return 0


def _check_python_imports(python: Path) -> bool:
    if not python.exists():
        print(f"venv: missing python at {python}")
        return False
    proc = subprocess.run(
        [str(python), "-c", "import openai, sys; print('imports ok')"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if proc.returncode != 0:
        print("dependencies: missing or broken")
        if proc.stderr:
            print(proc.stderr.strip())
        return False
    return True


def _models_request(base_url: str, api_key: str, timeout: int) -> bool:
    endpoint = base_url.rstrip("/") + "/models"
    req = urllib.request.Request(
        endpoint,
        headers={"Authorization": f"Bearer {api_key}"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            print(f"models endpoint HTTP {resp.status}")
            return 200 <= resp.status < 300
    except urllib.error.HTTPError as exc:
        body = exc.read(800).decode("utf-8", "replace")
        print(f"models endpoint HTTP {exc.code}")
        if body:
            print(body)
        return False
    except Exception as exc:
        print(f"models endpoint: {exc.__class__.__name__}: {exc}")
        return False


def _doctor(args: argparse.Namespace) -> int:
    home = _runtime_home()
    env_file = _env_path(home)
    values = _load_env_values(home)
    api_key = values.get("OPENAI_API_KEY", "")
    base_url = values.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
    model = values.get("SCIDRAW_FIGURE_MODEL", DEFAULT_MODEL)

    print(f"runtime home: {home}")
    print(f"env file: {env_file} ({'exists' if env_file.exists() else 'missing'})")
    print(f"venv python: {_venv_python(home)}")
    print(f"OPENAI_API_KEY={_mask_secret(api_key)}")
    print(f"OPENAI_BASE_URL={base_url}")
    print(f"SCIDRAW_FIGURE_MODEL={model}")

    ok = _check_python_imports(_venv_python(home))
    if args.check_api:
        if not api_key:
            print("api check: skipped, OPENAI_API_KEY unset")
            return 0 if ok else 1
        if not _models_request(base_url, api_key, args.timeout):
            return 1
    return 0 if ok else 1


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage scidraw scientific figure shared runtime")
    subparsers = parser.add_subparsers(dest="command", required=True)

    bootstrap = subparsers.add_parser("bootstrap", help="Create shared venv and install deps")
    bootstrap.set_defaults(func=_bootstrap)

    config = subparsers.add_parser("config", help="Write/update runtime .env")
    config.add_argument("--api-key")
    config.add_argument("--base-url")
    config.add_argument("--clear-base-url", action="store_true")
    config.add_argument("--model")
    config.set_defaults(func=_config)

    doctor = subparsers.add_parser("doctor", help="Check runtime and optional API connectivity")
    doctor.add_argument("--check-api", action="store_true")
    doctor.add_argument("--timeout", type=int, default=30)
    doctor.set_defaults(func=_doctor)

    return parser


def main(argv: Optional[list[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
