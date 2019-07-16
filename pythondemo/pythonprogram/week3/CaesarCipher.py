# -*- coding:utf-8 -*-

# 凯撒密码：原文P，密文C
# C = (P + 3) mod 26
# P = (C - 3) mod 26
ori = input()
res = ''
for p in ori:
    if 'A' <= p <= 'Z':
        # res += chr(ord(p) + 3)
        res += chr(ord('A') + (ord(p) - ord('A') + 3) % 26)
    elif 'a' <= p <= 'z':
        res += chr(ord('a') + (ord(p) - ord('a') + 3) % 26)
    else:
        res += p
print(res)
