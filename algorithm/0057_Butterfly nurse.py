import math

# Ввод данных
x1, y1 = map(int, input().split())
x2, y2, z2 = map(int, input().split())

# Расстояние между оберткой и бабочкой
f = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + z2**2)

# Оптическая сила
D = 1 / f

# Вывод с округлением до 3 знаков
print(f"{D:.3f}")
