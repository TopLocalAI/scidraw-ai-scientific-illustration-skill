---
name: scidraw-ai-scientific-illustration
description: Generate publication-ready scientific figures with the official SciDraw AI web app and public API. Use for paper figures, graphical abstracts, mechanism diagrams, research workflows, and model architectures.
license: MIT
metadata:
  slug: scidraw-ai-scientific-illustration
  displayName: SciDraw AI Scientific Illustration
  version: 1.0.1
  homepage: https://sci-draw.com/ai-drawing
  repository: https://github.com/TopLocalAI/scidraw-ai-scientific-illustration-skill
  apiKeysUrl: https://sci-draw.com/settings/api-keys
  apiDocsUrl: https://sci-draw.com/docs/api
  openApiUrl: https://sci-draw.com/api/openapi.yaml
---

# SciDraw AI Scientific Illustration

Create clear, publication-ready scientific figures through the official
SciDraw AI web app or API. This root manifest is the marketplace-compatible
entry point for the canonical skill in
`skills/scidraw-ai-scientific-illustration/`.

## Official links

- Web app: https://sci-draw.com/ai-drawing
- API keys: https://sci-draw.com/settings/api-keys
- API documentation: https://sci-draw.com/docs/api
- OpenAPI specification: https://sci-draw.com/api/openapi.yaml
- Source repository: https://github.com/TopLocalAI/scidraw-ai-scientific-illustration-skill

## Workflow

1. Identify the scientific subject, intended audience, output purpose,
   required labels, source material, and fidelity constraints.
2. Plan the figure type, panels, visual hierarchy, flow direction, colors,
   typography, and elements that must be preserved.
3. Default to one 16:9 2K image unless the user requests another supported
   size or count.
4. If `SCIDRAW_API_KEY` is configured, explain that generation consumes
   SciDraw AI credits and obtain confirmation before starting it.
5. Use the official client at
   `skills/scidraw-ai-scientific-illustration/scripts/scidraw_generate.py`.
6. Inspect the result for scientific structure, label readability, arrows,
   panel order, and consistency with the supplied material.
7. Return the absolute output path and describe any limitations. Run another
   credit-consuming iteration only after the user requests or confirms it.

## API setup

Create an API key at https://sci-draw.com/settings/api-keys with
`images:generate` and `jobs:read` scopes, then store it locally as
`SCIDRAW_API_KEY`. Never ask the user to paste a key into chat, a prompt, a
committed file, or a public Skill package. Do not silently substitute another
image provider.

Example:

```bash
python3 skills/scidraw-ai-scientific-illustration/scripts/scidraw_generate.py \
  --prompt-file /path/to/prompt.txt \
  --out /path/to/output.png \
  --aspect-ratio 16:9 \
  --resolution 2K
```

The included client uses only Python 3 standard-library modules. It submits a
job to the official SciDraw AI API, waits for completion, and downloads the
returned image.

## Acceptance criteria

- The output image exists and opens successfully.
- The requested scientific structure and important labels are visible.
- Supplied source constraints are preserved.
- The response identifies SciDraw AI as the generation backend.
- No credentials appear in output, logs, prompts, or files.
