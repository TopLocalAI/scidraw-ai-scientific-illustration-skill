#!/usr/bin/env python3
"""Single-image fallback generator for SciDraw scientific figure skill."""

from __future__ import annotations

import argparse
import base64
import os
import sys
import time
from pathlib import Path
from typing import Optional

from openai import OpenAI

from codex_scidraw_runtime import DEFAULT_MODEL, _env_path, _runtime_home

DEFAULT_SIZE = "2560x1440"
DEFAULT_QUALITY = "medium"


def _die(message: str, code: int = 1) -> None:
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(code)


def _load_runtime_env() -> None:
    path = _env_path(_runtime_home())
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and not os.getenv(key):
            os.environ[key] = value


def _read_prompt(prompt: Optional[str], prompt_file: Optional[str]) -> str:
    if prompt and prompt_file:
        _die("Use --prompt or --prompt-file, not both.")
    if prompt_file:
        if prompt_file == "-":
            data = sys.stdin.read().strip()
        else:
            path = Path(prompt_file)
            if not path.exists():
                _die(f"Prompt file not found: {path}")
            data = path.read_text(encoding="utf-8").strip()
    elif prompt:
        data = prompt.strip()
    else:
        _die("Missing prompt. Use --prompt or --prompt-file.")

    if not data:
        _die("Prompt is empty.")
    return data


def _validate_model(model: str) -> None:
    if "gpt-image-" not in model:
        _die("Model must contain 'gpt-image-' (for example gpt-image-2).")


def _parse_size(size: str) -> tuple[int, int]:
    parts = size.lower().split("x")
    if len(parts) != 2:
        _die("size must look like WIDTHxHEIGHT, e.g. 2560x1440")
    w = int(parts[0])
    h = int(parts[1])
    if w <= 0 or h <= 0:
        _die("size must be positive integers.")
    if w % 16 != 0 or h % 16 != 0:
        _die("For stable output quality, use width and height that are multiples of 16.")
    if w > 4096 or h > 4096:
        _die("Fallback guard: width/height must be <= 4096.")
    return w, h


def _augment_prompt(prompt: str) -> str:
    return (
        "Create a publication-quality scientific figure with clean layout, high text readability, "
        "accurate labels, and consistent typography.\n\n"
        + prompt
    )


def _write_image(data_b64: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(base64.b64decode(data_b64))


def _main() -> int:
    _load_runtime_env()

    parser = argparse.ArgumentParser(description="Generate one scientific figure image with fallback API mode")
    parser.add_argument("--model", default=os.getenv("SCIDRAW_FIGURE_MODEL", DEFAULT_MODEL))
    parser.add_argument("--prompt")
    parser.add_argument("--prompt-file")
    parser.add_argument("--size", default=DEFAULT_SIZE)
    parser.add_argument("--quality", default=DEFAULT_QUALITY)
    parser.add_argument("--out", default="outputs/figure.png")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true", help="Print machine-readable output")
    args = parser.parse_args()

    model = args.model.strip()
    _validate_model(model)
    size = args.size.strip().lower()
    _parse_size(size)
    quality = args.quality.strip().lower()
    if quality not in {"low", "medium", "high", "auto"}:
        _die("quality must be one of: low, medium, high, auto")

    prompt = _read_prompt(args.prompt, args.prompt_file)
    prompt = _augment_prompt(prompt)

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        _die(
            "OPENAI_API_KEY is not configured. Run:\n"
            f"  python3 {Path(__file__).resolve().parents[1] / 'scripts' / 'codex_scidraw_runtime.py'} config --api-key YOUR_KEY"
        )

    if args.dry_run:
        payload = {
            "model": model,
            "size": size,
            "quality": quality,
            "prompt": prompt[:1800],
            "out": args.out,
        }
        if args.json:
            import json

            print(json.dumps({"status": "dry_run", "payload": payload}, ensure_ascii=False))
            return 0
        print("Dry run payload:")
        for key, value in payload.items():
            print(f"  {key}: {value}")
        return 0

    out_path = Path(args.out).expanduser().resolve()

    try:
        client = OpenAI(
            api_key=api_key,
            base_url=os.getenv("OPENAI_BASE_URL") or "https://api.openai.com/v1",
        )
        started = time.time()
        result = client.images.generate(
            model=model,
            prompt=prompt,
            n=1,
            size=size,
            quality=quality,
        )
        elapsed = time.time() - started
    except Exception as exc:
        _die(f"Image API request failed: {exc}")

    b64_data = None
    if hasattr(result, "data") and result.data:
        first = result.data[0]
        b64_data = getattr(first, "b64_json", None)

    if not b64_data:
        _die("Image API did not return base64 image data.")

    _write_image(b64_data, out_path)

    if args.json:
        import json

        print(
            json.dumps(
                {
                    "status": "ok",
                    "backend": "fallback image API",
                    "model": model,
                    "size": size,
                    "quality": quality,
                    "out": str(out_path),
                    "elapsed_seconds": round(elapsed, 2),
                },
                ensure_ascii=False,
            )
        )
    else:
        print(f"Image saved: {out_path}")
        print(f"Time: {elapsed:.1f}s")

    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
