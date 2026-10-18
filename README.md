# 无界探索 · 赛题 B

> 本文件是**提交用**的技术路线说明。
> 过程记录见 `DailyProgress.md`，学习笔记见 `LearningLog.md`。

## 进度速览

- 10.16 环境就绪：WSL2 + Ubuntu(jiuxiangz) + `~/wujie` + `.venv`（Python 3.14.4）+ requests -> JSON + git 本地仓库
- 10.17 代码仓库推送至 GitHub 成功 + DeepSeek 返回可解析的动作 JSON
- 10.18 装上 Miniconda（Python 环境管理工具）
- 10.18 打通 MineDojo：修复 2 处环境阻塞后跑通一次观测（`rgb` 3×160×256、前进 5 步坐标单调递增），七步第②步完成

## 一、方案与关键设计（待填写）

评分占比约 30%。写清：任务规划怎么做、代码/技能怎么执行、记忆与反馈怎么处理。

### 探索方向 · 已记录的想法（2026-10-18）

- 环境返回的观测字段目前固定为 9 个（`rgb` / `inventory` / `equipment` / `life_stats` / `location_stats` / `nearby_tools` / `damage_source` / `masks` / `delta_inv`）。
- **想法**：若能按任务需要**自行扩充观测字段**（例如把「最近 N 步的状态变化」或「目标物的相对方位」直接做成环境输出），或许能减少 Agent 每一步的推理负担。
- 状态：**待验证**。属改环境配置的进阶内容，可行性待官方文档与后续实验确认，当前不影响主线进度。

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
- MineDojo 环境：conda 环境 `minedojo`（Python 3.9）+ MineDojo 本体
- 系统依赖（**运行必需**）：`sudo apt install xvfb x11-xserver-utils`
  - `xvfb` —— 虚拟显示器，让无头环境能跑 Minecraft
  - `x11-xserver-utils` —— 提供 `xrandr` 命令（LWJGL 2.9.4 靠它枚举显示模式，缺了会直接崩）
- 无头运行方式：`xvfb-run -a -s "-screen 0 1024x768x24" python minedojo_observe.py`
- 已修复的上游问题：`Malmo/Minecraft/build.gradle` 的 MixinGradle 依赖源失效（jitpack 该 commit 构建为 `Error`）→ 改用 `repo.spongepowered.org` + `org.spongepowered:mixingradle:0.6-SNAPSHOT`
- 观测脚本：`minedojo_observe.py`（reset 打印首帧 + 前进 5 步，输出 `frame_reset.png` / `frame_step5.png`）
- 排障备用工具（**非运行必需**，仅用于定位问题，不影响复现）：
  - `glxinfo`（来自 `mesa-utils`）—— 检测「本环境到底有没有 OpenGL 能力、版本多少」。实测 Xvfb 下为 `llvmpipe` / OpenGL 4.5，据此**排除「显卡驱动缺失」**
  - `xdpyinfo`（来自 `x11-utils`）—— 检测「X 服务器提供哪些扩展与分辨率」。对比 WSLg 与 Xvfb 后确认两者都有 RANDR + GLX，据此**排除「X 服务器能力不足」**
  - 两者的作用是「排除法」：把显卡驱动、GL 能力、X 服务器扩展这三个方向逐个划掉，最后才锁定真因是**缺 `xrandr` 命令**

## 三、结果与局限分析（待填写）

评分占比约 30%。写清：测试结果、改动前后对比数据、失败原因与目前仍存在的问题。

## 四、引用与团队分工（待填写）

评分占比约 10%。写清：参考资料来源、团队成员各自负责的部分。
