# Lumen Research

**让每个研究结论，都能找到它的问题、证据与边界。**

Lumen Research 是一个面向 AI 科研的 Agent Skill。它将文献调研、研究选题、实验设计、结果分析、论文写作、审稿和 rebuttal 组织成一套相互衔接的工作方法，帮助研究者从一个明确的问题出发，形成可检查的证据链。

它既可以参与完整研究流程，也可以只解决一个具体任务：比如核查某个 novelty claim、设计一组消融实验、解释统计结果，或逐条回应审稿人。

> 当前状态：私有仓库。除整合入口外，仓库同时保存本地完整论文写作 skill，便于换电脑原样迁移。

## 完整论文写作 skill

**需要原来完整的顶会论文写作规则，请直接使用 `$ccfa-paper-writing`，而不是只安装整合版 `lumen-research`。**

| 目录 | 内容 | 保存方式 |
| --- | --- | --- |
| [ccfa-paper-writing](skills/ccfa-paper-writing/SKILL.md) | 完整 CCF-A 论文写作与排版规范 | 本地原版逐文件复制，保留规则、参考资料、脚本和配置 |
| [edit-article](skills/edit-article/SKILL.md) | 文章结构、清晰度和语言修改 | 本地完整目录复制 |
| [writing-shape](skills/writing-shape/SKILL.md) | 将材料组织成文章和段落 | 本地完整目录复制 |
| [writing-beats](skills/writing-beats/SKILL.md) | 叙事展开和概念铺垫 | 本地完整目录复制 |
| [writing-fragments](skills/writing-fragments/SKILL.md) | 从零散材料中提炼写作内容 | 本地完整目录复制 |
| [pdf](skills/pdf/SKILL.md) | PDF 读取、生成与视觉检查 | 保留完整目录，包括许可和资源文件 |
| [lumen-research](skills/lumen-research/SKILL.md) | 科研流程的整合入口 | 独立编写；不替代上面的完整原版 |

`ccfa-paper-writing` 包含完整的 9 个文件：

```text
ccfa-paper-writing/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── writing-standard.md
│   ├── problem-boundary-and-hooks.md
│   ├── section-playbook.md
│   ├── revision-and-review.md
│   └── rendered-layout-audit.md
└── scripts/
    ├── audit_prose.py
    └── test_audit_prose.py
```

其中包括原版的问题边界、术语钩子、首次缩写定义、减少第一人称、非防御性写作、章节组织、短尾行、页面饱满度、题注间距，以及完整 PDF 逐页视觉检查规则。迁移时没有删减或改写；仅排除了 Python 自动生成的缓存。

## 核心理念

```text
研究问题 → 最接近的已有工作 → 可检验的假设
         → 能区分解释的实验 → 可追溯的证据 → 清晰的论文与回应
```

Lumen Research 将「做了什么」「观察到了什么」「结果支持什么」分开处理。它强调比较条件、数据来源、评估指标、适用范围和不确定性，鼓励提出可以证伪的假设，也保留负结果的研究价值。

## 能做什么

| 场景 | 适合交给 Lumen Research 的任务 | 典型输出 |
| --- | --- | --- |
| 文献调研 | 梳理研究方向、阅读关键论文、寻找相近工作 | 文献地图、对比表、研究空白及来源 |
| 研究选题 | 从方向生成 idea，分析价值、可行性和风险 | 假设、差异点、最小验证实验 |
| 创新性检查 | 检查问题、机制、评估设置与已有论文的重合 | 近邻论文比较、差异和不确定性 |
| 实验设计 | 设计主实验、消融、干预和诊断实验 | 假设—对照—指标—结果解释 |
| 结果分析 | 核对指标、差值、方差与数据口径 | 可追溯的结果表、发现及后续验证 |
| 论文写作 | 优化论文逻辑、论证、英文表达与术语 | 问题—方法—证据连贯的论文文本 |
| 审稿与 rebuttal | 拆解审稿意见，寻找已有证据并起草回应 | 问题—证据—策略矩阵及英文回复 |

## 设计原则

1. **证据先行**：数值、论文引用与实验结论必须有来源；缺失的信息明确标记。
2. **问题有边界**：写清楚任务、输入输出、假设、实验范围和不适用情形。
3. **叙事一环扣一环**：新概念先有动机，再定义，再用于论证。
4. **比较要公平**：说清数据、模型、训练预算、评价协议和统计单位。
5. **表达有力度，也有分寸**：有直接证据时清楚陈述；证据不足时明确限定，不靠防御性措辞掩盖问题。
6. **研究者掌握方向**：按照用户要求选择需要的阶段，不因为使用了 skill 就自动启动训练或提交内容。
7. **跨环境使用**：不依赖特定模型名、服务器路径或某个固定 MCP 服务。

