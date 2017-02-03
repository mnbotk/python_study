
# coding: utf-8

#dic = {"日":"Sun", "月":"Mon", "火":"Tue", "水":"Wed", "木":"Thu", "金":"Fri", "土":"Sat"}
#登録順で出力する必要がある場合はOrderedDictでの登録を使用する
from collections import OrderedDict
dic = OrderedDict([("日","Sun"), ("月","Mon"), ("火","Tue"), ("水","Wed"), ("木","Thu"), ("金","Fri"), ("土","Sat")])

for jap, eng in dic.items():
    print("{}: {}".format(jap, eng))
