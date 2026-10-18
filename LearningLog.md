# Learning Log

> 用途：**自己的学习笔记**（术语、命令、踩坑）。过程与实验数据记在 `DailyProgress.md`。

## 2026-10-16

### Goals

- [x] Goal 1 · install WSL2 + Ubuntu + python
- [x] Goal 2 · activate python venv
- [x] Goal 3 · run requests → JSON

### Where I place / what I name

- Workspace: ~/wujie
- home directory: /home/jiuxiangz

### What I learned

1. VS Code 左下角 "><" 可切换 "WSL: Ubuntu" 与 Windows 本地
2. PowerShell（右键 Windows 底部 → 管理员终端）
3. ctrl+shift+C/V 在 Linux 终端里复制/粘贴
4. venv = virtual environment（虚拟环境）
5. . = 隐藏文件/文件夹
6. ~ = 家目录
7. bin = 存放可执行命令的目录
8. source = 在当前 shell 里运行脚本
9. script = n 条命令的集合
10. source .venv/bin/activate 或 .venv/bin/python（激活后命令提示符前出现 (.venv) 标记）
11. pip = 安装第三方库的命令
12. pip install requests // 安装 requests 库
13. python probe.py // 用 python 解释器运行 probe.py

### Issues & Fixes

- Problem: 新开终端后装库报 `externally-managed-environment`
- Cause: 没有激活 venv，pip 落到了系统 Python 上（Ubuntu 禁止直接写入系统 Python）
- Solution: 先 `cd ~/wujie && source .venv/bin/activate`，再用 `python -m pip install <包名>`

### Takeaways

- ctrl+shift+C/V 在 Linux 终端里复制/粘贴
- 路径写法：Windows 用 "\"，Linux 用 "/"
- 新开终端 = 先激活 venv（两步：cd ~/wujie + source .venv/bin/activate）

## 2026-10-17

### Goals

- [x] Goal 1 · 调通 LLM API，拿到能被 json.loads() 解析的动作 JSON（七步第①步）
- [x] Goal 2 · 做一次「带 / 不带 response_format」的对比实验
- [x] Goal 3 · 整理三份文档（README 骨架 / 实验记录 / 本笔记）

### Where I place / what I name

- 代码：`call_llm.py`（调模型拿动作 JSON）、`compare_json.py`（对比实验）、`probe.py`（requests→JSON 探针）
- 配置：`.env`（存 DS_API_KEY，已被 .gitignore 忽略，不进仓库）
- 文档：`README.md`（交付物，精简）、`DailyProgress.md`（实验记录）、`LearningLog.md`（本笔记）

### What I learned

1. OpenAI 兼容接口：换厂商 / 换模型改 —— base_url、api_key、model
2. .env + load_dotenv()：把 key 和代码分开，代码可以公开，key 留在本地
3. response_format = {"type": "json_object"}：在 API 层强制模型输出 JSON
4. json.loads(text)：把模型输出的「文本」变成 Python 字典，Agent 才能直接取用
5. 解析成功率 = N 次调用中能解析成功的次数占比，衡量的是「稳定」，不是「某次成功」
6. Agent 主循环要跑几百步，每一步都解析一次 → 稳定性差会拖垮整体表现
7. `python -m pip install <包名>`：用「当前这个 python」的 pip 装包，避免装错环境
8. Error：externally-managed-environment 忘进 venv
9. `git status --short`：提交前先看哪些文件会上去（`.env` 绝不能出现）
10. 文档分工：README 给评委（精简 + 证据），DailyProgress 给自己（只增不删，答辩问答靠它）
11. 样本太小只能「观察」不能「下结论」（5 次 vs 5 次说明不了差别）

### Issues & Fixes

- Problem: 跑 `call_llm.py` 报 `ModuleNotFoundError: No module named 'dotenv'`
- Cause: 装库时没激活 venv，pip 装进了系统 Python，而脚本用的是 venv 里的 Python
- Solution: 激活 venv 后重装 `python -m pip install python-dotenv`，并用 `python -c "from dotenv import load_dotenv; print('ok')"` 验证

- Problem: VS Code 命令面板搜不到 `Python: Select Interpreter`
- Cause: Python 扩展没装在 WSL 侧（Remote-WSL 不会自动继承 Windows 侧的扩展）
- Solution: 暂时跳过 —— 终端里跑脚本不受影响；要补就在扩展面板点 "Install in WSL: Ubuntu"

### Takeaways

- 新终端第一件事：`cd ~/wujie && source .venv/bin/activate`
- 装库只认 `python -m pip install`
- 记实验一定要带数字（5/5 比「跑通了」有说服力）

## 2026-10-18

### Goals

- [x] Goal 1 · 安装 Miniconda（清掉一次畸形安装后重装并验证）
- [x] Goal 2 · 搞清 venv 与 conda 的分工、以及"激活"的机制
- [x] Goal 3 · 实测 `bash` 的 `-c` / `-l` / `-i` 三个开关对 `.bashrc` 的影响

### Where I place / what I name

- Miniconda 安装位置：`/home/jiuxiangz/miniconda3`
- 启动配置：`~/.bashrc` 末尾的 conda init 块（备份：`~/.bashrc.bak.conda`）
- 两套环境：`~/wujie/.venv`（跑 `call_llm.py`）｜ `/home/jiuxiangz/miniconda3`（后面装 MineDojo）
- 临时脚本：`/mnt/e/tmp/`（[AI] 为本次安装所写，属一次性工具，不进仓库）

