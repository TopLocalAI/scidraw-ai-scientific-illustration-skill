# SciDraw AI Scientific Illustration Skill

[![中文](https://img.shields.io/badge/docs-%E4%B8%AD%E6%96%87-red)](./README.md)

This is a **single-image** scientific illustration skill for Codex-style agents.

Each request generates exactly one image.  
This repo does not aim at full editable pipeline output, PPT assembly, or SVG editor workflows.

> [!TIP]
> For full production workflows (batch generation, edit-ready flow, SVG export, and platform workflows), use SciDraw directly:
>
> - https://sci-draw.com/
> - https://sci-draw.com/ai-scientific-illustration
> - https://sci-draw.com/convert

## Friendly note

This skill is optimized for “quick one-image delivery” in an agent workflow.

- Priority: use Codex built-in image generation.
- Optional fallback: `image_gen.py` CLI/API mode when built-in generation is unavailable.
- If you frequently use the same output settings, you can lock your preferred prompt structure once and reuse it.

## Features

- Single-image output per invocation.
- Works for scientific roadmaps, mechanism diagrams, method flows, model architecture charts, and comparison visuals.
- Supports source-anchored generation when strict preservation is required.
- Simple and explicit workflow, suitable for iterative review inside chat.

## Installation

### One-sentence install (recommended)

Tell your agent:

```text
Please install this skill for me: https://github.com/TopLocalAI/scidraw-ai-scientific-illustration-skill
```

### Manual install (Codex)

```bash
npx -y skills@latest add TopLocalAI/scidraw-ai-scientific-illustration-skill \
  --skill scidraw-scientific-figure \
  --agent codex \
  --global
```

Restart your agent afterwards.

## API fallback configuration

Only required when built-in image generation cannot be used.

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py config \
  --api-key "YOUR_API_KEY" \
  --base-url "https://api.openai.com/v1" \
  --model gpt-image-2
```

Health check:

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py doctor --check-api
```

## How to use

1. Define purpose (roadmap/flow/mechanism/architecture).
2. Specify aspect ratio (`16:9`, `4:3`, `1:1`).
3. Define language and label density.
4. Define structure and logic chain (question → method → result → validation).
5. Tell if source labels/axes/units must be strictly preserved.
6. Confirm single-image output.

Example:

```text
Generate one scientific figure in 16:9.
Use Chinese labels and keep layout logic clear.
Topic: ...
Flow: Problem -> Method -> Data -> Validation.
Keep key labels and numeric units unchanged.
Output only one image.
```

## Fallback CLI usage (optional)

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py bootstrap
```

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/image_gen.py \
  --prompt "Generate one scientific mechanism diagram, 16:9, academic style." \
  --size 2560x1440 \
  --quality medium \
  --out scidraw-ai-scientific-illustration-skill/outputs/figure.png
```

`image_gen.py` options:

- `--prompt-file /path/to/prompt.txt`
- `--prompt-file -` (stdin)
- `--dry-run`
- `--json`

## Case Gallery (downloaded from this repo R2 assets)

### 1. Funding Roadmap

![Funding Roadmap](assets/examples/case-1-funding-roadmap.png)

### 2. NSFC Technical Roadmap

![NSFC Technical Roadmap](assets/examples/case-2-nsfc-roadmap.png)

### 3. Research Logic Map

![Research Logic Map](assets/examples/case-3-research-logic.png)

### 4. Digital Twin Workflow

![Digital Twin Workflow](assets/examples/case-4-digital-twin.png)

## FAQ

- Does this skill export SVG or editable PPT?  
  No. For SVG/editable flows, use SciDraw’s web platform.
- Do I need an API key?  
  Usually no, when built-in image generation is available.
- Can I generate multiple images at once?  
  No. This skill is intentionally single-output.
- Is source input preserved?  
  It can be preserved when the prompt explicitly requires strict retention.

## Structure

```text
scidraw-ai-scientific-illustration-skill/
├── SKILL.md
├── README.md
├── README.en.md
├── requirements.txt
├── assets/
│   └── examples/
│       ├── case-1-funding-roadmap.png
│       ├── case-2-nsfc-roadmap.png
│       ├── case-3-research-logic.png
│       └── case-4-digital-twin.png
└── scripts/
    ├── codex_scidraw_runtime.py
    └── image_gen.py
```

