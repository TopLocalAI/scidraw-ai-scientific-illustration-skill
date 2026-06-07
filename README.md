# SciDraw AI Scientific Illustration Skill（科研画图）

## English

SciDraw AI Scientific Illustration Skill is a **single-image scientific drawing skill**.
Each call generates exactly **one** figure image.

### What this skill can do

- Generate one high-quality scientific figure per request.
- Prefer Codex built-in image generation first; use API/CLI only when needed.
- Preserve source assets (existing charts, experimental figures, screenshots, logos) when users request strict fidelity.
- Keep prompt handling bilingual-friendly and easy to control for academic style.
- Output is designed for paper figures, thesis diagrams, and explanation graphics, not editable PPT editing.

### Installation

Recommended: install from one sentence in Agent:

- "Please install this skill: `https://github.com/TopLocalAI/scidraw-ai-scientific-illustration-skill`"

Manual installation (optional):

```bash
npx -y skills@latest add TopLocalAI/scidraw-ai-scientific-illustration-skill \
  --skill scidraw-scientific-figure \
  --agent codex \
  --global
```

Then restart your agent.

### How to use in interaction

Use like normal assistant request, but give constraints clearly:

1. Declare output intent: e.g. mechanism diagram / roadmap / method flow.
2. Give format: aspect ratio, language, palette, text density.
3. Say if strict inputs must be preserved (e.g., legend, axis, logo, labels).
4. Confirm one-image-only requirement.
5. Ask for refinement after first result if needed.

A typical prompt pattern:

```text
请生成一个[主题]的科研示意图，16:9横版；
只输出一张高清图片；
核心要素：...
颜色风格：...
文本语言：中文（可含英文术语）；
请保留输入中的所有关键标签和数值。
```

### Fallback CLI mode (API mode)

Fallback is only used when built-in generation is unavailable or explicitly requested.

1) Bootstrap environment:

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py bootstrap
```

2) Configure API (optional):

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py config \
  --api-key "YOUR_API_KEY" \
  --base-url "https://api.openai.com/v1" \
  --model gpt-image-2
```

3) Quick health check:

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py doctor --check-api
```

4) Generate one image:

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/image_gen.py \
  --prompt "A clear scientific diagram showing ..." \
  --size 2560x1440 \
  --quality medium \
  --out scidraw-ai-scientific-illustration-skill/outputs/figure.png
```

`image_gen.py` also supports:

- `--prompt-file /path/to/file.txt` or `--prompt-file -` (stdin)
- `--dry-run` for payload preview
- `--json` for machine-readable output

### Case gallery (from current project R2 storage)

These examples are direct links from this repository's R2 assets.

#### Example 1: Funding roadmap (4:3)

![Funding roadmap 1](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/sAlNGOlGoTRXz1TZXq8um4wi7n54PEF9/7aebfaf4-a4ba-44bf-8c28-b47624c5ded8/51e4735f-bab4-4921-a224-b655f7fca2cb.png)

#### Example 2: NSFC technical roadmap (4:3)

![NSFC technical roadmap](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/OcMVhRBPIurfOZ9nepCLqhxRfive9tED/d961261e-6a3a-494a-ad48-5c8539aa2b34/83eb825f-4601-498f-b05a-5daca5031869.png)

#### Example 3: Research logic map (16:9)

![Research logic map](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/DgVKMzbihz31LyqEQ9Ib2JmbPh1GBKkW/93e27e3a-3c41-47ac-b5ab-79e33310fbc6/8b927d5c-539f-47e1-ba78-708710a0dc07.png)

#### Example 4: Digital twin workflow (16:9)

![Digital twin workflow](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/a7lq8FcdQN8wJnJFW9qcpAxmclSSjWRA/142fef6e-b3a1-40aa-b88a-3f78a14f3ce3/0ab31310-0a61-4fa1-9112-e0ae6156cb7b.png)

#### Example 5: Multi-layer evidence chain diagram (16:9)

![Evidence chain diagram](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/fEkof8JSRYXtMgSqmLXjvyK67EK32ac1/4674d3fb-9938-411d-a41f-1569bca591ef/23609505-f571-40ef-922f-7e68fb988702.png)

#### Example 6: Biomedical hydrogel roadmap (16:9)

![Hydrogel roadmap](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/iFIkRCMAHl48AicZhtEjkA7pUFhCE4dO/f1598d6a-cc8a-462e-b01d-9f7074fbdd79/f563dd8d-17c8-4816-a5f8-a888cdeee094.png)

### FAQ

- This skill outputs one image only per invocation by design.
- If built-in image generation is available, API keys are usually not required.
- For API mode, `OPENAI_API_KEY` is required; optional `OPENAI_BASE_URL` and `SCIDRAW_FIGURE_MODEL` are also supported.
- If a prompt is unclear, include at least: audience, purpose, ratio, color preference, and label language.

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

---

## 中文

SciDraw AI 科研画图 Skill 是一个**单图输出**的科研图生成 skill：
每次只生成**一张**图片。

