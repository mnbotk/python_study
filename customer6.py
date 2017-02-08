
# coding: utf-8

class Customer:
    bmi = 22.1
    def __init__(self, number, name, height=0):
        self.number = number
        self.name = name
        self.height = height
        
#メソッドを定義
def show_info(self):
    print("{}: {}".format(self.number, self.name))
    
#メソッドを追加
Customer.show_info = show_info

#インスタンスを生成
taro = Customer(101, "斉藤太郎", 180)

taro.show_info()
