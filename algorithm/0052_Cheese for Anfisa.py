import math
import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)
A = float(data[0])
B = float(data[1])
Z_deg = float(data[2])

# константы
L = A * math.sqrt(2)       # длина диагонали основания
EPS = 1e-12

# специальные случаи
if abs(Z_deg) < EPS:
    S = (A * A) / 2.0
elif abs(Z_deg - 90.0) < 1e-9:
    # вертикальная плоскость: прямоугольник диагональ x высота
    S = L * B
else:
    Z = math.radians(Z_deg)
    tanZ = math.tan(Z)
    cosZ = math.cos(Z)
    # h = B / tanZ  (максимальный v, обеспечивающий w <= B)
    h = B / tanZ

    half_peak = L / 2.0  # максимальное m(u)
    if h >= half_peak:
        Ap = (A * A) / 2.0
    else:
        Ap = h * L - h * h   # h*L - h^2

    S = Ap / cosZ

# вывод с точностью до 3 знаков
print(f"{S:.3f}")
