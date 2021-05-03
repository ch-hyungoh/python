"""# try - except
num1, num2 = 1, 0
r1=r2=r3=r4 = 0
try:
    # 에러가 발생할 가능성이 있는 코드 영역
    r1 = num1 + num2
    r2 = num1 - num2
    r3 = num1 * num2
    r4 = num1 / num2
except:
    # 에러가 발생했을때 처리할 코드영역
    print("예외 발생....")
print(r1)
print(r2)
print(r3)
print(r4)
"""
# try ~ except ~ finally
people = ["김유신", "김춘추", "장보고"]

try:
    # 예외가 발생할 가능성이 있는 코드
    for i in range(4):
        print(people[i])
except:
    # 예외 코드
    print("유효하지 않은 인덱스 참조")
finally:
    # 예외 발생 여부 상관없이 마지막 코드
    print("예외처리 완료......")

# try ~ except ~ else

print("프로그램 종료")

animal = ["사자", "코끼리", "기린", "호랑이"]
result = None
while True:
    try:
        # 예외가 발생할 가능성이 있는 코드
        print("동물을 선택해보세요")
        print("1:사자, 2:코끼리, 3:기린, 4:호랑이, 0:종료")

        answer = int(input("선택 : "))

        if answer == 0:
            print("종료합니다")
            break
        elif answer < 0:
            raise Exception("음수는 안됩니다.")

        result = animal[answer - 1]
    except Exception as e:
        # 예외 코드
        print("어러내용 :", e)
        print("청확시 0~4 사이에 숫자를 입력하시오")
    else:
        #예외가 발생 안했을때 실행되는 코드 영역
        print("선택한 동물은 "+result+"입니다")