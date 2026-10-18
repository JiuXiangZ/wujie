import os, json, requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.environ.get("DS_BASE_URL", "https://api.deepseek.com")
MODEL    = os.environ.get("DS_MODEL", "deepseek-chat")
API_KEY  = os.environ["DS_API_KEY"]

PROMPT = '以 JSON 输出一个 Minecraft 动作：字段 name 和 args，name 只能是 "move" 或 "jump"。'

def run(force_json):
    payload = {"model": MODEL,
               "messages": [{"role": "system", "content": "你是一个只输出 JSON 的助手。"},
                            {"role": "user", "content": PROMPT}]}
    if force_json:
        payload["response_format"] = {"type": "json_object"}
    r = requests.post(f"{BASE_URL}/chat/completions",
                      headers={"Authorization": f"Bearer {API_KEY}"},
                      json=payload, timeout=30)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

for name, flag in [("带 response_format", True), ("不带", False)]:
    ok = 0
    for i in range(5):
        text = run(flag)
        try:
            json.loads(text); ok += 1
        except Exception:
            print(f"  第{i+1}次解析失败：{text[:60]}")
    print(f"{name}：解析成功 {ok}/5")