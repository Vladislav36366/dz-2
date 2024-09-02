numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
print('До конца списка')
while len(numbers) > a:
    if numbers[a] > 0:
       print(numbers[a])
       a += 1
    else:
        a += 1
print('до первого отрицательного числа')
numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while len(numbers) > a:
    if numbers[a] > 0:
       print(numbers[a])
       a += 1
       if numbers[a] == 0:
           a += 1
    else:
        break