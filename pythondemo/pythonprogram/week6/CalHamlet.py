# -*- coding:utf-8 -*-

def getText():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")
    return txt


hamletText = getText()
words = hamletText.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
# 列表的.sort方法b
# key=lambda x: x[1] 第二个元素
# reverse=True 从大到小排序
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print(word)