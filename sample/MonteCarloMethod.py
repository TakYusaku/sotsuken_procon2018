# learning agent by Monte Carlo method

import gym
import requests
import numpy as np
import csv
import matplotlib.pyplot as pl
from collections import deque
import time
import threading
#import # 敵のデータ

def getAction(env, q_table, observation, episode,type): # get action (array)  # フィールド外は再計算
    #epsilon = 0.5 * (1 / (episode + 1))
    obs = env.getStatus(observation)
    epsilon = 0.5
    a = []
    b = False

    for i in range(2):
        if np.random.uniform(0, 1) > epsilon:  # e-greedy low is off
            x = np.argsort(q_table[obs[i]])[::-1]
            b = False
            c = 0
            while b!=True:
                b, d, ms, next_pos = env.judAc(i+3, x[c], observation[i])
                if type == "nb":
                    lv = env.show()
                    try:
                        if lv[next_pos[0],next_pos[1]] == 6 or lv[next_pos[0],next_pos[1]] == 3 or lv[next_pos[0],next_pos[1]] == 4:
                            c += 1
                            b = False
                        else:
                            c += 1
                    except:
                        c += 1
                else:
                    b = True
            a.append([d, ms, next_pos])

        else: # e-greedy low is on
            b = False
            while b!=True:
                pa = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
                b, d, ms, next_pos = env.judAc(i+3, pa, observation[i])
                if type != "nb":
                    b = True
            a.append([d, ms, next_pos])

    return a  # [[int(direction), str(movement), list(next position)],[]]
"""
def getAction(env, q_table, observation, episode,choice): # get action (array)  # フィールド外は罰金
    #epsilon = 0.5 * (1 / (episode + 1))
    epsilon = 0.5
    a = []
    b = False
    n = 2
    if choice == 0:
        n = 2
    elif choice == 1:
        n = 0

    for i in range(2):
        if np.random.uniform(0, 1) > epsilon:  # e-greedy low is off
            x = np.argsort(q_table[observation[i]])[::-1]
            b, d, ms, next_pos = env.judAc(i+1+n, x[0])
            a.append([d, ms, next_pos])

        else: # e-greedy low is on
            pa = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            b, d, ms, next_pos = env.judAc(i+1+n, pa)
            a.append([d, ms, next_pos])
    return a  # [[int(direction), str(movement), list(next position)],[]]
"""

# [] update Qtables
def updateQtable(q_table, memory):#observation, action, reward, next_observation):
    gamma = 0.99 # time discount rate
    alpha = 0.1 # learning rate
    total_reward_t = 0
    while (memory.len() > 0):
        (state, action, reward) = memory.sample()
        total_reward_t = gamma * total_reward_t       # 時間割引率をかける
        # Q関数を更新
        q_table[state, action[0]] = q_table[state, action[0]] + alpha*(reward+total_reward_t-q_table[state, action[0]])
        total_reward_t = total_reward_t + reward    # ステップtより先でもらえた報酬の合計を更新

    return q_table


class Memory:
    def __init__(self, max_size):
        self.buffer = deque(maxlen=max_size)

    def add(self, experience):
        self.buffer.append(experience)

    def sample(self):
        return self.buffer.pop()

    def len(self):
        return len(self.buffer)
