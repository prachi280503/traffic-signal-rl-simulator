from env.traffic_env import TrafficEnv
from agents.rl_agent import RLAgent
import matplotlib.pyplot as plt

env = TrafficEnv()
agent = RLAgent()

episodes = 300
episode_rewards = []

for ep in range(episodes):
    state = env.reset()
    total_reward = 0

    for _ in range(50):
        action = agent.get_action(state)
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state)
        state = next_state
        total_reward += reward

    episode_rewards.append(total_reward)
    print(f"Episode {ep+1} | Reward: {total_reward}")

plt.plot(episode_rewards)
plt.xlabel("Episodes")
plt.ylabel("Total Reward")
plt.title("RL Traffic Signal Learning")
plt.show()
