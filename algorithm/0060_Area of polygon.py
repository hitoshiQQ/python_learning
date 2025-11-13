n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

s = 0
for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % n]
    s += x1 * y2 - x2 * y1

area = abs(s) / 2
print(f"{area:.3f}")
