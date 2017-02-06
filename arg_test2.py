
# coding: utf-8
def test2(num):
    #関数の内部で引数を変更
    print("num(): {}".format(id(num)))
    num += 10
    print("num(): {}".format(id(num)))
    
n = 3
test2(n)
print(n)
