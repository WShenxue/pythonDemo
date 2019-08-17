# coding:utf-8

import jieba
txt = open("沉默的羔羊.txt", "r", encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
maxc = 0
maxw = ""
for key in counts:
    if counts[key] > maxc:
        maxc = counts[key]
        maxw = key
    if counts[key] == maxc and key > maxw:
        maxw = key
print(maxw)
