# 实验与进度记录

> 用途：**答辩与 README 的素材库**

## 2026-10-16（环境搭建）

- 装好 WSL2 + Ubuntu（WSL 3.0.3，用手动下载 MSI 安装，绕开 wsl --install 下载超时）
- 建工作区 ~/wujie，创建 Linux venv（Python 3.14.4），装 requests
- probe.py 跑通 requests → JSON：请求 GitHub API
  - 状态码 200，解析出 microsoft/WSL，stars 34108
- Git 仓库初始化：git init → 分支改 main
  - 配置 user.name / user.email
  - 建 .gitignore（.venv/、__pycache__/、*.pyc）
  - 首次提交 7d7223f「首次提交：requests→JSON 探针跑通」（2 个文件）
- 推送到 GitHub：仓库 JiuXiangZ/wujie，git push -u origin main 成功，main 已跟踪 origin/main
  - 注：推送实际在 10.17 凌晨完成
- 踩坑记录
  - wsl --install 下载超时 → 改用手动下载 WSL MSI 安装包
  - 官方学习指导：MineDojo 不支持 Windows，推荐 WSL2 + Ubuntu

## 2026-10-17

- 环境：WSL2 + Ubuntu，venv 激活成功（cd ~/wujie && source .venv/bin/activate）
- **第①步 · 调通 LLM API**：用 DeepSeek（deepseek-chat）拿到结构化动作 JSON
  - 模型原文：{"name":"move","args":{"direction":"forward","distance":1}}
  - 验收：连跑 3 次，json.loads() 均成功
  - 脚本：call_llm.py
- **对比实验**（样本各 5 次，仅观察不下结论）

  | 组别 | 解析成功 | 说明 |
  | --- | --- | --- |
  | 带 response_format | 5/5 | 脚本：compare_json.py |
  | 不带 response_format | 5/5 | 同样 5/5，未见差别 |

  - 观察：提示词本身的约束已足够，response_format 在这 5 次里没有带来额外收益（样本仅 5 次，不足以定论）
- 踩坑记录
  - 新开终端忘记激活 venv → pip 报 externally-managed-environment
  - 解决：先 source .venv/bin/activate，且统一用 python -m pip install <包名>
  - VS Code 命令面板搜不到 Python 命令 → 扩展未装在 WSL 侧（不影响终端运行，暂跳过）

## 2026-10-18（环境管理工具 + 环境机制实测）

- [AI] 下载 Miniconda（清华镜像 `miniconda.sh`，207MB）
- [AI] 首次安装踩坑：命令里的 `$HOME` 被 Windows 侧 PowerShell 抢先展开，装到畸形路径 `/home/jiuxiangz/C:UsersJiuXiangZ`
  - 症状：conda 报 `libmamba.so.4` 找不到、`.bashrc` 被写入错误路径、安装脚本退出码 2
  - 解决：删畸形目录 → 备份并删除 `.bashrc` 中错误的 conda init 块（备份 `~/.bashrc.bak.conda`）→ 改为写成 `.sh` 脚本、路径硬编码 `/home/jiuxiangz/miniconda3` 重装
- [AI] 重装结果：`PREFIX=/home/jiuxiangz/miniconda3`，无 libmamba 报错，`.bashrc` 中畸形路径 0 行
- [AI] 回归检查：老 venv 未受影响，`requests` 可导入
- [AI] 用 `wsl bash -lc 'conda --version'` 验证 → 报 `command not found`；改用脚本（内部 `bash -ic`）复验 → `conda 26.9.3`、`auto_activate_base -> False`
- [我] 新终端敲 `conda --version` → `conda 26.9.3`；`echo "CONDA_PREFIX=[$CONDA_PREFIX]"` → `CONDA_PREFIX=[]`（空，未自动激活 base）
- [我] 激活 / 退出 venv，观察提示符 `(.venv)` 与 `which python` 的对应：激活时指向 `~/wujie/.venv/bin/python`，`deactivate` 后 `which python` 无输出（系统只有 `python3`）
- [我] 实测 `-c` / `-lc` / `-ic` / `-lic` 四种组合下的 `type conda`：前两条报"文件路径"、后两条报"函数" → 说明只有 `-i` 会让 `.bashrc` 被读到底
- [我] 用 `env -i` 清空环境做对照，四条结果与预期一致（只有 `-i` 才有 conda 函数）
- [AI] 更新 `固定启动提示词.md`：第 7 节新增"记录必须区分谁在操作"一条，并同步到 `~/wujie`

## 2026-10-18（MineDojo 安装 + Minecraft 启动排障：把三层报错剥到根因）

