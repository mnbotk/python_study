
# coding: utf-8

f = open("sample.txt","r", encoding="utf_8")
lines = f.read()
print(lines)
f.close()

print("***********************")

f = open("sample.txt","r", encoding="utf_8")
lines = f.read(2)
print(lines)
lines = f.read(2)
print(lines)
f.close()


print("***********************")

f = open("sample.txt","r", encoding="utf_8")
lines = f.readlines()

for i,line in enumerate(lines):
    print("{:4d}: {}".format(i + 1, line.rstrip("\n")))

f.close()


print("***********************")

f = open("sample.txt","r", encoding="utf_8")
lines = f.readlines()

for i,line in enumerate(lines):
    print("{:4d}: {}".format(i + 1, line), end="")

f.close()


print("***********************")

import random

f = open("kakugen.txt","r", encoding="utf_8")
lines = f.readlines()

kakugen = lines[random.randrange(len(lines))]
print(kakugen.rstrip("\n"))

print("***********************")
