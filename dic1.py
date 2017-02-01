
# coding: utf-8
dic = {"日":"Sun", "月":"Sun", "火":"Sun", "水":"Sun", "木":"Sun", "金":"Sun", "土":"Sun"}

key = input("キーを入力してください：")
if key in dec:
    del dic[key];
    print(dic)
else:
    print('キー"{}"が見つかりませんでした'.format(key))
