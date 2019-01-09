import csv
import gym
import numpy as np
import sys
import datetime
import os
import matplotlib.pyplot as plt

def init_func(fm):
    mkdi = './log/' + fm
    os.mkdir(mkdi)
    mkdi = './log/' + fm + '/text_log'
    os.mkdir(mkdi)
    mkdi = './log/' + fm + '/q_table'
    os.mkdir(mkdi)
    mkdi = './log/' + fm + '/images'
    os.mkdir(mkdi)
    mkdi = './log/' + fm + '/images/result_totalpoint'
    os.mkdir(mkdi)
    mkdi = './log/' + fm + '/images/result_tilepoint'
    os.mkdir(mkdi)
    mkdi = './log/' + fm + '/images/result_fieldpoint'
    os.mkdir(mkdi)
    mkdi = './log/' + fm + '/images/result_reward'
    os.mkdir(mkdi)
    mkdi = './log/' + fm + '/images/result_reward_onestep'
    os.mkdir(mkdi)
    mkdi = './log/' + fm + '/im_field'
    os.mkdir(mkdi)
    mkdi = './log/' + fm + '/im_field/point'
    os.mkdir(mkdi)
    mkdi = './log/' + fm + '/im_field/tile'
    os.mkdir(mkdi)

def readQtable(type):
    fn = './log/' + type
    with open(fn, 'r') as file:
        lst = list(csv.reader(file))
    a = []
    for i in range(144):
        a.append(list(map(float,lst[i])))
    q_table = np.array(a)

    return q_table

