def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")  # убираем пробелы и разницу регистров
    return s == s[::-1]
