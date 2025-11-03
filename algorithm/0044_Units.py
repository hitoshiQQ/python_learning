n = int(input())
if n == 1:
    print(1)
    exit()

# Предвычислим делители >=2 для каждого числа
divs = [[] for _ in range(n + 1)]
for a in range(2, n + 1):
    for j in range(a, n + 1, a):
        divs[j].append(a)

INF = 10**9
dp = [INF] * (n + 1)
dp[0] = 0
dp[1] = 1

# buckets[v] = список чисел a, таких что dp[a] == v
# (хранятся в порядке возрастания a)
# максимальный возможный dp не больше n, поэтому размер n+1
buckets = [[] for _ in range(n + 1)]
buckets[1].append(1)

for x in range(2, n + 1):
    # верхняя граница: x единиц
    best = x

    # попробуем факторизации (a * b)
    for a in divs[x]:
        b = x // a
        val = dp[a] + dp[b]
        if val < best:
            best = val

    # теперь разложения на сумму, но перебираем только "полезные" a:
    # перебираем по возрастанию значений dp[a] (v),
    #  и внутри каждого бакета — по a (по возрастанию)
    half = x // 2
    # dp значение, до которого имеет смысл перебирать:
    # только v < best, т.к. dp[a] >= best не даст улучшения
    v = 1
    while v < best:
        for a in buckets[v]:
            if a > half:
                # бакеты в порядке возрастания a, значит дальше все a > half
                break
            b = x - a
            val = v + dp[b]  # dp[a] == v
            if val < best:
                best = val
        else:
            # выполнится если внутренний цикл не прервался по break,
            # тогда идём к следующему v
            v += 1
            continue
        # если внутренний цикл прервался по break (a > half),
        # нет смысла смотреть большие v
        break

    dp[x] = best
    # добавим x в соответствующий бакет
    if best <= n:
        buckets[best].append(x)

print(dp[n])
