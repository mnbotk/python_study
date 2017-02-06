
# coding: utf-8

import random

def random_gen(num):
    #生成済みの乱数を格納するリスト
    randoms = []
    
    while True:
        rand_num = random.randrange(num)
        #乱数に重複がない場合
        if rand_num not in randoms:
            randoms.append(rand_num)
            yield rand_num
        #すべての乱数を生成した
        elif len(randoms) == num:
            break
            
rand = random_gen(10)
print(next(rand))
print(next(rand))
print(next(rand))
print(next(rand))
print(next(rand))


print("*************")

rg = random_gen(100)
for r in rg:
    print(r)

