import requests
import random

index = random.sample(range(4), 4)#抽出する添字を取得
init_order = [i+1 for i in index]
init_pattern = [0,0,0,0]
for i in range(4):
    if i<2:
        init_pattern[init_order[i]-1] = 5
    else:
        init_pattern[init_order[i]-1] = 6

print(init_order)
print(init_pattern)

info = {"init_order":init_order}
response = requests.post('http://localhost:8000/start', data=info)
