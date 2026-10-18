"""七步第②步：接上 MineDojo 环境，打印一次真实观测。

运行方式（必须先激活 conda 环境）：
    conda activate minedojo
    cd ~/wujie
    python minedojo_observe.py

验收：能拿到非空的状态字典，且能说清每个字段是什么。
"""

import minedojo


def describe(d, indent=0):
    """逐层打印观测字典的结构（不猜字段名，有什么打什么）。"""
    pad = "  " * indent
    for k, v in d.items():
        if isinstance(v, dict):
            print(f"{pad}{k}: <dict>")
            describe(v, indent + 1)
        else:
            shape = getattr(v, "shape", None)
            if shape is not None:
                print(f"{pad}{k}: shape={shape}, dtype={getattr(v, 'dtype', '?')}")
            else:
                text = str(v)
                if len(text) > 100:
                    text = text[:100] + "..."
                print(f"{pad}{k}: {text}")


def save_frame(rgb, path):
    """把一张 RGB 观测存成 PNG，方便肉眼确认画面真的出来了。"""
    try:
        from PIL import Image
        img = Image.fromarray(rgb.transpose(1, 2, 0))
        img.save(path)
        print(f"已保存画面：{path}")
    except Exception as e:  # 存不下来不影响主流程
        print(f"画面保存失败（不影响观测）：{e}")


def main():
    print("=== 1. 创建 open-ended 环境 ===")
    env = minedojo.make(task_id="open-ended", image_size=(160, 256))
    print("env 类型:", type(env).__name__)
    print("task_prompt:", getattr(env, "task_prompt", "(无)"))

    print("=== 2. reset：拿第一次观测 ===")
    obs = env.reset()
    print("obs 类型:", type(obs))
    print("顶层字段:", list(obs.keys()))
    describe(obs)

    if "rgb" in obs:
        save_frame(obs["rgb"], "frame_reset.png")

    print("=== 3. 背包与自身状态 ===")
    print("inventory:", obs.get("inventory"))
    print("location_stats:", obs.get("location_stats"))
    print("life_stats:", obs.get("life_stats"))

    print("=== 4. 走 5 步（动作=前进），每步看 reward / done / 新位置 ===")
    for i in range(5):
        act = env.action_space.no_op()
        act[0] = 1  # 0=不动 1=前进 2=后退
        obs, reward, done, info = env.step(act)
        loc = obs.get("location_stats", {}).get("pos")
        pos = loc.tolist() if hasattr(loc, "tolist") else loc
        print(f"step {i + 1}: pos={pos} reward={reward} done={done}")

    if "rgb" in obs:
        save_frame(obs["rgb"], "frame_step5.png")

    env.close()
    print("=== 演示结束 ===")


if __name__ == "__main__":
    main()
