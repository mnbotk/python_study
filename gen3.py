
# coding: utf-8

str = "HeLlo"

gen = (c for c in str.upper())
for c in gen:
    print(c)

print("********************")

gen = [c for c in str.upper()]
for c in gen:
    print(c)

print("********************")
