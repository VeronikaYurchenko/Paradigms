# Задача №1
# Условие На вход подается число n. ● Задача Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n. Обоснуйте выбор парадигм. ● Пример вывода: 1 * 1 = 1 1 * 2 = 2 1 * 3 = 3 1 * 4 = 4 1 * 5 = 5 1 * 6 = 6 .. 1 * 9 = 9

MIN_LIMIT = 1
MAX_lIMIT = 11
HALF = 2

for i in range(MIN_LIMIT, MAX_lIMIT):
    for j in range(MIN_LIMIT, MAX_lIMIT // HALF + 1):
        print(f"{j:>2} x {i:>2} = {i * j:>2}", end='\t')
    print()
print()
for i in range(MIN_LIMIT, MAX_lIMIT):
    for j in range(MAX_lIMIT // HALF + 1, MAX_lIMIT):
        print(f'{j:>2} x {i:>2} = {i * j:>2}', end='\t')
    print()

