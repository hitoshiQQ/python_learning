import math_utils
import string_tools


def main():
    print("=== Демонстрация math_utils ===")
    print("Факториал 5:", math_utils.factorial(5))
    print("Максимум из (3, 9, 7):", math_utils.max_of_three(3, 9, 7))
    print("Сумма списка [1, 2, 3, 4, 5]:",
          math_utils.sum_list([1, 2, 3, 4, 5]))
    print("Палиндром 'шалаш':",
          math_utils.is_palindrome("шалаш"))

    print("\n=== Демонстрация string_tools ===")
    print("Удаляем гласные из 'программирование':",
          string_tools.remove("программирование"))


if __name__ == "__main__":
    main()
