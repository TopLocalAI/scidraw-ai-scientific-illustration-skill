# SciDraw AI Scientific Illustration Skill

[![中文](https://img.shields.io/badge/docs-%E4%B8%AD%E6%96%87-red)](./README.md)
[![GitHub stars](https://img.shields.io/github/stars/TopLocalAI/scidraw-ai-scientific-illustration-skill?style=flat&logo=github&label=stars)](https://github.com/TopLocalAI/scidraw-ai-scientific-illustration-skill/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/TopLocalAI/scidraw-ai-scientific-illustration-skill?style=flat&logo=github&label=forks)](https://github.com/TopLocalAI/scidraw-ai-scientific-illustration-skill/forks)

A Codex-oriented skill for generating **one scientific figure image per request**. It can also be used in Claude Code, OpenClaw, Hermes Agent, and other agents that support `SKILL.md`.

> [!TIP]
> If you do not have an image generation API, or if you need the full SciDraw workflow, use SciDraw AI directly:
>
> - AI Drawing: https://sci-draw.com/ai-drawing
> - SciDraw AI website: https://sci-draw.com/
> - Convert tools for SVG/PPTX/PDF/TIFF workflows: https://sci-draw.com/convert
>
> The SciDraw AI platform supports AI Drawing, sketch-to-professional-figure workflows, image editing, editable SVG/PPTX export, and publication-ready PNG/PDF/TIFF export. This skill only covers single-image generation inside agent workflows.

## Friendly Note

This skill is not the full SciDraw AI product, and it is not an editable PPT or SVG generator. It is a lightweight agent workflow: the agent interprets your scientific communication goal and preferably uses built-in ImageGen to generate one scientific figure image.

If you already use SciDraw AI on the web, treat this skill as a companion tool for quick drafts, prompt refinement, and structure planning inside Codex. For SVG, PPTX, batch conversion, and production export, return to the SciDraw AI platform.

## Features

- Single-image output: one invocation produces one figure.
- Built-in ImageGen first: in Codex-style environments, no API key is usually required.
- API guidance when ImageGen is unavailable: if the current agent has no built-in image generation, the skill tells users to connect an available image generation API or use SciDraw AI online.
- Scientific use cases: roadmaps, mechanisms, method flows, research frameworks, model diagrams, and graphical abstract drafts.
- Source-aware prompting: when users provide source figures, labels, axes, or screenshots, the workflow can require preservation of key details.
- Platform handoff: for editable SVG/PPTX export, PNG/PDF/TIFF export, and full project workflows, use SciDraw AI on the web.

## Output Examples

The figure below was generated with Codex built-in ImageGen to verify the default image generation path for this skill.

![ImageGen demo: SciDraw AI scientific workflow](assets/examples/imagegen-demo-scidraw-workflow.png)

The examples below were downloaded from this project’s R2 assets and embedded into this repository.

| Funding Roadmap | NSFC Technical Roadmap |
| --- | --- |
| ![Funding Roadmap](assets/examples/case-1-funding-roadmap.png) | ![NSFC Technical Roadmap](assets/examples/case-2-nsfc-roadmap.png) |
| Research Logic Map | Digital Twin Workflow |
| ![Research Logic Map](assets/examples/case-3-research-logic.png) | ![Digital Twin Workflow](assets/examples/case-4-digital-twin.png) |

## Use Cases

- Research proposal roadmaps and grant application figures
- Paper graphical abstracts, TOC graphics, mechanism illustrations, and method diagrams
- Thesis, defense, teaching, and lecture visuals
- AI architecture, data pipeline, system workflow, and experiment design diagrams
- Turning early scientific ideas into structured visual drafts

## Output Structure

By default, each run produces one image file:

```text
{output_dir}/
└── figure_YYYYMMDD_HHMMSS.png
```

README example assets are stored in:

```text
assets/examples/
├── imagegen-demo-scidraw-workflow.png
├── case-1-funding-roadmap.png
├── case-2-nsfc-roadmap.png
├── case-3-research-logic.png
└── case-4-digital-twin.png
```

## Installation

### One-sentence install

Send this sentence to your agent:

```text
Please install this SciDraw AI scientific illustration skill: https://github.com/TopLocalAI/scidraw-ai-scientific-illustration-skill
```

### Manual install for Codex

```bash
npx -y skills@latest add TopLocalAI/scidraw-ai-scientific-illustration-skill \
  --skill scidraw-scientific-figure \
  --agent codex \
  --global
```

Restart Codex after installation.

## What If ImageGen Is Unavailable

> [!TIP]
> In Codex, if built-in ImageGen is available, you usually do not need an API key.

If the current agent does not provide built-in ImageGen, use one of these routes instead:

- Connect an image generation API in the current agent or platform, such as an OpenAI-compatible image model, API key, and base URL.
- Use SciDraw AI online: https://sci-draw.com/ai-drawing

You can tell the current agent:

```text
This environment has no built-in ImageGen. Please use the image generation API
available in this agent to create one scientific figure. If no image API is
available, open SciDraw AI: https://sci-draw.com/ai-drawing
```

## Usage

Ask Codex, Claude Code, OpenClaw, or Hermes Agent to use this skill explicitly:

```text
Use the scidraw-scientific-figure skill to generate one 16:9 scientific roadmap figure.
```

A strong request should include:

1. Purpose: paper figure, grant figure, thesis figure, teaching figure, model diagram
2. Aspect ratio: 16:9, 4:3, 1:1, or journal-specific dimensions
3. Logic structure: question, method, data, validation, output
4. Text language: English, Chinese, or mixed terminology
5. Visual style: white background, academic palette, low saturation, clear arrows, modular layout
6. Preservation constraints: labels, axes, legends, units, logos, or source figure content that must remain unchanged

Example prompt:

```text
Use the scidraw-scientific-figure skill to generate one scientific roadmap figure.
Aspect ratio: 16:9 landscape. Output only one image.
Topic: multi-omics disease stratification and biomarker discovery.
Structure: data acquisition -> AI integration -> explainability -> patient stratification -> clinical validation.
Style: white background, muted blue-green academic palette, clear modules and arrows.
Text: English labels, concise and readable.
```

## Tips

- Avoid vague prompts such as “draw a scientific figure.” Name the modules, arrow relationships, and final output.
- Keep labels concise, especially for Chinese figures.
- For grant figures, describe the scientific question, research tasks, technical route, and validation loop.
- For graphical abstracts, describe the main finding, mechanism, method, and application context.
- If labels, axes, units, or experimental figures must be preserved, say so explicitly.

## Relationship to SciDraw AI

This skill is a lightweight agent entry point for the SciDraw AI workflow. The SciDraw AI web platform is the complete product.

Use SciDraw AI directly when you need:

- AI Drawing online: https://sci-draw.com/ai-drawing
- sketch-to-professional scientific figure workflows
- image upload and follow-up editing
- raster image to editable SVG conversion
- image to PPTX with editable text layers
- PNG, PDF, and TIFF publication export
- complete workflows for papers, grants, posters, and teaching materials

## FAQ

- Do I need an API key?  
  Usually no in Codex when built-in ImageGen is available. If the current agent has no image tool, you need to connect an image generation API in that agent or use SciDraw AI online.
- Does this skill export SVG?  
  The skill itself outputs an image. For SVG/PPTX editable export, use SciDraw AI’s convert workflow.
- Can it generate multiple images at once?  
  This skill is intentionally designed for one image per invocation.
- Can the output be submitted directly to a journal?  
  Authors must verify scientific accuracy, labels, units, and journal formatting. SciDraw AI provides the fuller export workflow for production use.

## More SciDraw AI

For the complete scientific drawing experience, use SciDraw AI:

- AI Drawing: https://sci-draw.com/ai-drawing
- Website: https://sci-draw.com/
- Convert tools: https://sci-draw.com/convert

## License

MIT
