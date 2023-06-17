import random

# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# list_1 = []
# n = int(input('Print a length for list: '))
# a = [0]*n
# a[0] = int(input('Print a first element of progression: '))
# d = int(input('Print a difference for progression: '))

# print(a[0], end='\n')

# for i in range(1,n):
#     a[i] = a[i-1] + d
#     print(a[i], end='\n')


# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума 
# и не больше заданного максимума)

n = int(input('Print a lenght for list: '))

def create_list(n):
    list = []
    for i in range(n):
        list.append(random.randint(1,20))
    return list
list_1 = create_list(n)
print(list_1)

minvalue = int(input('Print a min value: '))
maxvalue = int(input('Print a max value: '))


def findelems(list_1):
    list_indexes = []
    for i in range(len(list_1)):
        if list_1[i] >= minvalue and list_1[i] <= maxvalue:
            list_indexes.append(i)
        i+=1
    return list_indexes
    
indexes = findelems(list_1)

print(f'The indexes of correct elements is:{indexes}')

                   

    