def writeQtable(fm, type, q_table, episode):
    fn = './log/' + fm + '/q_table/' + str(episode) + '_' + type
    with open(fn, 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(q_table)

def readLParam(fn):
    r = []
    with open(fn, 'r') as file:
        lst = list(csv.reader(file))
    for i in range(10):
        if i < 6:
            r.append(float(lst[0][i]))
        else:
            r.append(lst[0][i])
    return r

def Log(fm, when,info=None,epoch=None):
    fn = './log/' + fm + '/text_log/' + fm + '.txt'
    f = open(fn,'a')
    if epoch is None and info is None and when is "start":
        m1 = "==================== start ( start time : " + fm + " ) ==================== \n"
        f.write(m1)
        f.close()
    elif epoch is None and when is "info":
        m1 = "port num is " + str(int(info[0])) + ", " + "epoch is " + str(int(info[1])) + ", " + "q learning late is " + str(info[4]) + ", " + "mcm learning late is " + str(info[5]) + ", " + "q learning type is " + info[6] + ", " + "mcm type is " + info[7] + ", " + "qtable of q learning is " + info[8] + ", " + "qtable of mcm is " + info[9] + " .\n"
        m2 = "-------------------------------------------------- \n"
        m = m1 + m2
        f.write(m)
        f.close()
    elif when == "now learning":
        m1 = str(epoch) + " epoch finished : " + "avarage time of a epoch is " + str(info[0]) + " / WPCT of agent1 is " + str(info[1]) + " , agent2 is " + str(info[2]) + " / avarage of reward1 is " + str(info[3]) + " , reward2 is " + str(info[4]) + " .\n"
        f.write(m1)
        f.close()
    elif epoch is None and when is "finished":
        m1 = "successfuly! : runtime is " + str(info[7]) + " \n"
        m2 = "agent1 won : " + str(info[0]) + " , agent2 won : " + str(info[1]) + "/ WPCT of agent1 is " + str(info[2]) + " , agent2 is " + str(info[3]) + " / avarage of reward1 is " + str(info[4]) + " , reward2 is " + str(info[5]) + " .\n"
        m3 = "==================== finished *successfuly* ( finished time : " + info[6] + " ) ==================== \n"
        m = m1 + m2 + m3
        f.write(m)
        f.close()
    elif epoch is None and when is "error":
        m1 = "error! : runtime is " + str(info[7]) + "\n"
        m2 = info[8] + "\n"
        m3 = "agent1 won : " + str(info[0]) + " , agent2 won : " + str(info[1]) + "/ WPCT of agent1 is " + str(info[2]) + " , agent2 is " + str(info[3]) + " / avarage of reward1 is " + str(info[4]) + " , reward2 is " + str(info[5]) + " .\n"
        m4 = "==================== finished *error* ( finished time : " + info[6] + " ) ==================== \n"
        m = m1 + m2 + m3 + m4
        f.write(m)
        f.close()

def getTime(type, start=None):
    now = datetime.datetime.now()
    if start is None and type == "filename":
        fs = now.strftime("%Y%m%d_%H%M%S")
        return fs,now
    elif start is None and type == "timestamp_s":
        fs = now.strftime("%Y%m%d_%H%M%S")
        return fs,now
    elif type == "timestamp_on":
        fs = now.strftime("%Y%m%d_%H%M%S")
        delta = now - start
        return delta,fs,now
"""
def mkCSV_reward_init(epoch):
    log_reward = np.zeros((epoch, 2))
    fn = 'q_table_' + sys.argv[1] + '.csv'
    with open(fn, 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(q_table)
"""
def saveField(env, fm, epoch, turn):
    """
    if epoch == 0:
        mkdi = './log/' + fm + '/im_field'
        os.mkdir(mkdi)
        mkdi = './log/' + fm + '/im_field/point'
        os.mkdir(mkdi)
        mkdi = './log/' + fm + '/im_field/tile'
        os.mkdir(mkdi)
    """
    if turn == 0:
        mkdi = './log/' + fm + '/im_field/tile/' + str(epoch)
        os.mkdir(mkdi)
        pf = env.savePField()
        pf_a = np.array(pf)
        fn = './log/' + fm + '/im_field/point/' + str(epoch) + '_point.csv'
        with open(fn, 'w') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerows(pf_a)
    uf = env.saveUField()
    uf_a = np.array(uf)
    fn = './log/' + fm + '/im_field/tile/' + str(epoch) + '/' + str(epoch) + '_' + str(turn) + '_tile.csv'
    with open(fn, 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(uf_a)

def saveImage(fm,s,f_rr,e_rr,s_avg,f_rr_avg,e_rr_avg,f_rr_oneTurn,e_rr_oneTurn,f_rr_oneTurn_avg,e_rr_oneTurn_avg,episode):
    plt.figure()
    plt.plot(s[2], 'r', label="QL",alpha=0.2)
    plt.plot(s[5], 'b', label="MCM",alpha=0.2)
    plt.plot(s_avg[2], 'r', label="QL avg")
    plt.plot(s_avg[5], 'b', label="MCM avg")
    plt.xlim(0, episode)
    plt.ylim(min(min(s[2]),min(s[5]))-50, max(max(s[2]),max(s[5]))+50)
    plt.xlabel("epoch")
    plt.ylabel("total point")
    plt.legend(loc='lower right')
    fn1 = './log/' + fm + '/images/result_totalpoint/result_totalpoint_' + str(episode) + '.png'
    plt.savefig(fn1)
    plt.close()

    plt.figure()
    plt.plot(s[0], 'r', label="QL",alpha=0.2)
    plt.plot(s[3], 'b', label="MCM",alpha=0.2)
    plt.plot(s_avg[0], 'r', label="QL avg")
    plt.plot(s_avg[3], 'b', label="MCM avg")
    plt.xlim(0, episode)
    plt.ylim(min(min(s[0]),min(s[3]))-50, max(max(s[0]),max(s[3]))+50)
    plt.xlabel("epoch")
    plt.ylabel("tilepoint")
    plt.legend(loc='lower right')
    fn2 = './log/' + fm + '/images/result_tilepoint/result_tilepoint_' + str(episode) + '.png'
    plt.savefig(fn2)
    plt.close()

    plt.figure()
    plt.plot(s[4], 'b', label="MCM",alpha=0.2)
    plt.plot(s[1], 'r', label="QL", alpha=0.2)
    plt.plot(s_avg[4], 'b', label="MCM avg")
    plt.plot(s_avg[1], 'r', label="QL avg")
    plt.xlim(0, episode)
    plt.ylim(min(min(s[1]),min(s[4]))-50, max(max(s[1]),max(s[4]))+50)
    plt.xlabel("epoch")
    plt.ylabel("fieldpoint")
    plt.legend(loc='lower right')
    fn3 = './log/' + fm + '/images/result_fieldpoint/result_fieldpoint_' + str(episode) + '.png'
    plt.savefig(fn3)
    plt.close()

    plt.figure()
    plt.plot(f_rr, 'r', label="QL",alpha=0.2)
    plt.plot(e_rr, 'b', label="MCM",alpha=0.2)
    plt.plot(f_rr_avg, 'r', label="QL avg")
    plt.plot(e_rr_avg, 'b', label="MCM avg")
    plt.xlim(0, episode)
    plt.ylim(min(min(f_rr),min(e_rr))-50, max(max(f_rr),max(e_rr))+50)
    plt.xlabel("epoch")
    plt.ylabel("reward")
    plt.legend(loc='lower right')
    fn4 = './log/' + fm + '/images/result_reward/result_reward_' + str(episode) + '.png'
    plt.savefig(fn4)
    plt.close()

    plt.figure()
    plt.plot(f_rr_oneTurn, 'r', label="QL",alpha=0.2)
    plt.plot(e_rr_oneTurn, 'b', label="MCM",alpha=0.2)
    plt.plot(f_rr_oneTurn_avg, 'r', label="QL avg")
    plt.plot(e_rr_oneTurn_avg, 'b', label="MCM avg")
    plt.xlim(0, episode)
    plt.ylim(min(min(f_rr_oneTurn),min(e_rr_oneTurn))-50, max(max(f_rr_oneTurn),max(e_rr_oneTurn))+50)
    plt.xlabel("epoch")
    plt.ylabel("reward per one step")
    plt.legend(loc='lower right')
    fn4 = './log/' + fm + '/images/result_reward_onestep/result_reward_onestep' + str(episode) + '.png'
    plt.savefig(fn4)
    plt.close()

"""
def notify(num_episode,Win1,Win2,s3,s6):#,s3,s4,s5,s6):
    #table = Texttable()
    ended_mess = "Learning was successful!\n"
    epoch_mess = "epoch is " + str(num_episode) + "\n"
    result_mess = "How many times did QL win?\n" + str(Win1) + "\n" + "How many times did MCM win?\n" + str(Win2) + "\n"
    finaltotalPoint_mess = "{total point}\n" + "[final point]\n" + "QL is " + str(s3[num_episode-1]) + "\n" + "MCM is " + str(s6[num_episode-1]) + "\n"
    maxtotalPoint_mess = "[max point]\n" + "QL is " + str(max(s3)) + "\n" + "MCM is " + str(max(s6)) + "\n"
    mintotalPoint_mess = "[min point]\n" + "QL is " + str(min(s3)) + "\n" + "MCM is " + str(min(s6)) + "\n"
    finaltilePoint_mess = "{tile point}\n" + "[final point]\n" + "QL is " + str(s1[num_episode-1]) + "\n" + "MCM is " + str(s4[num_episode-1]) + "\n"
    maxtilePoint_mess = "[max point]\n" + "QL is " + str(max(s1)) + "\n" + "MCM is " + str(max(s4)) + "\n"
    mintilePoint_mess = "[min point]\n" + "QL is " + str(min(s1)) + "\n" + "MCM is " + str(min(s4)) + "\n"
    finalpanelPoint_mess = "{panel point}\n" + "[final point]\n" + "QL is " + str(s2[num_episode-1]) + "\n" + "MCM is " + str(s2[num_episode-1]) + "\n"
    maxpanelPoint_mess = "[max point]\n" + "QL is " + str(max(s2)) + "\n" + "MCM is " + str(max(s5)) + "\n"
    minpanelPoint_mess = "[min point]\n" + "QL is " + str(min(s2)) + "\n" + "MCM is " + str(min(s5)) + "\n"
    mess = ended_mess + epoch_mess + result_mess + finaltotalPoint_mess + maxtotalPoint_mess + mintotalPoint_mess #+ finaltilePoint_mess + maxtilePoint_mess + mintilePoint_mess + finalpanelPoint_mess + maxpanelPoint_mess + minpanelPoint_mess
    fig_name = ['./result/result_point.png', './result/result_reward.png']
    #table.add_rows(['total','final','max','min'],['QL',str(s3[num_episode-1]),str(max(s3)),str(min(s3))],['MCM',str(s6[num_episode-1]),str(max(s6)),str(min(s6))])
    Log(m,fm)
    linenotify.main_m(mess)
    for i in range(2):
        linenotify.main_f(fig_name[i],fig_name[i])
"""
