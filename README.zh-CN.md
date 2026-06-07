# SciDraw AI 科研画图 Skill

## 这是什么 Skill

这是一个给 Codex 风格 Agent 用的**单图科研画图 skill**。

- 每次只生成 **1 张**图片。
- 适合论文、基金申请、课程汇报、研发方案中的科研示意图。
- 覆盖技术路线图、机制示意图、流程图、模型结构图、对比图。
- 默认不支持可编辑 PPT、可编辑矢量（SVG）等完整编辑链路。

## 关于 SciDraw AI

这个 skill 只负责“单图生成”。如果你需要更完整的流程和产品能力，建议直接在 SciDraw AI 使用：

- 官网：`https://sci-draw.com/`
- 科研图生成首页：`https://sci-draw.com/ai-scientific-illustration`
- 结果转可编辑/转换流程：`https://sci-draw.com/convert`
- 价格/会员与积分：`https://sci-draw.com/pricing`

### 为什么还要用这个 Skill

- 在 Agent 对话里快速出单张图，适合审稿前快速迭代。
- 支持精细化提示词控制，减少一次生成偏差。
- 内置能力可用时无需 API key，流程更简洁。
- 仅当内置不可用时使用 fallback API 兜底。

## 安装方式

你可以直接对你的 Agent 说：

> 请帮我安装这个 skill，链接是：https://github.com/TopLocalAI/scidraw-ai-scientific-illustration-skill

手动安装（Codex）：

```bash
npx -y skills@latest add TopLocalAI/scidraw-ai-scientific-illustration-skill \
  --skill scidraw-scientific-figure \
  --agent codex \
  --global
```

重启 Agent 后生效。

## 怎么用（核心）

建议按这个顺序给任务：

1. 先说用途（技术路线图/方法流程图/机制图/论文图等）
2. 明确画幅（16:9、4:3、1:1）
3. 说明语言与文字密度（中文优先、中文+英文术语）
4. 说明结构主线（问题 → 方法 → 结果 → 验证）
5. 明确是否严格保留源图、标签、坐标、单位
6. 说清“只要一张图”

示例：

```text
请生成一张科研技术路线图，16:9。
只输出一张图片，中文标签，白底、学术风。
主题：...
阶段：第一阶段... 第二阶段... 第三阶段...
时间顺序从左到右，箭头清晰，输出可读。
如果输入里有源图或坐标，请严格保留关键标签和数值。
```

### 内置图像与 API 回退

- 有内置图像能力：优先走内置，不需要先配 API。
- 无内置或你要外部接口时：走 `image_gen.py` 回退模式。

## 回退 CLI 使用

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py bootstrap
```

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py config \
  --api-key "你的 API KEY" \
  --base-url "https://api.openai.com/v1" \
  --model gpt-image-2
```

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/codex_scidraw_runtime.py doctor --check-api
```

```bash
python3 scidraw-ai-scientific-illustration-skill/scripts/image_gen.py \
  --prompt "一张可用于论文/基金的机制示意图" \
  --size 2560x1440 \
  --quality medium \
  --out scidraw-ai-scientific-illustration-skill/outputs/figure.png
```

`image_gen.py` 还支持：

- `--prompt-file /path/to/prompt.txt`
- `--prompt-file -`（从标准输入读）
- `--dry-run`
- `--json`

## 案例（来自仓库 R2 资源）

- [基金驱动实施路径图](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/sAlNGOlGoTRXz1TZXq8um4wi7n54PEF9/7aebfaf4-a4ba-44bf-8c28-b47624c5ded8/51e4735f-bab4-4921-a224-b655f7fca2cb.png)
- [国自然技术路线图](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/OcMVhRBPIurfOZ9nepCLqhxRfive9tED/d961261e-6a3a-494a-ad48-5c8539aa2b34/83eb825f-4601-498f-b05a-5daca5031869.png)
- [国家基金研究逻辑关系图](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/DgVKMzbihz31LyqEQ9Ib2JmbPh1GBKkW/93e27e3a-3c41-47ac-b5ab-79e33310fbc6/8b927d5c-539f-47e1-ba78-708710a0dc07.png)
- [数字孪生基金插图](https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/a7lq8FcdQN8wJnJFW9qcpAxmclSSjWRA/142fef6e-b3a1-40aa-b88a-3f78a14f3ce3/0ab31310-0a61-4fa1-9112-e0ae6156cb7b.png)

你可以直接拉到本地保存到案例素材库：

```bash
mkdir -p examples && cd examples
curl -L -O "https://pub-8c0ddfa5c0454d40822bc9944fe6f303.r2.dev/ai-drawings/OcMVhRBPIurfOZ9nepCLqhxRfive9tED/d961261e-6a3a-494a-ad48-5c8539aa2b34/83eb825f-4601-498f-b05a-5daca5031869.png"
```

## FAQ

- **这个 skill 支持 SVG 吗？**  
  不支持直接生成可编辑 SVG。要 SVG 或可编辑流程，请去 SciDraw AI 平台。
- **没有 API Key 能用吗？**  
  有内置生图时可以直接用；无内置时才需要 API 回退。
- **我可以一次生成多页吗？**  
  不能。这个 skill 的设计目标是单图输出。

## 目录结构

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

