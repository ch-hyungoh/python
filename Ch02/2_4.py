str1 = "hello"
str2 = "python"
str3 = str1 + str2
print(str3)

name = "홍길동"
print(name*3)

msg = "hello world"
print(len(msg))

print(msg[0])
print(msg[6])
print(msg[-1])
print(msg[-5])

print(msg[0:5])
print(msg[:5])
print(msg[6:10])
print(msg[6:])

people = "김유신|김춘추|장보고|강감찬|이순신"

p1, p2, p3, p4, p5 = people.split("|")

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

print("서울\n대전\n대구\n부산\n광주")
print("서울\t대전\t대구\t부산\t광주")
print("저는 '홍길동'입니다")