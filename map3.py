
# coding: utf-8

#def to_cm(inch):
#    return inch * 2.54
#
#inches = [9, 5.5, 6, 4, 5, 6.5, 10]
#for cm in map(to_cm,inches):
#    print(cm)

#上記をlamda式で
for cm in map(lambda inch: inch * 2.54,[9, 5.5, 6, 4, 5, 6.5, 10]):
    print(cm)