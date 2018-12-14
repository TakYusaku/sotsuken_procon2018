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
import traceback


# [] main processing
if __name__ == '__main__':
    # ハイパーパラメータの参照
    hypala_name = sys.argv[1]
    hypala = './hyperpalam_list/' + hypala_name
    info = ts.readLParam(hypala)
    # 開始時間の記録
    fm,le_start = ts.getTime("filename")
    ts.init_func(fm)
    ts.Log(fm, "start")
    # 学習パラメータ等の記録
    ts.Log(fm, "info",info)
    # 学習プラットフォームの選択
    env = gym.make('procon18env_re-v0')
    # 学習回数
    num_episode = int(info[1])
    # 学習率 _q is q learning, _m is mcm
    al_q = info[4]
    al_m = info[5]
    # 勝利数 win1 is ql , win2 is mcm
    Win1 = 0
    Win2 = 0

    # read q tables from csv file
    q_table = ts.readQtable(info[8])
    q_table_Enemy = ts.readQtable(info[9])
    # 学習タイプの選択
    type_f = info[6]
    type_e = info[7]
    f_rr = [] # 味方の各エピソードの報酬
    e_rr = [] # 敵の各エピソードの報酬
    s = [[],[],[],[],[],[]] #[[friend_tile],[friend_field],[friend_total],[enemy_tile],[enemy_field],[enemy_total]] 獲得ポイント
    epi_processtime = []
    kari_epi = 0

    try:
        for episode in range(num_episode):
            kari_epi += 1
            observation = env.reset(int(info[0]))
            terns = env.terns
            total_reward_f = 0
            total_reward_e = 0
            memory1 = M.Memory(terns)
            memory2 = M.Memory(terns)

            fs,epi_starttime = ts.getTime("timestamp_s")
            m = "epoch : " + str(episode+1) + " / " + str(num_episode)
            print(m)

            """
            if episode == 6:
                raise Exception
            """

            for i in range(terns):
                env.countStep() # epoch num のカウント
                # 状態の取得
                ob_f = env.getStatus(observation[0])
                ob_e = env.getStatus(observation[1])
                # 行動の取得
                action_f = Q.getAction(env, q_table, observation[0], episode,type_f) # array
                action_e = M.getAction(env, q_table_Enemy, observation[1], episode, type_e)

                for i in range(2):
                    if action_f[i][2] == action_e[i][2]: # 移動先が被ったら停留
                        action_f[i][1] = 'stay'
                        action_e[i][1] = 'stay'

                # process (friend_q)
                next_observation_f, reward_f = env.step(action_f,terns,0) # 行動の実行
                q_table = Q.updateQtable(env, q_table, observation[0], action_f, reward_f, next_observation_f,al_q) # Qテーブルの更新
                # process (enemy_mcm)
                next_observation_e, reward_e = env.step(action_e,terns,2) # 行動の実行
                memory1.add((ob_e[0], action_e[0], reward_e[0]))
                memory2.add((ob_e[1], action_e[1], reward_e[1]))

                # 報酬の記録
                total_reward_f += (reward_f[0] + reward_f[1]) / 2
                total_reward_e += (reward_e[0] + reward_e[1]) / 2
                observation = [next_observation_f,next_observation_e]

                if env.terns == env.now_terns:
                    # update q_table_Enemy
                    q_table_Enemy = M.updateQtable(q_table_Enemy, memory1,al_m)
                    q_table_Enemy = M.updateQtable(q_table_Enemy, memory2,al_m)
                    break

            epi_time_delta,fs,now = ts.getTime("timestamp_on",epi_starttime) # 1epoch 実行時間
            epi_processtime.append(epi_time_delta) # 実行時間の記録
            # 1 epoch の報酬の記録
            f_rr.append(total_reward_f)
            e_rr.append(total_reward_e)
            # 1ゲームのポイントの記録
            s_p = env.calcPoint()
            s[0].append(s_p[0])
            s[1].append(s_p[1])
            s[2].append(s_p[2])
            s[3].append(s_p[3])
            s[4].append(s_p[4])
            s[5].append(s_p[5])
            if env.judVoL() == "Win_1":
                Win1 += 1
                print('agent1 won')
            else:
                Win2 += 1
                print('agent2 won')

            if episode != 0 and episode%2 == 0 and episode!=num_episode-1 :
                ts.writeQtable(fm, info[8], q_table, episode)
                ts.writeQtable(fm ,info[9], q_table_Enemy, episode)
                info_epoch = [epi_processtime[episode],float(Win1/episode),float(Win2/episode),float(sum(f_rr)/episode),float(sum(e_rr)/episode)]
                ts.Log(fm,"now learning",info_epoch,episode)
                ts.saveImage(fm,s,f_rr,e_rr,episode)

        # 学習終了後の後処理
        le_delta,fs,now = ts.getTime("timestamp_on",le_start) # 総実行時間の記録
        ts.writeQtable(fm,info[8], q_table, num_episode)
        ts.writeQtable(fm,info[9], q_table_Enemy, num_episode)
        print("How many times did QL win, and What is WPCT of QL ?")
        w1 = str(Win1) + " , " + str(float(Win1/num_episode))
        print(w1)
        print("How many times did MCM win, and What is WPCT of MCM ?")
        w2 = str(Win2) + " , " + str(float(Win2/num_episode))
        print(w2)
        m = "finished time is " + str(now)
        print(m)

        info_finished = [Win1,Win2,float(Win1/num_episode),float(Win2/num_episode),float(sum(f_rr)/num_episode),float(sum(e_rr)/num_episode),fs,le_delta]
        ts.Log(fm,"finished",info_finished)
        ts.saveImage(fm,s,f_rr,e_rr,num_episode)
    except:
        m = str(sys.exc_info())
        le_delta,fs,now = ts.getTime("timestamp_on",le_start) # 総実行時間の記録
        info_error = [Win1,Win2,float(Win1/num_episode),float(Win2/num_episode),float(sum(f_rr)/kari_epi),float(sum(e_rr)/kari_epi),fs,le_delta,m]
        ts.Log(fm,"error",info_error)
        print(m)
        ###
        fn = './log/' + fm + '/text_log/error.log'
        with open(fn, 'a') as f:
            traceback.print_exc(file=f)
        ###
        ts.writeQtable(fm, info[8],q_table,kari_epi)
        ts.writeQtable(fm, info[9],q_table_Enemy,kari_epi)
        print("How many times did QL win, and What is WPCT of QL ?")
        w1 = str(Win1) + " , " + str(float(Win1/kari_epi))
        print(w1)
        print("How many times did MCM win, and What is WPCT of MCM ?")
        w2 = str(Win2) + " , " + str(float(Win2/kari_epi))
        print(w2)
        m = "finished time is " + str(now)
        print(m)
        ts.saveImage(fm,s,f_rr,e_rr,kari_epi)
