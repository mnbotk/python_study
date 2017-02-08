
# coding: utf-8
class Customer:
    def __init__(self, number, name, height=0):
        self.number = number
        self.name = name
        self.height = height
    

#インスタンスを作成
taro = Customer(101, "斉藤太郎", 180)
print("{}: {} {}cm".format(taro.number, taro.name, taro.height))

#身長を変更
taro.height = 175
print("{}: {} {}cm".format(taro.number, taro.name, taro.height))
