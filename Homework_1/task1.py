# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

# Bubble sort (imperative style)
def sort_list_imperative(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return numbers


print(f"Imperative style -> {sort_list_imperative([41, 6, 2, 7, -3, 2, 8, 56])}")
