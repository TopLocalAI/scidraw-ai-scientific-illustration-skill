# SciDraw AI Scientific Figure Skill

## English

SciDraw AI Scientific Figure Skill is a single-image scientific illustration skill: one request produces **one** high-quality figure image.

### Highlights

- English-first workflow and `SKILL.md` in English.
- Output policy: one image per invocation.
- Built-in image generation preferred; API fallback available.
- Source-asset aware (charts, figures, logos) when users require strict preservation.
- Bilingual project documentation (`README.md` below).

### Use cases

- Mechanism diagrams
- Scientific process flows
- Model architecture illustrations
- Metric/benchmark comparisons
- Architecture / pipeline summaries

### Folder structure

```text
scidraw-ai-scientific-illustration-skill/
├── SKILL.md
├── README.md
├── requirements.txt
├── .gitignore
└── scripts/
    ├── codex_scidraw_runtime.py
    └── image_gen.py
```

### Fallback CLI usage

1) Bootstrap runtime:

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py bootstrap
```

2) Configure API (if needed):

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py config \
  --api-key "YOUR_API_KEY" \
  --model gpt-image-2
```

3) Generate one image:

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/image_gen.py \
  --prompt "A clear scientific diagram showing ..." \
  --size 2560x1440 \
  --quality medium \
  --out scidraw-ai-scientific-illustration-skill/outputs/figure.png
```

### Notes

- Built-in mode should stay preferred in Codex-like environments.
- Fallback mode is only used when built-in image tool is unavailable or the user explicitly requests API mode.
- `image_gen.py` accepts `--prompt-file` (or stdin with `--prompt-file -`).

---

## 中文

SciDraw AI 科研画图 Skill 是一个**单图输出**工作流：每次请求只生成一张高质量科研示意图。

### 特性

- `SKILL.md` 使用英文，便于在 AI agent 工具生态中直接使用。
- 每次仅输出一张图片。
- 优先使用内置图片工具；仅在内置不可用或用户要求时走 API/CLI 回退。
- 支持来源素材（实验图、结果图、Logo、截图）作为“严格输入”保留。
- 文档中文/英文同页双语。

### 适用场景

- 机制示意图
- 科研流程图
- 模型/网络结构图
- 指标对比图
- 架构与流程总结图

### 目录结构

```text
scidraw-ai-scientific-illustration-skill/
├── SKILL.md
├── README.md
├── requirements.txt
├── .gitignore
└── scripts/
    ├── codex_scidraw_runtime.py
    └── image_gen.py
```

### 回退模式使用方式

1）初始化运行时：

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py bootstrap
```

2）写入配置（如需要）：

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py config \
  --api-key "你的_API_KEY" \
  --model gpt-image-2
```

3）生成单图：

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/image_gen.py \
  --prompt "清晰展示该实验方法中的关键结构关系" \
  --size 2560x1440 \
  --quality medium \
  --out scidraw-ai-scientific-illustration-skill/outputs/figure.png
```

### 说明

- 在支持内置图像能力的环境中，优先走内置工具。
- API 回退是兜底方案，不自动替代内置能力。
- `image_gen.py` 支持 `--prompt-file`（也可用 `--prompt-file -` 从标准输入读入 prompt）。
