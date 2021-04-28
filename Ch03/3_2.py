num1 = 1
while num1<5:
    print(num1)
    num1 += 1

k, sum = 1, 0

while k <= 10:
    sum += k
    k += 1

print(sum)

i, tot = 1, 0

while i <= 10:
    if i % 2 == 0:
        tot += i
    i += 1

print(tot)

num = 1

while True:
    if num % 5 == 0 and num % 7 == 0:
        break
    num += 1
print(num)

s, total = 1, 0

while s <= 10:

    s += 1

    if s % 2 == 1:
        continue
    total += s


print(total)

