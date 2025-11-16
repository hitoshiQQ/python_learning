# Запись в файл
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!")

# Чтение файла
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
