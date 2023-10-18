# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

# Declarative style
def sort_list_declarative(numbers):
    numbers.sort(reverse=True)


print(f"Declarative style -> {sort_list_declarative([41, 6, 2, 7, -3, 2, 8, 56])}")
