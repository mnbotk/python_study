
# coding: utf-8
class Customer:
    bmi = 22
    def __init__(self, number, name, height=0):
        self.__number = number
        self.__name = name
        self.__height = height
        
    #nameのゲッターメソッド
    def get_name(self):
        return self.__name
    
    #numberのゲッターメソッド
    def get_number(self):
        return self.__number
    
    #numberのセッターメソッド
    def set_number(self, number):
        self.__number = number
        
    #heightのゲッターメソッド
    def get_height(self):
        return self.__height
    
    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2
    
    #プロパティ
    name = property(get_name)
    number = property(get_number, set_number)
    height = property(get_height)
