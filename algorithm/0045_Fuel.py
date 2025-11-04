import heapq


def min_transfer_time(N, M, B, C, A, pipes):
    # граф в 0-based
    adj = [[] for _ in range(N)]
    for u, v, L in pipes:
        u -= 1
        v -= 1
        adj[u].append((v, L))
        adj[v].append((u, L))

    # находим первую дефицитную котельную
    deficit_nodes = [i for i in range(N) if A[i] < B]
    if not deficit_nodes:
        return 0
    t = deficit_nodes[0]
    D = B - A[t]

    # Dijkstra от t
    INF = 10**9
    dist = [INF]*N
    dist[t] = 0
    pq = [(0, t)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    # собираем источники (избыток)
    supplies = []
    total_supply = 0
    for i in range(N):
        if i == t:
            continue
        s = max(0, A[i] - B)
        if s > 0:
            supplies.append((dist[i], s))
            total_supply += s

    if total_supply < D:
        return -1  # по условию не должно происходить

    supplies.sort(key=lambda x: x[0])
    remain = D
    total_dist_tons = 0
    for d, s in supplies:
        if d >= INF:
            continue
        take = min(s, remain)
        total_dist_tons += take * d
        remain -= take
        if remain == 0:
            break

    return total_dist_tons * C


# ---------- безопасное чтение входа в виде списка токенов ----------
tokens = []
try:
    while True:
        line = input()
        # пропускаем пустые строки, но не зависаем на них
        if line is None:
            break
        parts = line.strip().split()
        if parts:
            tokens.extend(parts)
except EOFError:
    # конец входа — это нормально, обработаем имеющиеся токены
    pass

# если токенов совсем мало — завершаем (никаких исключений)
if len(tokens) < 4:
    # недостаточно данных для даже N M B C
    # можно ничего не печатать или вывести ошибку; выберем пустой выход
    raise SystemExit

it = iter(tokens)
try:
    N = int(next(it))
    M = int(next(it))
    B = int(next(it))
    C = int(next(it))
except StopIteration:
    raise SystemExit

# читаем A (N чисел). Если их меньше — завершаем аккуратно.
A = []
for _ in range(N):
    try:
        A.append(int(next(it)))
    except StopIteration:
        # недостаточно чисел в A — завершаем
        raise SystemExit

# читаем M троек (u, v, L). Если их меньше — берём столько, сколько есть.
pipes = []
for _ in range(M):
    try:
        u = int(next(it))
        v = int(next(it))
        L = int(next(it))
    except StopIteration:
        # вход закончился раньше, чем ожидалось — прекращаем чтение труб
        break
    pipes.append((u, v, L))

# Если меньше M строк было поставлено, это означает неполный ввод.
# В таком случае можно либо считать,
#  что остальные труб отсутствуют, либо завершить.
# Здесь мы считаем имеющиеся pipes как есть и продолжаем.
# Запускаем подсчёт и выводим результат (если возможен)
res = min_transfer_time(N, M, B, C, A, pipes)
print(res)
