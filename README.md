# CCF-A Paper Writing

**问题边界清晰，论证一环扣一环，语言严谨自然，排版逐页检查。**

这是本地完整的 `ccfa-paper-writing` skill 的迁移与版本管理仓库，面向人工智能顶会英文论文的撰写、重构、润色和提交前检查。核心 skill 保持本地原版的全部规则、参考资料、检查脚本和配置，便于在新电脑继续使用同一套写作标准。

> 仓库当前为私有。主 skill 为 `skills/ccfa-paper-writing/`；其他目录是辅助工具，可按需安装。

## 核心能力

| 方面 | 完整规范中的要求 |
| --- | --- |
| 研究叙事 | 问题、失败机制、设计要求、方法、证据和结论形成连续论证 |
| 问题边界 | 明确任务、输入输出、假设、适用场景和实验支持的范围 |
| 概念铺垫 | 后文概念先有动机和定义，每个技术词都有前文钩子 |
| 科学表达 | 结论先行、解释机制、用证据支撑主张，减少防御性表述 |
| 语言风格 | 尽量减少作者第一人称，自然使用被动语态，避免括号堆积和数字罗列 |
| 缩写与术语 | 每个独立文档首次写全称和缩写，之后保持统一 |
| 章节组织 | 控制小节数量，避免碎片化标题和技术报告式展开 |
| PDF 排版 | 检查短尾行、页面留白、栏底平衡、浮动体和题注间距 |
| 视觉核验 | 渲染后逐页检查，修改影响排版后重新核验 |
| 事实保护 | 保留实验数值、引用、方法定义和用户锁定的内容 |

所有详细要求以 [完整 SKILL.md](skills/ccfa-paper-writing/SKILL.md) 和它引用的参考文件为准。

## 完整文件

核心 skill 共 9 个文件，迁移时原样保留：

```text
skills/ccfa-paper-writing/
├── SKILL.md
├── agents/
│   └── openai.yaml
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

| 文件 | 用途 |
| --- | --- |
| [SKILL.md](skills/ccfa-paper-writing/SKILL.md) | skill 入口、核心原则、工作流程与完成标准 |
| [writing-standard.md](skills/ccfa-paper-writing/references/writing-standard.md) | 语言、论证和科研表达标准 |
| [problem-boundary-and-hooks.md](skills/ccfa-paper-writing/references/problem-boundary-and-hooks.md) | 问题边界、术语依赖和概念钩子 |
| [section-playbook.md](skills/ccfa-paper-writing/references/section-playbook.md) | 各论文章节的任务和展开方式 |
| [revision-and-review.md](skills/ccfa-paper-writing/references/revision-and-review.md) | 修改、审查和提交前检查 |
| [rendered-layout-audit.md](skills/ccfa-paper-writing/references/rendered-layout-audit.md) | 渲染后逐页视觉审查流程 |
| [audit_prose.py](skills/ccfa-paper-writing/scripts/audit_prose.py) | 本地语言与格式规则辅助检查 |
| [test_audit_prose.py](skills/ccfa-paper-writing/scripts/test_audit_prose.py) | 检查脚本的测试 |
| [openai.yaml](skills/ccfa-paper-writing/agents/openai.yaml) | Codex 展示和默认调用配置 |

仅排除 Python 自动生成的缓存。请复制整个目录，避免遗漏参考资料或脚本。

## 安装

先登录有私有仓库权限的 GitHub 账号，克隆到自己选择的位置。以下示例使用 `~/work/ccfa-paper-writing`：

```bash
git clone https://github.com/imhaojie/ccfa-paper-writing.git ~/work/ccfa-paper-writing
```

### Codex

在尚未安装同名 skill 的新电脑上：

```bash
mkdir -p ~/.codex/skills
cp -R ~/work/ccfa-paper-writing/skills/ccfa-paper-writing ~/.codex/skills/
```

重启 Codex 或开启新对话，然后使用 `$ccfa-paper-writing`。如果目标目录已经存在，请先比较版本，保留自己已有的修改。

### Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R ~/work/ccfa-paper-writing/skills/ccfa-paper-writing ~/.claude/skills/
```

重新启动后使用 `/ccfa-paper-writing`；具体发现和加载行为以实际安装版本为准。同名目录已存在时，先比较内容再更新。

### 按需安装辅助 skill

仓库也保留以下完整目录：

| Skill | 用途 |
| --- | --- |
| [edit-article](skills/edit-article/SKILL.md) | 文章结构和语言编辑 |
| [writing-shape](skills/writing-shape/SKILL.md) | 从材料组织文章与段落 |
| [writing-beats](skills/writing-beats/SKILL.md) | 叙事展开和概念铺垫 |
| [writing-fragments](skills/writing-fragments/SKILL.md) | 提炼零散写作材料 |
| [pdf](skills/pdf/SKILL.md) | PDF 处理和视觉检查，附带原有许可与资源 |
| [lumen-research](skills/lumen-research/SKILL.md) | 之前整理的科研流程入口，可选安装 |

安装辅助工具时，将需要的完整目录复制到对应平台的 skill 目录即可。

## 使用示例

### 整篇论文润色

```text
$ccfa-paper-writing 仔细阅读正文、补充材料和实验结果记录，
先分析叙事、问题边界和证据链，再润色全文。
保持实验数值、方法定义和引用不变，修改排版后逐页检查 PDF。
```

### 局部章节修改

```text
$ccfa-paper-writing 润色 Abstract、Introduction 和 Related Work。
围绕论文的核心问题和贡献展开，减少括号、数据堆砌和防御性表述，
保证术语首次出现前有动机，缩写定义后统一使用。
```

### 排版检查

```text
$ccfa-paper-writing 渲染最终 PDF 并逐页检查短尾行、页面留白、
双栏平衡、图表位置和题注间距。只进行有科学意义的小范围扩写或改写，
保留论文事实，遵守会议模板。
```

### 提交前审查

```text
$ccfa-paper-writing 检查正文与补充材料的主张、结果、术语和交叉引用，
指出未解决的问题。先报告发现，未经授权不要修改已提交版本。
```

## 本地检查

检查脚本为辅助工具，其提示需要结合上下文判断：

```bash
python3 skills/ccfa-paper-writing/scripts/audit_prose.py path/to/paper.tex
```

运行脚本测试：

```bash
cd skills/ccfa-paper-writing
python3 -m unittest discover -s scripts -p 'test_*.py'
```

PDF 编译、渲染和视觉检查需要使用环境提供对应能力；复制 skill 文件不会自动安装 LaTeX、渲染工具或配置模型。

## 更新与来源

将本仓库作为维护和迁移的版本源。更新时先拉取仓库，再比较已安装目录是否存在独立修改。原有本地 skill 保持原样；本次整理将其完整副本保存到仓库。

参考来源、完整备份说明与公开准备事项见 [SOURCES.md](SOURCES.md)。仓库当前为私有，尚未选择统一的开源许可证；附带的第三方许可文件继续保留。
