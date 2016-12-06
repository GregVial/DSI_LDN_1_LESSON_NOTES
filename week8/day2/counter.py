#!/usr/bin/env python

import numpy as np
import sys
import re
import collections
import matplotlib.pyplot as plt

dicty={}

for line in sys.stdin:
    for word in line.split(" "):
	word = word.lower()
        word = re.sub(r'[^a-zA-Z]*([a-zA-Z]*)[^a-zA-Z]*',r'\1',word)
	if len(word) != 0:
            if word not in dicty.keys():
     	        dicty[word] = 1
	    else:
	        dicty[word] += 1

#order = collections.OrderedDict(sorted(dicty.items()))

#for k,v in od.items():
#    print("%s %d" % (k,v))

od = sorted(dicty,key=dicty.get,reverse = True)

#for word in od:
#    print("%s %d" % (word,dicty[word]))


dictx = {}
for k,v in dicty.items():
    if v in dictx.keys():
        dictx[v].append(k)
    else:
        dictx[v] = [k]

for k,v in dictx.items():
    print(k,v)


dictz = {}
for k,v in dicty.items():
    if v>1:
        dictz[k] = v

plt.figure(figsize=(20,10))
plt.bar(range(len(dictz)), dictz.values(), align='center')
plt.xticks(range(len(dictz)), dictz.keys(),rotation=45)
plt.xlim(-1,len(dictz))
#plt.xticklabels(dicty.keys(),rotation=90)
plt.show()
