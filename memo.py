import requests
import random
import numpy as np
import os
import datetime
import pprint
"""
now = datetime.datetime.now()
fm = './qtable/' + now.strftime("%Y%m%d_%H%M%S")
os.mkdir(fm)

p = random.choice([[0,1,2,3,4],[0,3,4,1,2],[1,1,3,2,4],[1,3,1,4,2],[2,1,3,4,2],[2,3,1,2,4]])
pattern = p[0]
p.pop(0)
init_order = p

info = {"init_order":init_order,"pattern":pattern}
response = requests.post('http://localhost:8002/start', data=info)

p = random.choice([[0,1,2,3,4],[0,3,4,1,2],[1,1,3,2,4],[1,3,1,4,2],[3,1,3,4,2],[3,3,1,2,4]])
print(p)
p.pop(0)
print(p)
def getTime(type, start=None):
    now = datetime.datetime.now()
    if start is None and type == "filename":
        fs = now.strftime("%Y%m%d_%H%M%S")
        return fs,now
    elif start is None and type == "timestamp_s":
        return now
    elif type == "timestamp_on":
        delta = now - start
        return delta,now

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

now1 = datetime.datetime.now()
fm = now1.strftime("%Y%m%d_%H%M%S")
s = [[],[],[],[],[]]
s[0].append("a")
now2 = datetime.datetime.now()
delta = now2 - now1
print(str(delta))

start = getTime("timestamp_s")
print(start)
a = getTime("timestamp_on",start)
print(a)
print(a/2)
print(sum([0,1,2,3,4,5])/5)

a = [1,2,3,4,5,6,7,8]
print(float(sum(a)/8))
fs,now = getTime("filename")
init_func(fs)
"""
local_url = 'http://localhost:8002'

def savePField():
    global local_url
    url = local_url + '/show/im_field'
    resp = requests.get(url).text.encode('utf-8').decode().replace("\n", " ").replace("  "," ")
    li_pfield = [int(i) for i in resp.split()]
    return li_pfield

def saveUField():
    global local_url
    url = local_url + '/show/im_user'
    resp = requests.get(url).text.encode('utf-8').decode().replace("\n", " ").replace("  "," ")
    li_ufield = [int(i) for i in resp.split()]
    return li_ufield

def fun(usr,dir):
    data = {
        'usr': str(usr),
        'd': dir
    }
    url = 'http://localhost:8002/judgedirection'
    f = requests.post(url, data = data).text.encode('utf-8').decode().replace("\n", " ").replace("  "," ")
    iv_list = [i for i in f.split()]
    il = [int(iv_list[0]),int(iv_list[1])]
    return iv_list

def main():
    p = random.choice([[0,1,2,3,4],[0,3,4,1,2],[1,1,3,2,4],[1,3,1,4,2],[2,1,3,4,2],[2,3,1,2,4]])
    pattern = p[0]
    p.pop(0)
    init_order = p

    info = {"init_order":init_order,"pattern":pattern}
    response = requests.post('http://localhost:8002/start', data=info)

    print(init_order)

if __name__ == "__main__":
    main()
    #a = fun(1,"r")
    #print(a)
    #a = []
    #b = ''
    #for i in range(len(a)):
    #    b += a[i]
    #print(b)
