from customer_m2 import Customer
from datetime import date

class GoldCutomer(Customer):
    def __init__(self, number, name, height=0, birthdate=0):
        self.__birthdate = birthdate
        super().__init__(number, name, height)
        
    #birthdateプロパティの設定
    def get_birthdate(self):
        return self.__birthdate
    birthdate = property(get_birthdate)
    
#テスト用
if __name__ == "__main__":
    taro = GoldCutomer(101, "斉藤太郎", 180, date(1978,9,1))
    #スーパークラスのプロパティ
    name = taro.name
    number = taro.number
    height = taro.height
    #スーパークラスのメソッド
    std_weight = taro.std_weight()
    #サブクラスのインスタンス変数
    birth = taro.birthdate
    
    print("{} {} 身長:{}cm 標準体重:{:.2f}kg 誕生日:{}".format(number, name, height, std_weight, birth))