a = float(input("Введите первое число: "))
op = input("Введите операцию (+, -, *, /): ")
b = float(input("Введите второе число: "))

if op == "+":
    print("Результат:", a + b)
elif op == "-":
    print("Результат:", a - b)
elif op == "*":
    print("Результат:", a * b)
elif op == "/":
    if b != 0:
        print("Результат:", a / b)
    else:
        print("Ошибка: Деление на ноль!")
else:
    print("Неизвестная операция!")
