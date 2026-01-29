import matplotlib.pyplot as plt
import matplotlib.animation as animation
from env.traffic_env import TrafficEnv
from agents.rl_agent import RLAgent
import numpy as np

env = TrafficEnv()

# RL agents for two intersections
agent1 = RLAgent()
agent2 = RLAgent()

state = env.reset()

# Fixed queues (copy for fair comparison)
fixed_queues = {
    "I1": state["I1"][:4].copy(),
    "I2": state["I2"][:4].copy()
}

# Figure layout (2x2)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
titles = [
    "RL – Intersection 1", "Fixed – Intersection 1",
    "RL – Intersection 2", "Fixed – Intersection 2"
]

bars = []
texts = []

for ax, title in zip(axs.flatten(), titles):
    ax.set_ylim(0, 30)
    ax.set_title(title)
    b = ax.bar(["N","S","E","W"], [0,0,0,0], color="red")
    bars.append(b)
    texts.append(ax.text(0.5, 25, "", ha="center"))

def update(frame):
    global state, fixed_queues

    # RL actions
    a1 = agent1.get_action(state["I1"])
    a2 = agent2.get_action(state["I2"])

    next_state, rewards = env.step({"I1": a1, "I2": a2})

    agent1.learn(state["I1"], a1, rewards["I1"], next_state["I1"])
    agent2.learn(state["I2"], a2, rewards["I2"], next_state["I2"])

    # FIXED signal (always NS)
    for key in ["I1", "I2"]:
        fixed_queues[key] += np.random.randint(0, 3, size=4)
        fixed_queues[key][0] = max(0, fixed_queues[key][0] - 3)
        fixed_queues[key][1] = max(0, fixed_queues[key][1] - 3)

    # Update RL bars
    for i, key in enumerate(["I1", "I2"]):
        for bar, q in zip(bars[i*2], next_state[key][:4]):
            bar.set_height(q)
        texts[i*2].set_text(f"Reward: {rewards[key]}")

    # Update Fixed bars
    for i, key in enumerate(["I1", "I2"]):
        for bar, q in zip(bars[i*2+1], fixed_queues[key]):
            bar.set_height(q)
        texts[i*2+1].set_text(f"Waiting: {sum(fixed_queues[key])}")

    state = next_state

ani = animation.FuncAnimation(
    fig,
    update,
    frames=120,
    interval=600,
    cache_frame_data=False
)

ani.save(
    "traffic_rl_vs_fixed.gif",
    writer="pillow",
    fps=2
)

print("GIF saved as traffic_rl_vs_fixed.gif")
plt.show()
