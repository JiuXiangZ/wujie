# B 无界探索 · 学习指导（官方文档总结）

> 来源：飞书 wiki《B 无界探索 学习指导》
> https://pcnuxhluoos7.feishu.cn/wiki/ZJsgwD38iiNgvGkioVocxBAjnGh
> 整理日期：2026-10-16

---

## 01 · 赛题与学习路线

- **主角**：你设计的智能体（Agent），从**空背包**出发。
- **做什么**：在仿真开放世界里**采集资源、制作工具**，逐步完成**木制 → 石器 → 铁器**任务。
- **核心能力**：看懂当前状态 → 决定下一步行动 → **发现上一步行动有没有成功**（结果检查）。
- **入门建议**：先观察一次「**画面 → 动作 → 新画面**」的过程。
  → 可以让 Coding Agent 帮你装 MineDojo、跑官方示例，看角色如何移动、环境如何返回画面。
- **进阶路径**：短视频理解 Agent / 工具 / 记忆等概念 → 进阶课实现一个 Agent 循环 → 论文展开到任务规划、技能积累与开放世界探索。

相关：[赛题说明 PDF](https://pcnuxhluoos7.feishu.cn/wiki/CCrywxMwciiPrxklufNcXltPn4g) · [Wiki Agent](https://wiki.uestcai.top/zh/agent.html)

---

## 02 · GitHub 与实践代码

### MineDojo 官方代码
- 仓库：https://github.com/MineDojo/MineDojo
- 官方示例：创建仿真环境，让角色向前移动和跳跃。可改动作、观察画面变化。
- ⚠️ **重要：MineDojo 不支持 Windows 系统！**
  - **Windows 方案：WSL2 + Ubuntu**（在 Windows 中运行 Linux 环境）。
  - MineDojo 对 Python 版本有要求（见官方文档），**推荐在 WSL2 里装 Miniconda** 来管理隔离的 Python 环境。
  - Mac 方案：参考官方 macOS 安装说明，检查 JDK 8、Python 环境与依赖兼容性。
- 链接：[官方安装说明（含 macOS）](https://docs.minedojo.org/sections/getting_started/install.html) · [入门示例](https://docs.minedojo.org/sections/getting_started/sim.html) · [Windows WSL 安装说明](https://learn.microsoft.com/zh-cn/windows/wsl/install)

**官方给出的 Prompt（可直接发给 Coding Agent）：**
> 请根据 MineDojo 官方仓库和安装文档，结合我的系统版本、芯片和显卡检查环境，协助安装。说明命令在哪个终端执行，并为项目建立独立环境。运行官方示例，让我看到场景和角色移动；结合代码解释观察与动作，再尝试修改移动或跳跃行为。遇到报错时，请解释原因并协助排查。

### OpenClaw Agent 工程参考
- 仓库：https://github.com/openclaw/openclaw
- 说明：本题用不到它，但作为**稍大型的 Agent 项目**，读它能帮助建立宏观理解。
- 建议让 Coding Agent 带你读**工具调用、会话和记忆**模块，结合一次任务理解它们如何配合。

**官方 Prompt：**
> 请克隆并阅读 OpenClaw 官方仓库，定位工具调用与结果返回的实现。用中文解释一次调用经过哪些模块，并画出数据流。结合代码说明会话和记忆在其中的作用。

---

## 03 · 入门视频

| 视频 | 作者 | 内容 |
|---|---|---|
| [从 LLM 到 Agent Skill](https://www.bilibili.com/video/BV1E7wtzaEdq/) | 马克的技术工作坊 | 大语言模型、上下文、工具调用、MCP、Agent 与 Skill 之间的关系 |
| [Skill、MCP、RAG 与 Agent](https://www.bilibili.com/video/BV1ojfDBSEPv/) | 飞天闪客 | Skill、MCP、RAG、Agent、OpenClaw 的基本概念与用途 |

---

## 04 · 进阶课程

| 课程 | 作者 | 内容 |
|---|---|---|
| [Agent 的概念、原理与构建模式](https://www.bilibili.com/video/BV1TSg7zuEqR/) | 马克的技术工作坊 | 结合「简化版 Claude Code」，讲 **ReAct 循环**、工具调用、计划与执行 |
| [Hugging Face 中文 Agent 课程](https://huggingface.co/learn/agents-course/zh-CN/unit1/agent-steps-and-structure) | Hugging Face | 思考/行动/观察；配 [工具介绍](https://huggingface.co/learn/agents-course/zh-CN/unit1/tools) 与 [简单 Agent 实现](https://huggingface.co/learn/agents-course/zh-CN/unit1/dummy-agent-library) |

---

## 05 · 论文选读

### 怎么读
- 先看 [如何读论文（李沐）](https://www.bilibili.com/video/BV1H44y1t75x/)。
- 首次读：**摘要 → 方法图 → 一段任务轨迹**，不要逐句翻译。
- 把英文原文和图交给 AI，请它用中文讲清过程，并在官方代码里定位对应实现。
- 带着「**这一步为什么这样设计**」去读。

### 推荐阅读顺序：**ReAct → Voyager → MineDojo**

| 论文 | 为什么读 | 链接 |
|---|---|---|
| **ReAct**｜思考、行动与观察 | 「思考—行动—观察」循环**最贴近入门代码** | [PDF/原文](https://pcnuxhluoos7.feishu.cn/wiki/WJMlwNBPJi656HkDVqkc9HAknxc) · [项目](https://react-lm.github.io/) · [代码](https://github.com/ysymyth/ReAct) |
| **Voyager**｜技能积累与开放世界探索 | 展示**技能如何积累和复用**（技能库 + 迭代提示） | [PDF/原文](https://pcnuxhluoos7.feishu.cn/wiki/TgagwWvO6i4w53keLUWcTa8nnOb) · [项目](https://voyager.minedojo.org/) · [代码](https://github.com/MineDojo/Voyager) |
| **MineDojo**｜环境、任务与知识 | 介绍本题所用**环境背后的任务与资源** | [PDF/原文](https://pcnuxhluoos7.feishu.cn/wiki/N1MEwSF37iulyjkSJiXc3i7knVc) · [项目](https://minedojo.org/) · [代码](https://github.com/MineDojo/MineDojo) |

**读论文 Prompt：**
> 请结合这篇论文的方法图和相应正文，用中文解释输入、输出和各模块的作用。保留关键英文术语，公式中的符号请配一个小例子。标出解释对应的原文章节，并结合我提供的代码找到实现位置。

---

## 06 · 资料索引

- [赛题说明 PDF](https://pcnuxhluoos7.feishu.cn/wiki/CCrywxMwciiPrxklufNcXltPn4g)
- [ReAct · 思考、行动与观察](https://pcnuxhluoos7.feishu.cn/wiki/WJMlwNBPJi656HkDVqkc9HAknxc)
- [Voyager · 技能积累](https://pcnuxhluoos7.feishu.cn/wiki/TgagwWvO6i4w53keLUWcTa8nnOb)
- [MineDojo · 开放世界环境](https://pcnuxhluoos7.feishu.cn/wiki/N1MEwSF37iulyjkSJiXc3i7knVc)
- [返回学习指南](https://pcnuxhluoos7.feishu.cn/wiki/NqfCwy9HSiZjxDkQiLwcdoHznWc)

---

## ★ 对备赛最关键的三条结论

1. **MineDojo 不支持 Windows，官方点名推荐 WSL2 + Ubuntu** —— 说明在 Windows 上装 WSL2 是**官方指定路线**，不是绕路。
2. **官方推荐在 WSL2 里装 Miniconda** 管理隔离的 Python 环境（先用 venv 也能跑，但环境复杂后 Miniconda 更省事；注意 MineDojo 对 Python 版本有要求）。
3. **入门第一步是「跑通 MineDojo 官方示例」**，先看到「画面 → 动作 → 新画面」，再谈 Agent 循环。
