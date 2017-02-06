
# coding: utf-8

names = {"Taro":55, "Makoto":49, "Akiko":30, "Kazuo":32, "Chie":22, "Ken":48}

print("*************************************************")
for name in sorted(names.items(), key= lambda n: n[0]):
    print(name[0],name[1])

print("*************************************************")
for name in sorted(names.items()):
    print(name[0],name[1])

print("*************************************************")
for name in sorted(names.keys()):
    print(name,names[name])

print("*************************************************")
for name in sorted(names.items(), key=lambda n: n[0]):
    print(name[0],name[1])
