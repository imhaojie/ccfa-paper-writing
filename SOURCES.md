# 来源与发布准备

## 本地整理依据

本项目的 `skills/lumen-research/` 结合用户原有的论文写作偏好、科研任务和以下本地 skill 的工作思路，以新的结构编写。

- `ccfa-paper-writing`：问题边界、术语铺垫、证据驱动的论文叙事、减少防御性写作及渲染后检查。
- `research-lit`、`idea-creator`、`idea-discovery`、`novelty-check`：文献梳理、研究选题、近邻工作比较与验证。
- `run-experiment`、`monitor-experiment`、`analyze-results`：实验设计、运行状态和结果分析。
- `research-review`、`auto-review-loop`、`research-pipeline`：研究审查、证据链与阶段衔接。

原有 skill 的作者、上游地址及许可证尚未在本次整理中确认。公开前应追溯来源，核验是否需要署名或保留许可，并检查本项目文字及设计是否满足相关要求。不要将以上列表误认为已经完成来源核验。

## 完整目录备份

为满足换电脑时保留完整写作规则的需求，仓库另行原样保存了以下本地 skill，而不以整合入口的简述替代：

- `skills/ccfa-paper-writing/`：完整 9 个文件，包含入口、5 份参考资料、2 个脚本和 Codex 配置。
- `skills/edit-article/`、`skills/writing-shape/`、`skills/writing-beats/`、`skills/writing-fragments/`：各自完整的本地原版。
- `skills/pdf/`：完整的本地原版，保留自带的 `LICENSE.txt`、配置和图片资源。

仅排除 `__pycache__/`、`.pyc` 等自动生成缓存。原有本地安装目录未被修改。完整备份的 skill 保留各自名称和原文，不代表其全部内容均为仓库所有者原创。

## 公开发布前检查

- 确认项目作者展示名、品牌名称和公开联系方式。
- 检查名称在目标平台上是否已有冲突；目前未做商标或名称可用性检索。
- 核验本项目及参考来源的许可，再由项目所有者选择许可证。
- 用真实研究任务测试至少文献、实验分析、论文写作和 rebuttal 四种模式，并记录可复现的测试方法与不足。
- 检查不同 Agent 的 skill 加载方式，依据实际环境更新安装说明。
- 检查是否包含私人论文、审稿意见、密钥、本机敏感路径和其他不应公开的材料。
