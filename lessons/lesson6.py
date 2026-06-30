#Линейная сложность 

def o_n(my_list, target):
    for i in my_list:
        if i == target:
            return i
    return 0
    
   
o_n([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4)

#Бинарная сложность

def o_logN(my_list, target):
    left = 0
    right = len(my_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if my_list[mid] == target:
            return target
        elif my_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "Не найдено"


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(o_n(my_list, 4))       # 4
print(o_logN(my_list, 4))    # 4
print(o_logN(my_list, 99))   

    
    