## 安装

### Codex

登录有仓库权限的 GitHub 账号后，先克隆仓库：

```bash
git clone https://github.com/imhaojie/lumen-research.git ~/work/lumen-research
```

在尚未安装这些同名 skill 的新电脑上，把 `skills/` 下的完整目录复制到 Codex：

```bash
mkdir -p ~/.codex/skills
cp -R ~/work/lumen-research/skills/. ~/.codex/skills/
```

如果目标目录已经存在同名 skill，请先比较内容，避免覆盖自己之前的修改。完成后重启 Codex 或开启新对话，在对话中使用 `$ccfa-paper-writing` 调用完整论文写作规范，或使用 `$lumen-research` 调用科研整合入口。

### Claude Code

在尚未安装这些同名 skill 的新电脑上，将完整目录复制到 Claude Code 的个人 skill 目录：

```bash
mkdir -p ~/.claude/skills
cp -R ~/work/lumen-research/skills/. ~/.claude/skills/
```

重新启动 Claude Code 后，可使用 `/ccfa-paper-writing` 或 `/lumen-research`；具体调用方式和自动发现行为取决于安装版本。`references/`、`scripts/`、`agents/` 等必须和对应的 `SKILL.md` 一起复制。

克隆不会自动配置联网、GPU、实验环境、MCP 或账户凭证；相关任务需要新电脑具备对应能力。

### 更新

在仓库目录拉取新版本后，先比较本机已安装版本是否有独立修改，再更新对应 skill 目录。建议把 Git 仓库作为维护源，避免在多个位置分别修改后产生版本冲突。不要将 API Key、私有审稿意见、实验数据或服务器凭证放进公开仓库。

## 使用示例

### 1. 梳理研究方向

```text
$lumen-research 帮我梳理音频视觉分割中声音与运动对齐的研究。
请比较最相关的论文，指出各自的问题设定、方法差异和可验证的研究空白。
请给出原论文链接，并标出检索范围和日期。
```

### 2. 设计最小实验

```text
$lumen-research 我有一个多模态对齐方法。请先阅读项目中的方法描述和现有结果，
设计最少的消融和干预实验，说明每组实验排除什么替代解释，
以及不同结果分别支持什么结论。先不要启动训练。
```

### 3. 分析已有结果

```text
$lumen-research 分析 results/ 下的实验结果。
请区分绝对提升和相对提升，核对多种子统计，明确哪些结论能够由现有数据支持。
```

### 4. 润色论文

```text
$ccfa-paper-writing 帮我润色这篇论文的 Introduction 和 Experiments。
保留实验数字、方法定义和引用，检查问题边界、叙事衔接和证据是否支撑主张。
严格使用完整 skill 中的语言和格式规则；排版修改后逐页检查最终 PDF。
```

### 5. 准备 rebuttal

```text
$lumen-research 结合提交的正文、补充材料和全部审稿意见，
建立逐条问题—证据—回应策略矩阵，指出真正需要补实验的问题，
再根据字数限制撰写英文 rebuttal。不得虚构结果或修改已提交正文。
```

## 项目结构

```text
lumen-research/
├── README.md
├── SOURCES.md
└── skills/
    ├── ccfa-paper-writing/  # 完整原版：规则、5 份参考、脚本及配置
    ├── edit-article/
    ├── writing-shape/
    ├── writing-beats/
    ├── writing-fragments/
    ├── pdf/                # 包含 LICENSE.txt 和 assets/
    └── lumen-research/     # 科研流程整合入口
        ├── SKILL.md
        └── references/
            ├── discovery.md
            ├── experiments.md
            ├── writing.md
            └── review-rebuttal.md
```

`SKILL.md` 负责选择任务与核心原则；详细流程按需从 `references/` 加载。不同平台对 skill 的发现、权限、搜索和执行能力可能不同，具体行为以实际环境为准。

## 不适合期待什么

- 它不能单凭模型记忆保证文献检索完整，也不能证明一个想法绝对新颖。
- 它不会把缺少原始记录的结果变成可复现结果，也不会把拟议实验写成已完成实验。
- 它不会自动获得 GPU、搜索权限、付费 API 或外部评审资格。
- 研究判断、数据真实性、投稿规定和最终提交仍需要研究者核对。

## 来源与公开发布

本项目是对作者既有科研工作习惯及本地 skill 流程的独立整理。灵感、参考来源和待核验事项见 [SOURCES.md](SOURCES.md)。

本地初版尚未选择开源许可证；将仓库公开或宣称可自由再分发前，请先确认素材来源和权利，并由项目所有者选择适当的许可证。不要在未经核验的情况下将第三方 skill 原文打包为个人原创。
