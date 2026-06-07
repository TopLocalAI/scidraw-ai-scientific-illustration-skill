---
name: scidraw-scientific-figure
version: 1.0.0
description: Create one high-quality scientific/technical figure image per request. This skill focuses on single-image output, consistency, and repeatable visual guidance.
metadata:
  openclaw:
    requires:
      bins:
        - python3
    primaryEnv: OPENAI_API_KEY
    envVars:
      - name: OPENAI_API_KEY
        required: false
        description: Optional for API fallback mode.
      - name: OPENAI_BASE_URL
        required: false
        description: Optional OpenAI-compatible endpoint for API fallback.
      - name: SCIDRAW_FIGURE_MODEL
        required: false
        description: Default is gpt-image-2.
      - name: SCIDRAW_FIGURE_HOME
        required: false
        description: Optional runtime home override, default is ~/.scidraw-figure-skill.
  homepage: https://github.com/<your-org>/scidraw-ai-scientific-illustration-skill
---

# SciDraw Scientific Figure Skill

## Overview

This skill generates **exactly one figure image per run** from a scientific prompt, outline, or source materials summary. It is designed for researchers, students, and product teams who want publishable- style visuals with clear labels and readable text.

Use this skill when:

- You need one figure for a paper, report, thesis slide, or demo explanation.
- The output can be a full-slide style image instead of an editable PPT page.
- You want strict control over layout role, color palette, and text quality.

Do **not** use this skill when you need a full editable multi-page deck as the primary output.

## Philosophy

- One image per user request is the default.
- Keep style consistent per task.
- Chinese and English text should be readable; avoid garbled characters.
- Use the built-in image tool when available. Fall back only when unavailable or explicitly requested.

## Workflow (Single Image)

1. Read user request
   - identify topic, audience, output purpose, required labels, data fidelity, and constraints
   - confirm exact output intent (cover, mechanism diagram, comparison chart style, timeline, process flow, model architecture, etc.)

2. Confirm style and format
   - confirm aspect ratio (default 16:9) and language for labels
   - confirm typography density (compact/normal/airy)
   - confirm color palette and visual tone

3. Confirm image backend
   - check builtin image tool availability
   - if builtin is available: prefer builtin and do not configure API key first
   - if builtin is unavailable or user requires API mode: use fallback CLI/API workflow
   - show the checked result and ask for confirmation before generating

4. Generate one figure
   - generate directly to the requested output path
   - if source figure/data assets are required, treat them as strict inputs
   - show generated preview path and ask for final approval

5. Optional repair
   - if requested, regenerate with tighter constraints
   - if local strict source image is wrong, regenerate with stronger preservation instructions

## Output structure (single figure run)

Use one figure file path by default:

```text
{base_dir}/outputs/
└── figure_YYYYMMDD_HHMMSS.png
```

If user provides an explicit path, use that exact path.

## Built-in image tool (preferred)

Prefer built-in image generation when available (`image_gen` in Codex-style environments).

For builtin mode:

- keep the prompt in one request
- include role-labeled references for any local source images after `view_image`
- never treat local files as raw file paths in builtin prompt

## API/CLI fallback mode

Fallback mode uses `scripts/image_gen.py` and shared runtime config.

### Recommended bootstrap

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py bootstrap
```

### One image generation command

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/image_gen.py \
  --model gpt-image-2 \
  --size 2560x1440 \
  --quality medium \
  --prompt-file /tmp/prompt.txt \
  --out outputs/figure.png
```

## Required local assets

If user supplies source data/image inputs that must appear in the output, treat them as strict requirements:

- keep original labels/axes/values visible
- do not redraw them as alternatives
- preserve naming and unit scale when provided

## Response protocol

Before generation:

- summarize interpretation
- list backend and reason
- confirm output path

After generation:

- return absolute output path
- state whether backend used
- ask whether one more refinement is needed

## Acceptance criteria

- One final image file exists and is readable
- The image visually matches requested role and style
- Key text is present and clear
- If source asset constraints exist, they are visibly preserved
