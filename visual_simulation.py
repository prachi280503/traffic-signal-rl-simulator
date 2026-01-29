import matplotlib.pyplot as plt
import matplotlib.animation as animation
from env.traffic_env import TrafficEnv
from agents.rl_agent import RLAgent

env = TrafficEnv()
agent = RLAgent()

# Load a trained-like behavior (quick warmup)
for _ in range(100):
    state = env.reset()
    for _ in range(20):
        action = agent.get_action(state)
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state)
        state = next_state

state = env.reset()

# Plot setup
fig, ax = plt.subplots()
lanes = ["North", "South", "East", "West"]
bars = ax.bar(lanes, state[:4], color="red")

ax.set_ylim(0, 30)
ax.set_ylabel("Number of Vehicles")
ax.set_title("RL-Based Traffic Signal Simulator")

signal_text = ax.text(0.5, 25, "", ha="center", fontsize=12)

def update(frame):
    global state
    action = agent.get_action(state)
    state, reward, done = env.step(action)

    for bar, q in zip(bars, state[:4]):
        bar.set_height(q)

    if action == 0:
        bars[0].set_color("green")
        bars[1].set_color("green")
        bars[2].set_color("red")
        bars[3].set_color("red")
        signal_text.set_text("Signal: North-South GREEN")
    else:
        bars[0].set_color("red")
        bars[1].set_color("red")
        bars[2].set_color("green")
        bars[3].set_color("green")
        signal_text.set_text("Signal: East-West GREEN")

    return bars

ani = animation.FuncAnimation(fig, update, frames=200, interval=500)
plt.show()
