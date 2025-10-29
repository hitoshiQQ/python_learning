def is_prime(num):
    # Проверка, является ли число простым
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2

    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

# Основная программа
N, K = map(int, input().split())

# Если не найдем просто число
res = -1

# Проверяем все билеты после Вани
# s — количество пассажиров, которых Петя пропускает: 0..N-2
# Петя получит билет с номером K + (s+1)
for s in range(0, N - 1):
    ticket = K + (s + 1)
    if is_prime(ticket):
        res = s
        break

print(res)