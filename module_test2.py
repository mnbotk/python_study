
# coding: utf-8
from customer_m1 import Customer

#インスタンスを生成
taro = Customer(101, "斉藤太郎", 180)
hanako = Customer(102, "山田花子", 165)

#標準体重を表示
print("{} 標準体重：{:.2f}kg".format(taro.name, taro.std_weight()))
print("{} 標準体重：{:.2f}kg".format(hanako.name, hanako.std_weight()))

