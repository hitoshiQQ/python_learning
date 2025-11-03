# Получаем число на ввод
n = int(input())
# a, b, c - размеры целого прямоугольного параллелипеда
# a - длина
a = int((n ** (1 / 3)) + 0.5)
# b - ширина
b = int(((n / a) ** 0.5) + 0.5)
# c - высота
c = int(n / (a * b))
# Один слой
s1 = a * (b + 1) + b * (a + 1)
# Между слоями
s2 = (a + 1) * (b + 1)
# Всего спичек на целый прямоугольный параллелипипед
result = s1 * (c + 1) + s2 * c
# remainder - оставшиеся кубики
remainder = n - a * b * c

# Если кубы ещё остались
if remainder != 0:
    if n > 4:
        # d, e - размеры нового прямоугольного параллелипипеда
        d = int(remainder ** 0.5)
        e = int(remainder ** 0.5)
        # Подбираем оптимальные d, e
        last = (d, e)
        while d * e < remainder:
            last = (d, e)
            if d < e:
                d += 1
            else:
                e += 1
        d, e = last
        # К результату добавляем полученные спички
        result += d * (e + 1) + e * (d + 1) + (d + 1) * (e + 1)
        remainder -= d * e
        if remainder != 0:
            # Если кубики всё равно остались, то добавляем и их
            result += 3 * (remainder - 1) + 5
    else:
        result += 8
# Выводим результат
print(int(result))
