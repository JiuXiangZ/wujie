import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()   # 从同目录的 .env 读取变量

BASE_URL = os.environ.get("DS_BASE_URL", "https://api.deepseek.com")
MODEL    = os.environ.get("DS_MODEL", "deepseek-chat")
API_KEY  = os.environ["DS_API_KEY"]

def call_llm(prompt, force_json=True):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "你是一个只输出 JSON 的助手。"},
            {"role": "user", "content": prompt},
        ],
    }
    if force_json:
        payload["response_format"] = {"type": "json_object"}
    r = requests.post(f"{BASE_URL}/chat/completions",
                      headers={"Authorization": f"Bearer {API_KEY}"},
                      json=payload, timeout=30)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

PROMPT = '以 JSON 输出一个 Minecraft 动作：字段 name 和 args，name 只能是 "move" 或 "jump"。'

text = call_llm(PROMPT)
print("模型原文：", text)
action = json.loads(text)
print("解析成功：", action)
print("动作名：", action["name"])