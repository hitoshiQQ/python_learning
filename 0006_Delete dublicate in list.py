def remove_dublicate(l):
    # Результирующий список
    result = []

    # Проходим по всему списку и добавляем уникальные элементы
    for item in l:
        if item not in result:
            result.append(item)

    return result
num = [1, 2, 3, 2, 4, 1, 5]
num = remove_dublicate(num)
print(num)