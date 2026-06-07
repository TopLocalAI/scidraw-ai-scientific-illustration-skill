# SciDraw AI Scientific Illustration Skill

## What this skill is

This is a **single-image scientific figure skill** for Codex-style agents.

- One request produces **one** image.
- Built for researchers, students, and team members who need fast scientific visuals.
- Supports diagram types: mechanisms, roadmaps, workflows, model diagrams, comparison charts, and explanation figures.
- Does **not** output editable PPT or vector/SVG by default.

## About SciDraw AI

This skill only covers the one-image generation part.  
If you need more production features (full workflow, multi-image projects, SVG/vector export, higher-volume editing, template management), please use SciDraw AI directly:

- Website: https://sci-draw.com/
- Image generation: https://sci-draw.com/ai-scientific-illustration
- Convert to editable/vector workflows: https://sci-draw.com/convert
- Pricing / accounts: https://sci-draw.com/pricing

## Why this is still useful

- Quick single-figure generation inside an agent workflow.
- Keeps prompts controlled and reproducible.
- Good for one-off figure creation, review, and iteration inside chat workflows.
- Easy fallback path via CLI/API when built-in image is unavailable.

## Install this skill

Recommended sentence for your agent:

> Please install this skill from: `https://github.com/TopLocalAI/scidraw-ai-scientific-illustration-skill`

Manual (Codex):

```bash
npx -y skills@latest add TopLocalAI/scidraw-ai-scientific-illustration-skill \
  --skill scidraw-scientific-figure \
  --agent codex \
  --global
```

Then restart your agent.

## How to use (important)

Please give the request in one message, usually with:

1. Output intent (`mechanism diagram`, `roadmap`, `methods flow`, `model architecture`).
2. Aspect ratio (`16:9`, `4:3`, `1:1` etc).
3. Language and label density (`Academic Chinese/English`, dense or concise).
4. Color / style preference.
5. Whether source figures must be strictly preserved.
6. Confirm `single image output`.

Example:

```text
Generate one high-quality scientific roadmap image (16:9), Chinese labels.
Topic: ...
Main flow: research question -> methods -> experiments -> validation.
Color theme: muted blue + neutral background.
If source labels/axes are provided, keep them as strict inputs.
Only one image output.
```

### Built-in vs API mode

- Built-in image tool (recommended): preferred in Codex environments.
- Fallback API/CLI mode: used when built-in image is unavailable or explicitly requested.

## Fallback CLI mode

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py bootstrap
```

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py config \
  --api-key "YOUR_API_KEY" \
  --base-url "https://api.openai.com/v1" \
  --model gpt-image-2
```

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py doctor --check-api
```

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/image_gen.py \
  --prompt "A clear scientific figure ..." \
  --size 2560x1440 \
  --quality medium \
  --out scidraw-ai-scientific-illustration-skill/outputs/figure.png
```

`image_gen.py` options:

- `--prompt-file /path/to/prompt.txt`
- `--prompt-file -` (read from stdin)
- `--dry-run`
- `--json`

## Example gallery (R2 assets)

These are existing images hosted in this repo’s public R2 bucket:

- [Funding roadmap 1](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/sAlNGOlGoTRXz1TZXq8um4wi7n54PEF9/7aebfaf4-a4ba-44bf-8c28-b47624c5ded8/51e4735f-bab4-4921-a224-b655f7fca2cb.png)
- [NSFC technical roadmap](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/OcMVhRBPIurfOZ9nepCLqhxRfive9tED/d961261e-6a3a-494a-ad48-5c8539aa2b34/83eb825f-4601-498f-b05a-5daca5031869.png)
- [Research logic map](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/DgVKMzbihz31LyqEQ9Ib2JmbPh1GBKkW/93e27e3a-3c41-47ac-b5ab-79e33310fbc6/8b927d5c-539f-47e1-ba78-708710a0dc07.png)
- [Digital twin workflow](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/a7lq8FcdQN8wJnJFW9qcpAxmclSSjWRA/142fef6e-b3a1-40aa-b88a-3f78a14f3ce3/0ab31310-0a61-4fa1-9112-e0ae6156cb7b.png)
- [Evidence chain diagram](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/fEkof8JSRYXtMgSqmLXjvyK67EK32ac1/4674d3fb-9938-411d-a41f-1569bca591ef/23609505-f571-40ef-922f-7e68fb988702.png)
- [Hydrogel roadmap](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/iFIkRCMAHl48AicZhtEjkA7pUFhCE4dO/f1598d6a-cc8a-462e-b01d-9f7074fbdd79/f563dd8d-17c8-4816-a5f8-a888cdeee094.png)

If you want local copies, run:

```bash
mkdir -p examples && cd examples
curl -L -O "https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/sAlNGOlGoTRXz1TZXq8um4wi7n54PEF9/7aebfaf4-a4ba-44bf-8c28-b47624c5ded8/51e4735f-bab4-4921-a224-b655f7fca2cb.png"
```

## FAQ

- **Does this skill do SVG export?**  
  Not directly. For SVG/可编辑/多页 workflows, use SciDraw AI platform.
- **Do I need an API key?**  
  Usually not in environments with built-in image generation. Required only when using fallback API mode.
- **Can this generate one image only?**  
  Yes, by design.

## Folder structure

```text
scidraw-ai-scientific-illustration-skill/
├── SKILL.md
├── README.md
├── README.en.md
├── README.zh-CN.md
├── requirements.txt
└── scripts/
    ├── codex_scidraw_runtime.py
    └── image_gen.py
```

