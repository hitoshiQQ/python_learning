def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Только неотрицательные числа!")
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
