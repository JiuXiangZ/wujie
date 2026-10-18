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
