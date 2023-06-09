#Поспелов Максим Васильевич БПИ-20-01 Задание 5

import time

# начало счета времени алгоритма
start = time.time()

# чтение из файла
with open('input.txt', 'r') as f:
    n = int(f.readline())

# создание списка чисел от 2 до n
numbers = list(range(2, n+1))

# отметка всех кратных чисел
for i in range(2, int(n**0.5)+1):
    if i in numbers:
        for j in range(i*i, n+1, i):
            if j in numbers:
                numbers.remove(j)

# запись простых чисел в файл
with open('output.txt', 'w') as f:
    f.write(', '.join(map(str, numbers)))

# вывод времени в консоль
    end = time.time() - start
    print(end)