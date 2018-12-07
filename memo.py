import requests
import random
import numpy as np

index = random.sample(range(4), 4)#抽出する添字を取得
init_order = [i+1 for i in index]
print(init_order)

list = [i+1 for i in np.argsort(init_order)]

if list.index(1) > list.index(2):
    k = list.index(2)
    list[list.index(1)] = 2
    list[k] = 1
if list.index(3) > list.index(4):
    k = list.index(4)
    list[list.index(3)] = 4
    list[k] = 3


print(list)

info = {"init_order":init_order}
response = requests.post('http://localhost:8002/start', data=info)
