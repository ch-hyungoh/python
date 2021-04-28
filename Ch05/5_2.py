#defoult 매개변수
def hello(name = "홍길동", age = 21):
    print("이름 : ", name)
    print("나이 : ", age)

hello()
hello("강감찬")
hello("김유신", 31)
#가변 매개변수
def total(*nums):
    tot = 0
    for n in nums:
        tot += n
    return tot
print(total(1))
print(total(1, 2, 4, 6, 7, 8, 11))
#하나 이상의 리턴값
def sum_and_multi(num1, num2):
    y1 = num1 + num2
    y2 = num1 * num2

    return y1, y2
rs1, rs2 = sum_and_multi(1, 2)
rs3, rs4 = sum_and_multi(3, 4)

print(rs1, rs2, rs3, rs4)
#변수에 저장하는 함수
def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

cals = [plus, minus]
res3 = cals[0](3, 4)
res4 = cals[1](4, 5)

print(res3, res4)

#람다함수
lam_plus = lambda x, y: x+ y

print(lam_plus(2, 3))