### What I learned

1. conda 是「包管理器 + 环境管理器」；Miniconda 是它的精简发行版（Anaconda = conda + 几百个预装库的巨型版）
2. venv 只能给系统已有的 Python 建隔离外壳（换不了 Python 版本、装不了非 Python 依赖）；conda 能指定 Python 版本、还能装 JDK 等二进制依赖 → MineDojo 需要后者
3. `PATH` 是一串目录清单，敲命令时按顺序查找、命中第一个：conda init 把 `miniconda3/condabin` 加进 `PATH`（在交互式 shell 里生效），所以 `conda` 命令不用激活就能用；venv 靠 activate 把自己的 `bin` 临时插到最前面
4. 激活 = 改 `PATH` + 改提示符 `PS1`；`(.venv)` 只是"信号"，判断在哪个环境要看 `which python`
5. `PS1` 里 `\[ \]` = 不占屏幕宽度的非打印区；`\u \h \w \$` = 用户名/主机名/当前目录/提示符；`\033[01;32m` 这类是 ANSI 颜色码
6. Ubuntu 系统里只有 `python3`，没有 `python`（`python` 这个名字要靠 venv / conda 环境提供）
7. Windows 侧会先"解析"一遍再传给 WSL：双引号内的 `$HOME` 会被 PowerShell 替换成 `C:\Users\...`（单引号不展开；最稳的是写成 `.sh` 文件）
8. `bash` 的三个启动开关是三个独立维度：`-c` 管"跑我给你的文本、跑完就退出"；`-i` 管"装成交互式 shell"；`-l` 管"装成登录 shell、额外读 `~/.profile`"
9. `.bashrc` 是边读边执行的（读一行、执行一行）。它开头的 `case $- in *i*) ;; *) return;; esac` 是门卫：`$-` 是当前 shell 的开关字母串，交互式时含 `i` → 含 `i` 就继续往下读，不含就执行 `return`（`return` = 停止执行当前被读入的文件，回到读它的地方）→ 所以非交互时第 4 行就收工，末尾的 conda init 完全没被读到
10. `-l` 会让 bash 读 `~/.profile`，而 `.profile` 里有 `. "$HOME/.bashrc"` 那行 → 这正是 `-lc` 能"碰到 `.bashrc` 却读不完"的原因；决定成败的字母是 `i`，不是 `l`
11. 环境变量（`PATH`）会被子进程继承，shell 函数不会继承 → 所以 `type conda` 报"文件路径"还是"函数"才是判据：报"函数"说明 conda init 真的执行过；报"文件"只说明 `PATH` 里有它。要排除继承干扰，用 `env -i` 清空环境再测

### Issues & Fixes

- Problem: Miniconda 装到畸形路径 `/home/jiuxiangz/C:UsersJiuXiangZ`，conda 报 `libmamba.so.4` 找不到（[AI] 代跑安装时踩到）
- Cause: 命令用双引号包裹后，PowerShell 抢先展开 `$HOME` → 传进 Linux 的是 `C:\Users\JiuXiangZ/...`，反斜杠在 Linux 里被当普通字符
- Solution: 删畸形目录 → 备份后用 `sed` 整段删除 `.bashrc` 里错误的 conda init 块 → 把安装命令写成 `.sh` 文件、路径硬编码 `/home/jiuxiangz/miniconda3` 重装

- Problem: [AI] 用 `bash -lc 'conda --version'` 验证时报 `command not found`，一度误判为安装失败
- Cause: `.bashrc` 开头的门卫对非交互 shell 直接 `return`（第 4 行收工），conda init 没被执行；`-l` 让 `.profile` 读到了 `.bashrc`，但门卫把它挡在开头
- Solution: 改用交互式 `bash -ic` 复验 → `conda 26.9.3` 正常。结论：`-i` 才是关键，`-l` 只影响是否多读 login 那层文件

- Problem: [我] 执行 `deactivate` 后，`which python` 没有任何输出
- Cause: 正常现象 —— Ubuntu 只提供 `python3`，系统里没有 `python` 这个名字
- Solution: 无需处理；要看系统 Python 用 `which python3`

- Problem: [我] 四条 `type conda` 的结果和预期不一样（本以为 `-c` / `-lc` 会"找不到"，实际都找到了）
- Cause: `PATH` 被子进程继承 —— 交互式终端启动时 conda init 已把 `condabin` 加进 `PATH`，子 shell 一出生就带着它；而 shell 函数不继承
- Solution: 用 `env -i HOME="$HOME" PATH=/usr/bin:/bin bash -ic 'type conda'` 清空环境复测，才看清"函数 vs 文件"的差别

### Takeaways

- 从 Windows 侧给 WSL 传命令：能用单引号就别用双引号；带变量或反斜杠的一律写成 `.sh` 文件执行
- 判断"在不在某个环境"，永远看 `which python` / `which python3`，不看提示符（激活真正改变的只有 `PATH`）
- 一个终端只激活一个环境：跑 `call_llm.py` 用 venv，跑 MineDojo 用 conda 环境
- 装新工具后必做"回归检查"：确认旧工具（老 venv）没被弄坏
- 排查"明明配好了却不生效"时，先怀疑"我是不是在非交互 shell 里跑的"（脚本、自动化、`-c` 场景都属非交互）
- "同一命令在 A 处能跑、B 处不能跑" → 先比两处的父进程环境（`PATH` / 环境变量），再怀疑代码