# Граф невзвешенный и неориентированный: узлы — почтовые отделения, рёбра — существующие связи 
#(двунаправленные). Спонсору нужно, чтобы из узла s можно было добраться до всех остальных узлов.
# Это равносильно требованию, чтобы все вершины лежали в одной компоненте связности с s.
from collections import deque

# Считываем исходные данные
n, s, k = map(int, input().split())

# Строим список смежности (граф)
adj = [[] for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# Массив для отметки посещённых вершин
visited = [False] * (n + 1)

# Счётчик компонент связности
components = 0

# Обход в ширину (BFS)
for v in range(1, n + 1):
    if not visited[v]:
        components += 1
        queue = deque([v])
        visited[v] = True
        while queue:
            u = queue.popleft()
            for w in adj[u]:
                if not visited[w]:
                    visited[w] = True
                    queue.append(w)

# Минимальное количество новых связей = (число компонент - 1)
print(components - 1)