
# coding: utf-8
#***********関数
def larger_5(inch):
    return inch > 5

inches = [9, 5.5, 6, 4, 5, 6.5, 10]

cms = []
for inch in filter(larger_5, inches):
    cms.append(inch * 2.54)
print(cms)


#***********lambda式
#inches = [9, 5.5, 6, 4, 5, 6.5, 10]
cms = []
for inch in filter(lambda inch: inch > 5, inches):
    cms.append(inch * 2.54)
print(cms)

#***********内包表記
#inches = [9, 5.5, 6, 4, 5, 6.5, 10]
cms = [inch * 2.54 for inch in inches if inch > 5]
print(cms)
