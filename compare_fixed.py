from env.traffic_env import TrafficEnv

env = TrafficEnv()
state = env.reset()

total_wait = 0

for _ in range(100):
    action = 0  # Always NS green
    state, reward, done = env.step(action)
    total_wait += -reward

print("Total Waiting Time (Fixed Signal):", total_wait)
