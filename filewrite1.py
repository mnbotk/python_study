
# coding: utf-8

with open("out.txt", "w", encoding="utf_8") as f:
    f.write("こんにちは")
    f.write("Pythonの世界へようこそ\n")
    f.write(str(2017))
    f.write("年\n")


print("******************************")

with open("out.txt", "a", encoding="utf_8") as f:
    f.write("さようなら\n")


print("******************************")

weekdays = ["月曜日\n","火曜日\n","水曜日\n","木曜日\n","金曜日\n","土曜日\n","日曜日\n"]

with open("days.txt", "w", encoding="utf_8") as f:
    f.writelines(weekdays)


print("******************************")

import os, sys, random

#引数がひとつであることを確認
#if len(sys.argv) != 2:
#    print("ファイル名をひとつ指定してください")
#    sys.exit()
    
#パスが存在するかを確認
#path = sys.argv[1]
path = "kuji.txt"
if os.path.exists(path):
    if input("上書しますか？(y/n):") != "y":
        sys.exit()

kuji = ["大吉","中吉","凶"]
with open(path, "w", encoding="utf_8") as f:
    f.write(kuji[random.randrange(len(kuji))] + "\n")


print("******************************")
