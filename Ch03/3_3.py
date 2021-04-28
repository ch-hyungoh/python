"""#for
for i in range(5):
    print(i)

for i in range(10, 20):
    print(i)

for k in range(10, 0, -1):
    print(k)
#for 1부터 10까지 합
sum = 0
for i in range(11):
    sum += i
print(sum)
#for 1부터 10까지 짝수합
sum2 =0
for k in range(11):
    if k % 2 == 0:
        sum2 += k
print(sum2)
#for 중첩 for
for a in range(3):
    print(a)

    for b in range(4):
        print(b)
#for 구구단
"""
for q in range(2, 10):
    for w in range(1, 10):
        print("{} * {} = {}".format(q, w, q*w))
#for 별 삼각형
for a in range(10, 0, -1):
    for b in range(a):
        print("★", end=" ")
    print("\n")

for i in range(10):
    print("☆" * i)
#for list를 이용한 for
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

for person in ["김유신", "김춘추", "장보고"]:
    print(person)

scores = [62, 86, 72, 74, 96]
total = 0

for i in scores:
    total += i
print(total)
#for list를 이용한 for

for index, value in enumerate(scores):
    print("{}, {}".format(index, value))
#for complihension
list1 = [1, 2, 3, 4, 5]
list2 = [num * 2 for num in list1]
print(list2)