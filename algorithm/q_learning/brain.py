"""version:
pandas = 1.0.1
numpy = 1.18.1
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class QLearningTable:
    """RL brain, Value function with qTable"""
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

    def choose_action(self, observation):
        self.check_state_exist(observation)
        # action selection
        if np.random.uniform() < self.epsilon:
            # choose best action
            state_action = self.q_table.loc[observation, :]
            # some actions may have the same value, randomly choose on in these actions
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)
        else:
            # choose random action
            action = np.random.choice(self.actions)
        return action

    def learn(self, s, a, r, s_):
        """ implementation of the bellman equation"""

        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, :].max() 
        else:
            q_target = r 
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)  # update


    def check_state_exist(self, state):
        """check if following state exists"""

        if state not in self.q_table.index:
            # append new state to q table
            self.q_table = self.q_table.append(
                pd.Series(
                    [0]*len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )

    
    def plot_total_reward(self, total_reward_list):
        plt.plot(np.arange(len(total_reward_list)), total_reward_list)
        plt.ylabel('Total Reward')
        plt.xlabel('Episodes')
        plt.show()
        #print(total_reward_list, len(total_reward_list))
    
