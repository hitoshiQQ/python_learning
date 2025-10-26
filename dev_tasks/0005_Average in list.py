def average (l):
    # Проверка на пустой список
    if not l:
        raise ValueError("Список пуст!")
    
    # Проверка на числа
    if not all(isinstance(x, (int, float)) for x in l):
        raise TypeError("Не все элементы списка являются числами!")
    
    # Вычисление среднего числа
    return sum(l) / len(l)

num = [10, 20, 30, 40, 50]
print("Среднее: ", average(num))