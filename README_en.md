# SciDraw AI Scientific Illustration Skill

[![中文](https://img.shields.io/badge/docs-%E4%B8%AD%E6%96%87-red)](./README.md)
[![SciDraw AI](https://img.shields.io/badge/SciDraw%20AI-AI%20Drawing-0f766e)](https://sci-draw.com/ai-drawing)
[![GitHub stars](https://img.shields.io/github/stars/TopLocalAI/scidraw-ai-scientific-illustration-skill?style=flat&logo=github&label=stars)](https://github.com/TopLocalAI/scidraw-ai-scientific-illustration-skill/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/TopLocalAI/scidraw-ai-scientific-illustration-skill?style=flat&logo=github&label=forks)](https://github.com/TopLocalAI/scidraw-ai-scientific-illustration-skill/forks)

A reusable agent skill for generating high-quality scientific figures with the official SciDraw AI web app and public API. It works with Codex, Claude Code, OpenClaw, Hermes Agent, and other agents that support `SKILL.md`.

> [!TIP]
> Use [SciDraw AI](https://sci-draw.com/ai-drawing) directly in the browser, or connect the included Python client to the official SciDraw AI API:
>
> - [AI Drawing](https://sci-draw.com/ai-drawing)
> - [SciDraw AI website](https://sci-draw.com/)
> - [Create an API key](https://sci-draw.com/settings/api-keys)
> - [API documentation](https://sci-draw.com/docs/api)
> - [Convert tools for SVG/PPTX/PDF/TIFF workflows](https://sci-draw.com/convert)
>
> The SciDraw AI platform supports AI Drawing, sketch-to-professional-figure workflows, image editing, editable SVG/PPTX export, and publication-ready PNG/PDF/TIFF export. This skill covers scientific figure generation and prompt structuring inside agent workflows.

## Friendly Note

This repository is the official agent entry point for SciDraw AI. Connect the [SciDraw AI MCP server](https://sci-draw.com/mcp) first (account sign-in, no API key); when its tools are available the skill uses them. Otherwise the skill plans a scientific figure, sends generation requests to SciDraw AI when `SCIDRAW_API_KEY` is configured, downloads the result, and guides review and iteration. It does not silently substitute another image provider.

For interactive editing, SVG/PPTX conversion, batch workflows, and publication exports, use the full SciDraw AI web platform.

## Features

- Figure-by-figure iteration: by default, the skill structures prompts and outputs around one scientific figure at a time, making layout, labels, and style easier to review. Multi-figure work can be generated figure by figure.
- Official SciDraw backend: direct API generation uses `SCIDRAW_API_KEY` and the included standard-library Python client.
- Browser fallback: without an API key, use the SciDraw AI online drawing workflow.
- No provider confusion: another image backend is used only when the user explicitly requests it.
- Scientific use cases: roadmaps, mechanisms, method flows, research frameworks, model diagrams, and graphical abstract drafts.
- Source-aware prompting: when users provide source figures, labels, axes, or screenshots, the workflow can require preservation of key details.
- Platform handoff: for editable SVG/PPTX export, PNG/PDF/TIFF export, and full project workflows, use SciDraw AI on the web.

## Examples

### From Research Idea to Scientific Figure

[![SciDraw AI scientific workflow](assets/examples/imagegen-demo-scidraw-workflow.png)](https://sci-draw.com/ai-drawing)

### Scientific Figure Examples

| Sketch to Export Workflow | Biomarker Discovery Roadmap |
| --- | --- |
| [![Sketch to export workflow](assets/examples/english-sketch-to-export.png)](https://sci-draw.com/ai-drawing) | [![Biomarker discovery workflow](assets/examples/english-biomarker-workflow.png)](https://sci-draw.com/ai-drawing) |

| Hydrogel Drug Delivery | Soil Carbon Monitoring |
| --- | --- |
| [![Hydrogel drug delivery mechanism](assets/examples/english-hydrogel-delivery.png)](https://sci-draw.com/ai-drawing) | [![Soil carbon monitoring workflow](assets/examples/english-soil-carbon-monitoring.png)](https://sci-draw.com/ai-drawing) |

## Use Cases

- Research proposal roadmaps and grant application figures
- Paper graphical abstracts, TOC graphics, mechanism illustrations, and method diagrams
- Thesis, defense, teaching, and lecture visuals
- AI architecture, data pipeline, system workflow, and experiment design diagrams
- Turning early scientific ideas into structured visual drafts

## Output Structure

By default, the skill outputs an image file for the current scientific figure, making it easy to review and refine each figure:

```text
{output_dir}/
└── figure_YYYYMMDD_HHMMSS.png
```

README example assets are stored in:

```text
assets/examples/
├── imagegen-demo-scidraw-workflow.png
├── english-sketch-to-export.png
├── english-biomarker-workflow.png
├── english-hydrogel-delivery.png
└── english-soil-carbon-monitoring.png
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
  --skill scidraw-ai-scientific-illustration \
  --agent codex \
  --global
```

You can also install it with GitHub CLI Agent Skills:

```bash
gh skill install TopLocalAI/scidraw-ai-scientific-illustration-skill \
  scidraw-ai-scientific-illustration \
  --agent codex \
  --scope user
```

Restart Codex after installation.

## SciDraw AI API

> [!TIP]
> Direct API generation consumes SciDraw AI credits. The skill asks for confirmation before starting a credit-consuming request.

Create a key at [SciDraw AI API Keys](https://sci-draw.com/settings/api-keys), then store it locally without committing it:

```bash
export SCIDRAW_API_KEY='sd_YOUR_KEY'
```

The included client uses Python 3 standard-library modules only. It calls `POST /api/v1/images/generations`, polls the returned job, and downloads the generated image. See the [API documentation](https://sci-draw.com/docs/api) and `skills/scidraw-ai-scientific-illustration/SKILL.md` for the complete workflow. Never paste or commit a real key.

## Usage

Ask Codex, Claude Code, OpenClaw, or Hermes Agent to use this skill explicitly:

```text
Use the scidraw-ai-scientific-illustration skill to generate a 16:9 scientific roadmap figure with SciDraw AI.
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
Use the scidraw-ai-scientific-illustration skill to generate a scientific roadmap figure with SciDraw AI.
Aspect ratio: 16:9 landscape.
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

This skill is a lightweight agent entry point for the [SciDraw AI](https://sci-draw.com/ai-drawing) workflow. The SciDraw AI web platform is the complete product.

SciDraw AI provides:

- [AI Drawing online](https://sci-draw.com/ai-drawing)
- sketch-to-professional scientific figure workflows
- image upload and follow-up editing
- raster image to editable SVG conversion
- image to PPTX with editable text layers
- PNG, PDF, and TIFF publication export
- complete workflows for papers, grants, posters, and teaching materials

## FAQ

- Do I need an API key?  
  No, if you connect the [SciDraw AI MCP server](https://sci-draw.com/mcp): it signs in with your SciDraw AI account and the skill uses it automatically. An API key is only needed for the bundled Python client.
- Does this skill export SVG?  
  The skill itself outputs an image. For SVG/PPTX editable export, use SciDraw AI’s convert workflow.
- Can it generate multiple figures?  
  Yes. For better control, generate them figure by figure so each layout, label set, and visual style can be reviewed. For batch conversion, editable export, and full project workflows, use the SciDraw AI platform.
- Can the output be submitted directly to a journal?  
  Authors must verify scientific accuracy, labels, units, and journal formatting. SciDraw AI provides the fuller export workflow for production use.

## More SciDraw AI

The complete scientific drawing workflow is available in [SciDraw AI](https://sci-draw.com/ai-drawing):

- [AI Drawing](https://sci-draw.com/ai-drawing)
- [Website](https://sci-draw.com/)
- [Convert tools](https://sci-draw.com/convert)

## License

MIT
