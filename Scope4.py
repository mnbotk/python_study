
# coding: utf-8
value4 = 1
def scope_test4():
    global value4
    value4 = 100
    print("内部：",value4)
    
scope_test4()
print("外部：",value4)
