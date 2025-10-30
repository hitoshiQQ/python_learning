from datetime import date

# Считываем количество смен
k = int(input())

# Множество для хранения уникальных дат "Пятница 13"
friday_13_set = set()

# Перебираем все смены
for _ in range(k):
    a, b = map(int, input().split())  # начало и конец смены (года)
    for year in range(a, b + 1):
        for month in range(1, 13):  # все месяцы
            d = date(year, month, 13)
            # weekday(): 0=понедельник, ..., 4=пятница
            if d.weekday() == 4:
                friday_13_set.add(d)

# Выводим количество уникальных дней, когда была "Пятница 13"
print(len(friday_13_set))