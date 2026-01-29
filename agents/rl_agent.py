import numpy as np
import random

class RLAgent:
    def __init__(self):
        self.q_table = {}
        self.lr = 0.1
        self.gamma = 0.9
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01

    def get_action(self, state):
        state = tuple(state)
        if random.random() < self.epsilon:
            return random.choice([0, 1])
        return np.argmax(self.q_table.get(state, [0, 0]))

    def learn(self, state, action, reward, next_state):
        state = tuple(state)
        next_state = tuple(next_state)

        if state not in self.q_table:
            self.q_table[state] = [0, 0]
        if next_state not in self.q_table:
            self.q_table[next_state] = [0, 0]

        best_next = max(self.q_table[next_state])
        self.q_table[state][action] += self.lr * (
            reward + self.gamma * best_next - self.q_table[state][action]
        )

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
