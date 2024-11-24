# TODO Написать свою реализацию функции для подсчёта числа вхождение элементов в список
def my_count(lst: list, item) -> int:

    count = 0
    for element in lst:
        if element == item:
            count += 1
    return count

example_list = [1, 2, 3, 1, 2, 1, 4]
item_to_count = 1
result = my_count(example_list, item_to_count)
print(f"Элемент {item_to_count} встречается {result} раз(а).")