
# coding: utf-8

f = open("sample.txt","r", encoding="utf_8")

i=0
while True:
    line = f.readline()
    if line == "":
        break
    print("{:4d}: {}".format(i + 1, line.rstrip("\n")))
    i += 1

f.close()


print("*******************************")

f = open("sample.txt","r", encoding="utf_8")

for i, line in enumerate(f):
    print("{:4d}: {}".format(i + 1, line.rstrip("\n")))

f.close()


print("*******************************")

with open("sample.txt","r", encoding="utf_8") as f:
    for i, line in enumerate(f):
        print("{:4d}: {}".format(i + 1, line.rstrip("\n")))


print("*******************************")

#空の辞書を用意
results = {}

with open("answer.txt", "r", encoding="utf_8") as f:
    for line in f:
        country = line.rstrip("\n")
        if country in results:
            results[country] += 1
        else:
            results[country] = 1

#結果をソートして表示
for country in sorted(results.items(), key = lambda c:c[1], reverse=True):
    print("{}: {}".format(country[0],country[1]))


print("*******************************")



