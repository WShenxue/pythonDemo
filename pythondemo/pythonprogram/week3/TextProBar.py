import time

print("{:-^50}".format("执行开始"))
scale = 50
start = time.perf_counter()
for i in range(51):
    a = '*' * i
    b = (scale - i) * '.'
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print("\r{:3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
    time.sleep(0.1)
print("\n{:-^50}".format("执行结束"))

