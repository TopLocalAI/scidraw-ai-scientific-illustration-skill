# SciDraw AI 科研画图 Skill

[![English](https://img.shields.io/badge/docs-English-blue)](./README.en.md)

这是一个给 Codex / 类 Codex Agent 用的**单图科研画图 skill**。  
每次只生成 **1 张**高质量科研图像（不是 PPT 项目，不是可编辑 SVG/PPT）。

> [!TIP]
> 这个 skill 的重点是“快 + 稳 + 单图”，适合一张图一次到位；如果你需要完整平台能力（批量出图、完整编辑链路、SVG 导出、可配置工作流），请优先用 SciDraw 官网：
>
> - https://sci-draw.com/
> - 生成页面：https://sci-draw.com/ai-scientific-illustration
> - 转换/编辑流程：https://sci-draw.com/convert

## 温馨提示

这个 skill 仅覆盖“按提示词产出单张科研图”的核心场景。  
如果你是第一次使用，建议直接走内置生图模式；如果内置能力不可用，再用 API/CLI 回退。

你也可以让 AI 把你常用的参数（比例、配色、提示词结构）固化到一个标准化流程中，后续不必反复重复设置。

## 特点

- 每次只输出 1 张图，结果更可控。
- 优先走内置图像能力（Codex-style 环境默认如此）。
- 无内置时支持 CLI/API fallback。
- 适配基金图、路线图、机制图、方法流程图、模型结构图、对比图等。
- 支持输入源素材为“严格要求”时保留关键结构、标签与坐标。
- 默认不直接提供可编辑 PPT / SVG 输出（如需这些功能建议去 SciDraw）。

## 安装

### 一句话安装（推荐）

你可以对 Agent 说：

```text
请帮我安装这个 skill，链接是：https://github.com/TopLocalAI/scidraw-ai-scientific-illustration-skill
```

### 手动安装（Codex）

```bash
npx -y skills@latest add TopLocalAI/scidraw-ai-scientific-illustration-skill \
  --skill scidraw-scientific-figure \
  --agent codex \
  --global
```

安装后重启 Agent 生效。

## 生图模型配置（API 回退）

如果你是在内置生图可用环境，一般不需要 API Key。  
只有在 API/CLI 回退场景才需要配置，命令如下：

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py config \
  --api-key "你的 API KEY" \
  --base-url "https://api.openai.com/v1" \
  --model gpt-image-2
```

健康检查：

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py doctor --check-api
```

## 使用方式（建议流程）

1. 说明图像用途（例如：基金技术路线图/机制示意图/课程汇报图）
2. 指定画幅（16:9、4:3、1:1）
3. 指定语言与标签密度（中文优先、中文+英文术语）
4. 描述结构主线（问题→方法→结果→验证）
5. 标注是否“严格保留”输入中的标签、坐标、图例、单位
6. 明确“只要一张图”

示例：

```text
请生成一张科研技术路线图（16:9），只输出 1 张图。
核心内容：基金研究问题、研究阶段（1/2/3）、每阶段成果、验证路径。
视觉风格：白底、学术配色、文字清晰可读。
输出语言：中文，保留必要英文术语。
如果有源图关键标签，请严格保持不变。
```

## 回退 CLI 生成（可选）

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py bootstrap
```

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/image_gen.py \
  --prompt "请生成一张中文的科研机制示意图，16:9" \
  --size 2560x1440 \
  --quality medium \
  --out scidraw-ai-scientific-illustration-skill/outputs/figure.png
```

`image_gen.py` 还支持：

- `--prompt-file /path/to/prompt.txt`
- `--prompt-file -`（标准输入）
- `--dry-run`
- `--json`

## 案例（已从仓库 R2 下载到本仓库）

### 1. 基金驱动实施路径图

![基金驱动实施路径图](assets/examples/case-1-funding-roadmap.png)

### 2. 国自然技术路线图

![国自然技术路线图](assets/examples/case-2-nsfc-roadmap.png)

### 3. 研究逻辑关系图

![研究逻辑关系图](assets/examples/case-3-research-logic.png)

### 4. 数字孪生基金插图

![数字孪生基金插图](assets/examples/case-4-digital-twin.png)

## FAQ

- 这个 skill 能生成 SVG 吗？  
  不支持可编辑 SVG。建议在 SciDraw 平台走完整编辑/导出链路。
- 没有 API key 能用吗？  
  有内置生图能力时可以直接使用；否则走回退模式需配置 API。
- 可以一次输出多图吗？  
  不可以，当前设计是单图输出。
- 能直接嵌入论文原图吗？  
  可以把来源图转为严格保留约束，由提示词要求保留坐标、标签和单位。

## 目录结构

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

