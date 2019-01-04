import numpy as np
import csv
import matplotlib.pyplot as plt

def readQtable(number):
    fn = '../log/20181217_001117/im_field/point/' + str(number) + '_point.csv'
    with open(fn, 'r') as file:
        lst = list(csv.reader(file))
    a = []
    for i in range(14):
        a.append(list(map(int,lst[i])))

    q_table = np.array(a)

    return q_table

if __name__ == "__main__":
    for i in range(5000):
        a = np.ravel(readQtable(i))
        b = a.tolist()
        print(len(b))
        """
        c = []
        for j in range(len(b)):
            if b[j]!= 0:
                c.append(b[j])
            elif j!=0 and j!=len(b)-1 and b[j]==0 and b[j+1]!=0 and b[j-1]!=0:
                c.append(b[j])
        #d = np.array(c)
        plt.hist(c, bins=88)
        plt.title("Histgram")
        plt.xlabel("points")
        plt.ylabel("tilenum")
        #plt.show()
        fn = './point_histgram/' + str(i) + '_phist.png'
        plt.savefig(fn)
        plt.clf()
        """
