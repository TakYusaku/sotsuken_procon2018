import csv
import numpy as np
import sys
import datetime

def readQtable(type):
    fn = type
    with open(fn, 'r') as file:
        lst = list(csv.reader(file))
    a = []
    for i in range(144):
        a.append(list(map(float,lst[i])))
    q_table = np.array(a)

    return q_table

def readLParam(fn):
    r = []
    with open(fn, 'r') as file:
        lst = list(csv.reader(file))
    for i in lst[0]:
        r.append(float(i))
    return r

def Log(when,epoch,info=None):
    now = datetime.datetime.now()
    fm = now.strftime("%Y%m%d_%H%M%S")
    fn = './log/' + fm + '.txt'
    f = open(fn,'a')

    if info is None and when is "start":
        m1 = "==================== start ==================== \n"
        m2 = "start time is " + now.strftime("%H%M%S") + "\n"
        m = m1 + m2
        f.write(m)
        f.close()
    elif info is None and when is "info":
        m1 = "total epoch is " + str(epoch) + "\n"
        m2 = " "+ "-------------------------------------------------- \n"
        f.write(m1)
        f.close()
    elif when is "learning":
        m1 = "now epoch is " + str(epoch) + "\n"
        m2 =



def mkCSV_reward_init(epoch):
    log_reward = np.zeros((epoch, 2))

    fn = 'q_table_' + sys.argv[1] + '.csv'
    with open(fn, 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(q_table)

def save_resultImage(s3,s6,episode):
    plt.subplot(2,2,1)
    plt.plot(s3, 'r', label="QL")
    plt.plot(s6, 'b', label="MCM")
    plt.xlim(0, episode)
    plt.ylim(-500, 500)
    plt.xlabel("epoch")
    plt.ylabel("total point")
    plt.legend(loc='lower right')
    plt.subplot(2,2,3)
    plt.plot(s1, 'r', label="QL")
    plt.plot(s4, 'b', label="MCM")
    plt.xlim(0, episode)
    plt.ylim(-500, 500)
    plt.xlabel("epoch")
    plt.ylabel("tilepoint")
    plt.legend(loc='lower right')
    plt.subplot(2,2,4)
    plt.plot(s2, 'r', label="QL")
    plt.plot(s5, 'b', label="MCM")
    plt.xlim(0, episode)
    plt.ylim(-500, 500)
    plt.xlabel("epoch")
    plt.ylabel("fieldpoint")
    plt.legend(loc='lower right')
    plt.savefig('./result/result_point.png')

    plt.figure()
    plt.plot(f_rr, 'r', label="QL")
    plt.plot(e_rr, 'b', label="MCM")
    plt.xlim(0, episode)
    plt.ylim(-500, 500)
    plt.xlabel("epoch")
    plt.ylabel("reward")
    plt.legend(loc='lower right')
    plt.savefig('./result/result_reward.png')

def notify(num_episode,Win1,Win2,s3,s6):#,s3,s4,s5,s6):
    #table = Texttable()
    ended_mess = "Learning was successful!\n"
    epoch_mess = "epoch is " + str(num_episode) + "\n"
    result_mess = "How many times did QL win?\n" + str(Win1) + "\n" + "How many times did MCM win?\n" + str(Win2) + "\n"
    finaltotalPoint_mess = "{total point}\n" + "[final point]\n" + "QL is " + str(s3[num_episode-1]) + "\n" + "MCM is " + str(s6[num_episode-1]) + "\n"
    maxtotalPoint_mess = "[max point]\n" + "QL is " + str(max(s3)) + "\n" + "MCM is " + str(max(s6)) + "\n"
    mintotalPoint_mess = "[min point]\n" + "QL is " + str(min(s3)) + "\n" + "MCM is " + str(min(s6)) + "\n"
    """
    finaltilePoint_mess = "{tile point}\n" + "[final point]\n" + "QL is " + str(s1[num_episode-1]) + "\n" + "MCM is " + str(s4[num_episode-1]) + "\n"
    maxtilePoint_mess = "[max point]\n" + "QL is " + str(max(s1)) + "\n" + "MCM is " + str(max(s4)) + "\n"
    mintilePoint_mess = "[min point]\n" + "QL is " + str(min(s1)) + "\n" + "MCM is " + str(min(s4)) + "\n"
    finalpanelPoint_mess = "{panel point}\n" + "[final point]\n" + "QL is " + str(s2[num_episode-1]) + "\n" + "MCM is " + str(s2[num_episode-1]) + "\n"
    maxpanelPoint_mess = "[max point]\n" + "QL is " + str(max(s2)) + "\n" + "MCM is " + str(max(s5)) + "\n"
    minpanelPoint_mess = "[min point]\n" + "QL is " + str(min(s2)) + "\n" + "MCM is " + str(min(s5)) + "\n"
    """
    mess = ended_mess + epoch_mess + result_mess + finaltotalPoint_mess + maxtotalPoint_mess + mintotalPoint_mess #+ finaltilePoint_mess + maxtilePoint_mess + mintilePoint_mess + finalpanelPoint_mess + maxpanelPoint_mess + minpanelPoint_mess
    fig_name = ['./result/result_point.png', './result/result_reward.png']
    #table.add_rows(['total','final','max','min'],['QL',str(s3[num_episode-1]),str(max(s3)),str(min(s3))],['MCM',str(s6[num_episode-1]),str(max(s6)),str(min(s6))])
    Log(m,fm)
    """
    linenotify.main_m(mess)
    for i in range(2):
        linenotify.main_f(fig_name[i],fig_name[i])
    """
