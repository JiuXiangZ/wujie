import json
import requests

# 向一个公开接口发请求，拿到「模型回复」的同类东西
resp = requests.get("https://api.github.com/repos/microsoft/WSL", timeout=15)
print("状态码:", resp.status_code)

# 把返回文本解析成 Python 字典 —— 这就是处理模型输出的核心动作
data = resp.json()
print("类型:", type(data))
print("仓库名:", data["full_name"])
print("star 数:", data["stargazers_count"])