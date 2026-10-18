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
