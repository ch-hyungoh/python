def sum(x , y):
    tot = 0
    for k in range(x, y+1):
        tot += k

    return tot

tot = 0
start = 1
end = 10

tot = sum(start, end)

print(tot)

import math
import random
import time

r1 = abs(-5)
print(r1)

r2 = math.ceil(1.2)
r3 = math.ceil(1.8)
print(r2, r3)

r4 = math.floor(1.2)
r5 = math.floor(1.8)

r6 = round(1.2)
r7 = round(1.8)

print(r4, r5, r6, r7)

r8 = math.sqrt(4)
r9 = math.sqrt(9)
print(r8, r9)

num1 = random.random()
print(num1)

num2 = num1*10
print(num2)

num3 = math.ceil(num2)
print(num3)

num4 = math.ceil(random.random() * 10)
print(num4)

t1 = time.time()
print(t1)

t2 = time.ctime()
print(t2)

now = time.localtime(time.time())
year = time.strftime("%Y", now)
month = time.strftime("%m", now)
date = time.strftime("%d", now)
hour = time.strftime("%h", now)
min = time.strftime("%M", now)
sec = time.strftime("%s", now)

print(now)
print("%s, %s, %s" %(year, month, date))
print(hour, min, sec)