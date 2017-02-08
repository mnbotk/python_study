
# coding: utf-8

from datetime import date

class Customer:
    bmi = 22
    def __init__(self, number, name, height=0):
        self.number = number
        self.name = name
        self.height = height
    
    #標準体重を戻す
    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2
    
#インスタンスを生成
taro = Customer(101, "斉藤太郎", 180)
#インスタンス変数を追加
taro.birthdate = date(1989, 7, 3)
#標準体重を表示
print("{} 誕生日：{}".format(taro.name, taro.birthdate))

