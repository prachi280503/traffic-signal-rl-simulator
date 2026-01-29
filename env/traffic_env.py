import numpy as np

class TrafficEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        # Two intersections, each with 4 lanes
        self.queues = {
            "I1": np.random.randint(5, 15, size=4),
            "I2": np.random.randint(5, 15, size=4)
        }
        self.phases = {"I1": 0, "I2": 0}
        return self.get_state()

    def step(self, actions):
        rewards = {}

        for key in ["I1", "I2"]:
            action = actions[key]
            self.phases[key] = action

            # vehicle arrivals
            arrivals = np.random.randint(0, 3, size=4)
            self.queues[key] += arrivals

            # vehicle departures
            if action == 0:  # NS green
                self.queues[key][0] = max(0, self.queues[key][0] - 3)
                self.queues[key][1] = max(0, self.queues[key][1] - 3)
            else:  # EW green
                self.queues[key][2] = max(0, self.queues[key][2] - 3)
                self.queues[key][3] = max(0, self.queues[key][3] - 3)

            rewards[key] = -np.sum(self.queues[key])

        return self.get_state(), rewards

    def get_state(self):
        avg_I1 = np.mean(self.queues["I1"])
        avg_I2 = np.mean(self.queues["I2"])

        return {
            "I1": np.append(self.queues["I1"], [self.phases["I1"], avg_I2]),
            "I2": np.append(self.queues["I2"], [self.phases["I2"], avg_I1])
        }
