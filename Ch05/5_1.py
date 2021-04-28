#function 프로그래밍에서 인련의 로직 단위 정의. 호출로 이루어짐

def f(x):
    y = 2 * x + 3
    return y

print(f(1))

#함수유형1 매개변수0 리턴값 0
def type1(x, y):
    z = x + y
    return z
#함수유형2 매개변수0 리턴값 X
def type2(items):
    total = 0
    for item in items:
        total += item

    print(total)

type2([1, 2, 3, 4, 5])
type2((2, 4, 6, 8, 10))
#함수유형3 매개변수X 리턴값 0

def type3():
    total = 0
    for i in range(11):
        total += i

    return total

print(type3())
#함수유형4 매개변수X 리턴값 X
def type4():
    print("type3 result :", type3())

type4()

def gugudan(a):
    print("{}단".format(a))
    for j in range(2, 10):
        print("{} * {} = {}".format(a, j, a*j))

gugudan(2)
gugudan(3)
gugudan(7)