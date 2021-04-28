num1, num2 = 1, 2

if num1 > 0:
    print("num1은 0보다 크다")
else:
    print("num1은 0보다 작다")

if num1 >num2:
    print("num1은 num2보다 크다")

if num1 >0:
    if num2 > 1:
        print("num1은 0보다 크고 num2는 1보다 크다")

if num1 >0 and num2 > 1:
    print("num1은 0보다 크고 num2는 1보다 크다")

num3, num4 = 3, 4

if num3 >num4:
    print("num3은 num4보다 크다")
else:
    print("num4은 num3보다 크다")

if num1 >num2:
    print("num1은 num2보다 크다")
elif num2 >num3:
    print("num2은 num3보다 크다")
elif num3 >num4:
    print("num3은 num4보다 크다")
else:
    print("num4가 가장 크다")

num = 3

result = num * 2 if num >=5 else num +2

print(result)

score = int(input("점수입력하시오"))

if score>90:
    print("A입니다")
elif score>80:
    print("B입니다")
elif score>70:
    print("C입니다")
elif score>60:
    print("D입니다")
else:
    print("E입니다")