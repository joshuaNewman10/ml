from abc import abstractmethod


class Agent:
    def __init__(self):
        self.reset_reward()

    def initialize(self):
        self.reset()

    @abstractmethod
    def get_action(self, action, current_observation, previous_observation, reward, done, info):
        raise NotImplementedError

    def update_reward(self, reward, done):
        self.total_reward += reward

    def reset(self):
        self.reset_reward()

    def reset_reward(self):
        self.total_reward = 0
