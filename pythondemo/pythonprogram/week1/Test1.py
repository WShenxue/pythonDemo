num = int(input())
str = "Hello World"
res = ""
if num == 0:
    print(str)
elif num > 0:
    for n in range(len(str)):
        if (n + 1) % 2 != 0:
            res = res + str[n]
            if len(str) == (n + 1):
                print(res)
        else:
            res = res + str[n]
            print(res)
            res = ""

else:
    for n in str:
        print(n)