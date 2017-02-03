
# coding: utf-8
def doll_to_yen(doll,rate):
    return doll * rate

#引数にリテラルを指定して呼出す
yen = doll_to_yen(100, 105)
print("為替レート: {}".format(105))
print("{}ドルは{}円".format(100, yen))

rate = 100
doll = 150
#引数に変数を指定して呼出す
yen = doll_to_yen(doll, rate)
print("為替レート： {}".format(rate))
print("{}ドルは{}円".format(doll, yen))
