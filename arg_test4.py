
# coding: utf-8
def test4(lst):
    print("lst: {}".format(id(lst)))
    lst = lst + [3,4]
    print("関数内部：{}".format(str(lst)))
    print("lst: {}".format(id(lst)))
    
l = [1, 2, 3]
test4(l)
print(l)
