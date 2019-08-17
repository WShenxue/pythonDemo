# -*- coding: UTF-8 -*-
# coding:utf-8

import jieba

excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此", "商议", "如何", "左右"}

txt = open("threekingdoms.txt", "r", encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word ==  "孔明曰":
        word = "孔明"
    elif word == "关公"or word == "云长":
        word = "关羽"
    elif word == "玄德" or word == "玄德曰":
        word = "刘备"
    elif word == "孟德" or word == "丞相":
        word = "曹操"
    else:
        counts[word] = counts.get(word, 0) + 1
# 过滤字典
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))