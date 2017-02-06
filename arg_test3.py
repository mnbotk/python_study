
# coding: utf-8
def test3(lst):
    print("lst: {}".format(id(lst)))
    lst[0] = 0
    lst.append(100)
    print("lst: {}".format(id(lst)))
    
l = [1, 2, 3]
test3(l)
print(l)