- [AI] 创建 conda 环境 `minedojo`（Python 3.9）并安装 MineDojo 本体
- **第 1 层坑 · 依赖源已失效**
  - 症状：`Could not find com.github.SpongePowered:MixinGradle:dcfaf61`
  - 实测：该 commit 在 jitpack 的构建状态为 `Error`、POM 返回 404；旧脚本还依赖已于 2021 年关停的 `jcenter()`
  - 解决：[AI] 按官方未合并的 PR #137，给 `minedojo/sim/Malmo/Minecraft/build.gradle` 加 `repo.spongepowered.org` 仓库、坐标换成正式版 `org.spongepowered:mixingradle:0.6-SNAPSHOT`
  - 结果：构建通过（14m55s，27 个任务全绿）
- **第 2 层坑 · 游戏启动崩溃（报错与真因隔了三层）**
  - 症状：`OpenGL: ~~ERROR~~ RuntimeException: No OpenGL context found in the current thread.`；崩溃报告里 `Caused by: java.lang.ArrayIndexOutOfBoundsException: 0` @ `LinuxDisplay.getAvailableDisplayModes`
  - 判断一（只治了症状）：以为是 WSLg 给不了 GL → [我] 装 `xvfb` / `x11-utils` / `mesa-utils`；[AI] 预检 `glxinfo` 在 Xvfb 下正常（llvmpipe，OpenGL 4.5），但**报错一字未变**
  - 判断二（同样只治症状）：以为 Gradle daemon 缓存了旧环境 → [AI] 实测 daemon（PID 308121，19:02 启动）环境为 `DISPLAY=:0`；kill daemon 重跑后新 daemon 确为 `DISPLAY=:99` + `GALLIUM_DRIVER=llvmpipe`，但**报错仍完全相同**
  - 转折点：[AI] 写了 **40 秒最小 Java 探针**，直接调 LWJGL `Display.getAvailableDisplayModes()`，在三种 X 服务器（WSLg `:0`、手动 Xvfb `:99`、`xvfb-run` `:100`）下**全部返回空数组** → 证明与 X 服务器无关，并把 4 分钟一次的试错循环压成 40 秒
  - 根因（[Mojira MC-111217](https://bugs.mojang.com/browse/MC-111217)）：**LWJGL 2.9.4 是通过调用外部命令 `xrandr` 来枚举显示模式的**，不是调库函数；系统里没有 `xrandr` 时 `XRandR.process()` 失败 → 空数组 → 崩。与 DISPLAY、GLX、显卡均无关
  - 解决：[我] 安装 `x11-xserver-utils`（提供 `/usr/bin/xrandr`）
  - 复测（探针）：WSLg `:0` → **35 个模式**；Xvfb `:99` → 1 个（1024x768）→ 修复确认
- 环境新增依赖（均由 [我] 用 sudo apt 安装）：
  - **运行必需**：`xvfb`（虚拟显示器）、`x11-xserver-utils`（提供 `xrandr` 命令，本次真正的解药）
  - **排障工具（非运行必需）**：`x11-utils`（提供 `xdpyinfo`）、`mesa-utils`（提供 `glxinfo`）
- **结果 · 七步第②步完成（接上环境打印一次观测）**
  - 运行命令：`xvfb-run -a -s "-screen 0 1024x768x24" python minedojo_observe.py`
  - [AI] 20:28:08 启动 → 20:30:10 结束，耗时 2m02s（依赖与资源均已缓存），`observe exit=0`
  - 观测顶层 9 个字段：`rgb` shape=(3,160,256) uint8｜`inventory`｜`equipment`｜`life_stats`｜`location_stats`｜`nearby_tools`｜`damage_source`｜`masks`｜`delta_inv`
  - reset 首帧：`pos=[46.5, 71.0, 88.5]`，life=20 / food=20，光照等级 15，背包 36 格全空（全 `air`）
  - 连续 5 次「前进」动作：z 坐标 88.598 → 89.332 单调递增，reward 恒 0，done 恒 False
  - 产物：`frame_reset.png`(37719 B)、`frame_step5.png`(37918 B)
- 对比：第 1 次完整构建 14m55s → 修复后单次运行 2m02s（Gradle 依赖与 Minecraft 资源已缓存）

## 2026-10-18（收尾：Git 流程修正 + 记下一个想法）

- [我] Git 修正三步：
  - 提交 `2b6a7de` 后**忘记 push**（核对：本地领先远程 1 个提交）→ 补 push
  - `git add .` 误把 `logs/` 下 7 个运行日志提交进仓库 → `git rm -r --cached logs/` + `.gitignore` 增加 `logs/`（提交 `9542b7f`）
  - 核对结果：本地 = 远程 = `9542b7f`，工作区干净，`.env` 未被跟踪
- [AI] `LearningLog.md` 新增「Git 提交流程」与「MineDojo 打通（环境层知识）」两节
- **记下一个想法（未验证）**：环境观测字段目前固定 9 个。若后续某一步反复缺关键信息，可考虑「按任务需要扩充观测字段」（如把最近 N 步的状态变化、目标物的相对方位直接做成环境输出），以减少每步推理负担。属改环境配置的进阶内容，可行性待确认，当前不影响主线。
  - [AI] 已同步记入 README「探索方向 · 已记录的想法（2026-10-18）」
