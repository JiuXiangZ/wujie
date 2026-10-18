# 无界探索 · 赛题 B

> 本文件是**提交用**的技术路线说明。
> 过程记录见 `DailyProgress.md`，学习笔记见 `LearningLog.md`。

## 进度速览

- 10.16 环境就绪：WSL2 + Ubuntu(jiuxiangz) + `~/wujie` + `.venv`（Python 3.14.4）+ requests -> JSON + git 本地仓库
- 10.17 代码仓库推送至 GitHub 成功 + DeepSeek 返回可解析的动作 JSON
- 10.18 装上 Miniconda（Python 环境管理工具，为后面安装 MineDojo 做准备）

## 一、方案与关键设计（待填写）

评分占比约 30%。写清：任务规划怎么做、代码/技能怎么执行、记忆与反馈怎么处理。

## 二、实现与复现（待填写）

评分占比约 30%。写清：环境与依赖、运行步骤、别人照着能否跑出同样结果。

### 环境与依赖（已完成部分）

- 系统：Windows + WSL2（Ubuntu 26.04.1 LTS，用户 jiuxiangz）
- 工作区：`~/wujie`
- Python 环境：venv（Python 3.14.4），已装 `requests`、`python-dotenv`
- 环境管理：Miniconda 3（conda 26.9.3，路径 `/home/jiuxiangz/miniconda3`），为后续安装 MineDojo 准备
- 密钥：`.env` 存 `DS_API_KEY`，已写入 `.gitignore`（不进仓库）
- 代码仓库：GitHub `JiuXiangZ/wujie`
- 复现命令：`python -m venv .venv && source .venv/bin/activate && python -m pip install requests python-dotenv`

## 三、结果与局限分析（待填写）

评分占比约 30%。写清：测试结果、改动前后对比数据、失败原因与目前仍存在的问题。

## 四、引用与团队分工（待填写）

评分占比约 10%。写清：参考资料来源、团队成员各自负责的部分。
