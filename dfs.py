from collections import defaultdict

def dfs(graph, start, end=None):
    """
    dfs    

    :param graph:
    :param start:
    :param end:
    :return:
    """
    if start not in graph or (end is not None and end not in graph):
        raise ValueError("Некорректные вершины")

    visited = set()
    stack = [(start, 0)]  # (vertex, distance)
    path_length = None

<<<<<<< HEAD
    # Добавьте | комментарии | в код программы
=======
    # Добавьте комментарии в код программы ++
>>>>>>> 06c42b7805393d0abac4679695a362b5c1b0d0e8
    while stack:
        vertex, distance = stack.pop()
        if vertex == end:
            path_length = distance
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, distance + 1))

    return list(visited), path_length


# Пример использования
edges = [(4, 2), (1, 3), (2, 4)]
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

print(dfs(graph, 1))  # Обход в глубину
print(dfs(graph, 2, 4))  # Длина пути от 2 до 4 -> 1
