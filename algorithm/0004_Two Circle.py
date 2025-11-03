import math

x1, y1, r1, x2, y2, r2 = map(float, input().split())

# Расстояние между центрами
d = math.hypot(x2 - x1, y2 - y1)

# Если центры окружности совпадают
if d == 0:
    print(-1 if r1 == r2 else 0)
    # Если центры разнесены на расстояние больше суммы радиусов
elif d > r1 + r2 or d < abs(r1 - r2):
    print(0)
    # Если расстояние равно сумме или разности радиусов
elif d == r1 + r2 or d == abs(r1 - r2):
    print(1)
else:
    print(2)
