def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")  # убираем пробелы и разницу регистров
    return s == s[::-1]


def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Только неотрицательные числа!")
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def max_of_three(a: int, b: int, c: int) -> int:
    return max(a, b, c)


def sum_list(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        total += num
    return total
