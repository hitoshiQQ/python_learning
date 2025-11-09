import math


def compute_gcd(a: int, b: int) -> int:
    """Вычисляет наибольший общий делитель двух чисел."""
    return math.gcd(a, b)


def reflections_and_pocket(M: int, N: int):
    """
    Возвращает количество отражений и номер лузы.
    Нумерация луз:
      1 — верхняя левая,
      2 — верхняя правая,
      3 — нижняя правая,
      4 — нижняя левая.
    """
    g = compute_gcd(M, N)
    p = N // g
    q = M // g
    reflections = p + q - 2

    if p % 2 == 1 and q % 2 == 0:
        pocket = 2
    elif p % 2 == 1 and q % 2 == 1:
        pocket = 3
    elif p % 2 == 0 and q % 2 == 1:
        pocket = 4
    else:
        pocket = 1

    return reflections, pocket


# --- Ввод и вывод ---
M, N = map(int, input().split())
R, pocket = reflections_and_pocket(M, N)
print(R, pocket)
