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