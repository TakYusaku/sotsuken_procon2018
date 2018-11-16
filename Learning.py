import gym
import requests
import numpy as np
import csv
import matplotlib.pyplot as plt
from collections import deque
import time
import threading
import datetime
##### library
import Learning_Method.Q_Learning as Q
import Learning_Method.MonteCarloMethod as M
import tools.tools as ts
#import linenotify
import sys


# [] main processing
if __name__ == '__main__':
    info = ts.readLParam('li.csv')
    env = gym.make('procon18env_re-v0')
    num_episode = int(info[1])
    Win1 = 0
    Win2 = 0

    # read q tables from csv file
    q_table = ts.readQtable(info[8])
    q_table_Enemy = ts.readQtable(info[9])
    type_f = info[6]
    type_e = info[7]
    f_rr = [] # 味方の各エピソードの報酬
    e_rr = [] # 敵の各エピソードの報酬
    f_r = []
    e_r = []
    s1 = []
    s2 = []
    s3 = []
    s4 = []
    s5 = []
    s6 = []

    try:
        for episode in range(num_episode):
            observation,init_pos_info = env.reset(int(info[0]))
            order = init_pos_info[0]
            pattern = init_pos_info[1]
            friends = [order[0],order[1]]
            enemies = [order[2],order[3]]
            terns = env.terns
            total_reward_f = 0
            total_reward_e = 0
            memory1 = M.Memory(terns)
            memory2 = M.Memory(terns)

            for i in range(terns):
                env.countStep()
                ob_f = env.getStatus(observation[0])
                ob_e = env.getStatus(observation[1])

                action_f = Q.getAction(env, q_table, ob_f, episode, friends, type_f) # array
                action_e = M.getAction(env, q_table_Enemy, ob_e, episode, enemies, type_e)

                for i in range(2):
                    if action_f[i][2] == action_e[i][2]: # 移動先が被ったら停留
                        action_f[i][1] == "stay"
                        action_e[i][1] == "stay"

                # process (friend_q)
                next_observation_f, reward_f, done = env.step(action_f,terns,0)
                q_table = Q.updateQtable(env, q_table, observation[0], action_f, reward_f, next_observation_f)
                # process (enemy_mcm)
                next_observation_e, reward_e, done = env.step(action_e,terns,2)
                memory1.add((ob_e[0], action_e[0], reward_e[0]))
                memory2.add((ob_e[1], action_e[1], reward_e[1]))

                total_reward_f += (reward_f[0] + reward_f[1])
                total_reward_e += (reward_e[0] + reward_e[1])
                observation = [next_observation_f,next_observation_e]

                if terns - 1 == i:
                    # update q_table_Enemy
                    q_table_Enemy = M.updateQtable(q_table_Enemy, memory1)
                    q_table_Enemy = M.updateQtable(q_table_Enemy, memory2)
                    break
            f_rr.append(total_reward_f)
            e_rr.append(total_reward_e)
            s = env.calcPoint()
            s1.append(s[0])
            s2.append(s[1])
            s3.append(s[2])
            s4.append(s[3])
            s5.append(s[4])
            s6.append(s[5])
            if env.judVoL() == "Win_1":
                f_r.append(1)
                e_r.append(-1)
                Win1 += 1
                print('Win1')
            else:
                f_r.append(-1)
                e_r.append(1)
                Win2 += 1
                print('Win2')

            if episode%500 == 0 and episode!=num_episode-1 :
                #saveImage()
                now = datetime.datetime.now()
                m = "epoch is " + str(episode) + " now.\n" + "Win1 is " + str(Win1) + "\n" + "Win2 is " + str(Win2) + "\n" + "now time is " + str(now) + '\n'
            #Log(m,fm)

        ts.writeQtable(info[8], q_table)
        ts.writeQtable(info[9], q_table_Enemy)
        print("How many times did QL win?")
        print(Win1)
        print("How many times did MCM win?")
        print(Win2)
        m = "How many times did QL win?" + str(Win1) + "\n"
        #Log(m,fm)
        m = "How many times did MCM win?" + str(Win2) + "\n"
        #Log(m,fm)

        #saveImage()
        #notify(num_episode,Win1,Win2,s3,s6)
        #notify(num_episode,Win1,Win2,s1,s2,s3,s4,s5,s6)
        now = datetime.datetime.now()
        m = "finished time is " + str(now)
        print(m)
        #Log(m,fm)
        #linenotify.main_m(m)

    except:
        m = str(sys.exc_info())
        print(m)
        #linenotify.main_m(m)
        ts.writeQtable(info[8], q_table)
        ts.writeQtable(info[9], q_table_Enemy)
        #saveImage()
        m = "How many times did QL win?" + str(Win1) + "\n"
        #Log(m,fm)
        m = "How many times did MCM win?" + str(Win2) + "\n"
        #Log(m,fm)
        #notify(num_episode,Win1,Win2,s3,s6)
        #notify(num_episode,Win1,Win2,s1,s2,s3,s4,s5,s6)
        now = datetime.datetime.now()
        m = "(error)finished time is " + str(now)
        #Log(m,fm)
        #linenotify.main_m(m)
