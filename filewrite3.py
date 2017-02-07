
# coding: utf-8

import os, sys, random

#引数がひとつであることを確認
if len(sys.argv) != 2:
    print("ファイル名をひとつ指定してください")
    sys.exit()
    
#パスが存在するかを確認
path = sys.argv[1]
#path = "kuji.txt"
if os.path.exists(path):
    if input("上書しますか？(y/n):") != "y":
        sys.exit()

kuji = ["大吉","中吉","凶"]
with open(path, "w", encoding="utf_8") as f:
    f.write(kuji[random.randrange(len(kuji))] + "\n")
