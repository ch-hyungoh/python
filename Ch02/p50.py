oneLine = "this is one line string"
print(oneLine)
print("문자열 길이 : ", len(oneLine))
print(oneLine[0:4])
print(oneLine[:4])
print(oneLine[:])
print(oneLine[::2]) #2의 배수

print(oneLine[0:-1:2])
print(oneLine[-6:2])
print(oneLine[-6:])

subString = oneLine[-11:]
print(subString)