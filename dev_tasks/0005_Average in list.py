def average(Any):
    # Проверка на пустой список
    if not Any:
        raise ValueError("Список пуст!")
    # Проверка на числа
    if not all(isinstance(x, (int, float)) for x in Any):
        raise TypeError("Не все элементы списка являются числами!")
    # Вычисление среднего числа
    return sum(Any) / len(Any)


num = [10, 20, 30, 40, 50]
print("Среднее: ", average(num))
