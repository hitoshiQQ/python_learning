from math import gcd

def lcm(a, b):
    return a // gcd(a, b) * b

# Чтение входных данных
k, n, m, d = map(int, input().split())

# Находим общий знаменатель (НОК)
a = lcm(k, lcm(n, m))

# Считаем t = a/k + a/n + a/m
t = a // k + a // n + a // m

# Знаменатель формулы
den = a - t

# Проверка условий существования решения
if den <= 0:
    print(-1)
else:
    num = d * a
    if num % den != 0:
        print(-1)
    else:
        s = num // den
        print(s)