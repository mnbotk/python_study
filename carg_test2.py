# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:10:02 2017

@author: ohtsukam
"""

import sys

sum = 0
for i in range(1, len(sys.argv)):
    sum += float(sys.argv[i])

print(u"総和：　{}".format(sum))