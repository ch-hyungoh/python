dataset = [1, 4, 3]
print(dataset)

dataset.append(2)
dataset.append(5)
print(dataset)

dataset.sort()
print(dataset)

dataset.sort(reverse=True)
print(dataset)

dataset.insert(2, 6)
print(dataset)

dataset.remove(6)
print(dataset)


#map 함수 리스트 원소를 지정된 함수로 일괄 처리해 주는 함수
def plus10(n):
    return n+10

list1 = [1, 2, 3, 4, 5]
list1_map = map(plus10, list1)
print(list(list1_map))

list2 = [1.1, 2.2, 3.3, 4.4, 5.5]
list2_map_list = list(map(int, list2))
print(list2_map_list)

list3 = [1, 2, 3, 4, 5]
list3_map_list = list(map(lambda x:x*2, list3))
print((list3_map_list))

list4 = ["1", "2", "3", "4", "5"]
list4_map_list = list(map(int, list4))
print(list4_map_list)

a = input("입력 : ")
print(a)

var1, var2, var3 = map(int, input("3개 입력 :").split())
print(var1, var2, var3)
print(var1+var2+var3)