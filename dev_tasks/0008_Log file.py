# Вам доступен текстовый файл logfile.txt
# с информацией о времени входа пользователя в систему и выхода из нее.
# Каждая строка файла содержит три значения,
# разделенные запятыми и символом пробела: имя пользователя, время входа,
# время выхода, где время указано в 24-часовом формате.

# Напишите программу, которая создает файл output.txt
# и выводит в него имена всех пользователей (не меняя порядка следования),
# которые были в сети не менее часа.


def time_to_minutes(t):
    # Преобразование времени в минуты
    hours, min = map(int, t.split(':'))
    return hours * 60 + min


with open('logfile.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file if line.strip()]
result = []

for line in lines:
    name, log_in, log_out = [x.strip() for x in line.split(',')]
    duration = time_to_minutes(log_out) - time_to_minutes(log_in)
    if duration >= 60:
        result.append(name)

with open('output.txt', 'w', encoding='utf-8') as out_file:
    for name in result:
        out_file.write(name + '\n')
