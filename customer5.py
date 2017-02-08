
# coding: utf-8

class Customer:
    bmi = 22.1
    def __init__(self, number, name, height=0):
        self.number = number
        self.name = name
        self.height = height
        
#クラス変数を追加
Customer.LIMIT = 50

#インスタンスを生成
taro = Customer(101, "斉藤太郎", 180)
hanako = Customer(102, "山田花子", 165)

print(taro.LIMIT)
print(hanako.LIMIT)
print(Customer.LIMIT)

