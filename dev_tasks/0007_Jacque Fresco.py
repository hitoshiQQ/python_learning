with open('goats.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]

from collections import Counter

# Читаем файл
with open('goats.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file if line.strip()]

# Находим границы секций (без учета регистра)
idx_colors = next(i for i, line in enumerate(lines)
                  if line.upper() == 'COLOURS')
idx_goats = next(i for i, line in enumerate(lines)
                 if line.upper() == 'GOATS')

# Список козлов
goats = lines[idx_goats + 1:]

# Подсчёт количества каждого цвета
counts = Counter(goats)

# Общее количество козлов
total = len(goats)

# Цвета, которые составляют более 7%
threshold = 0.07 * total
result = sorted([color for color, cnt in counts.items() if cnt > threshold])

# Запись в answer.txt
with open('answer.txt', 'w', encoding='utf-8') as file:
    for color in result:
        file.write(color + '\n')
