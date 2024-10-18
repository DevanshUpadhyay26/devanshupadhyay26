def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list




list=[10,12,2,3,4,5]
print(bubbleSort(list))



def sum(num: int, num2: int) -> int:
    return num+num2
res = sum(1,2)
print (res)