### 这个 skill 能做什么

- 一次生成一张科研示意图（技术路线图、机制图、流程图、模型结构图、对比图）
- 默认优先使用 Codex 内置图像能力，API/CLI 仅作兜底
- 支持“严格保留”输入素材（实验图、截图、Logo、坐标系标签等）
- 输出结果偏“直接用于论文/答辩/文档”的成片图，不是可编辑 PPT

### 安装方式

推荐：在你的 agent 里直接发一句安装指令：

- “请帮我安装这个 skill，链接是：https://github.com/TopLocalAI/scidraw-ai-scientific-illustration-skill”

手动安装（可选）：

```bash
npx -y skills@latest add TopLocalAI/scidraw-ai-scientific-illustration-skill \
  --skill scidraw-scientific-figure \
  --agent codex \
  --global
```

安装后重启你的 Agent 生效。

### 怎么用（交互逻辑）

按这个顺序给请求，成功率最高：

1. 先说用途：基金/NSFC 图、毕业论文图、课程汇报图、论文方法图……
2. 说清画幅：16:9、4:3、1:1 等
3. 给核心结构：模块名、阶段、关系箭头、输出物
4. 指定语言与风格：中文标签密度、学术配色、字体层次
5. 明确是否有“必须保留”素材
6. 明确说“只要一张图”，避免多图输出

示例提示词结构：

```text
请生成一张[场景]的科研图，16:9 横版，单图输出；
主题：...
主线：问题 -> 方法 -> 结果 -> 验证；
配色：...
文字：中文标签，字号可读，术语准确；
如果输入里有源图或公式，请严格保留关键要素；
```

### 回退 CLI 模式（如果你在非内置图像环境）

1）先初始化运行时：

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py bootstrap
```

2）配置 API（按需）：

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py config \
  --api-key "你的_API_KEY" \
  --base-url "https://api.openai.com/v1" \
  --model gpt-image-2
```

3）校验配置：

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py doctor --check-api
```

4）生成一张图：

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/image_gen.py \
  --prompt "请生成一张可直接用于论文的机制示意图，16:9..." \
  --size 2560x1440 \
  --quality medium \
  --out scidraw-ai-scientific-illustration-skill/outputs/figure.png
```

`image_gen.py` 还支持：

- `--prompt-file /path/to/file.txt` 或 `--prompt-file -`（标准输入）
- `--dry-run` 先看参数
- `--json` 生成结构化返回

### 案例（直接引用当前仓库 R2）

以下图片都来自仓库内公开的 R2 资源，可直接用于效果展示：

#### 案例1：基金驱动实施路径图

![案例1-基金驱动实施路径图](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/sAlNGOlGoTRXz1TZXq8um4wi7n54PEF9/7aebfaf4-a4ba-44bf-8c28-b47624c5ded8/51e4735f-bab4-4921-a224-b655f7fca2cb.png)

#### 案例2：国自然技术路线图

![案例2-国自然技术路线图](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/OcMVhRBPIurfOZ9nepCLqhxRfive9tED/d961261e-6a3a-494a-ad48-5c8539aa2b34/83eb825f-4601-498f-b05a-5daca5031869.png)

#### 案例3：国家基金研究逻辑关系图

![案例3-国家基金研究逻辑关系图](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/DgVKMzbihz31LyqEQ9Ib2JmbPh1GBKkW/93e27e3a-3c41-47ac-b5ab-79e33310fbc6/8b927d5c-539f-47e1-ba78-708710a0dc07.png)

#### 案例4：数字孪生基金插图

![案例4-数字孪生基金插图](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/a7lq8FcdQN8wJnJFW9qcpAxmclSSjWRA/142fef6e-b3a1-40aa-b88a-3f78a14f3ce3/0ab31310-0a61-4fa1-9112-e0ae6156cb7b.png)

#### 案例5：总体研究思路与实施策略

![案例5-总体研究思路与实施策略](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/fEkof8JSRYXtMgSqmLXjvyK67EK32ac1/4674d3fb-9938-411d-a41f-1569bca591ef/23609505-f571-40ef-922f-7e68fb988702.png)

#### 案例6：前药水凝胶技术路线图

![案例6-前药水凝胶技术路线图](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/iFIkRCMAHl48AicZhtEjkA7pUFhCE4dO/f1598d6a-cc8a-462e-b01d-9f7074fbdd79/f563dd8d-17c8-4816-a5f8-a888cdeee094.png)

### 常见问题

- 为什么默认不要求 API key？  
  因为在支持内置图像能力的环境里默认走内置，不需要配置外部模型。
- 什么时候会用 API 兜底？  
  内置能力不可用，或用户明确要求 API/CLI 生成时。
- 能不能一次生成多张？  
  当前 skill 策略是“单次只出 1 张”，避免输出混乱和返工。
- 你们会保留多少源图细节？  
  当用户明确要求“严格保留”时，会约束模型尽量保留结构、标签、坐标关系和数值表达。

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
