class BipartiteGraph:
    def __init__(self, graph):
        self.graph = graph
        self.left = set()
        self.right = set()
        for u in graph:
            self.left.add(u)
            for v in graph[u]:
                self.right.add(v)

    def max_matching(self):
        matching = {}
        for u in self.left:
            visited = set()
            self.find_path(u, visited, matching)
        return matching

    def find_path(self, u, visited, matching):
        for v in self.graph[u]:
            if v not in visited:
                visited.add(v)
                if v not in matching or self.find_path(matching[v], visited, matching):
                    matching[v] = u
                    return True
        return False


graph = dict()
f = open('in.txt', 'r')
n = int(f.readline())
for i in range(n):
    set_elements = tuple(map(int, f.readline().split()[:-1]))  # Исключаем завершающий 0
    graph[(set_elements, i)] = list(set_elements)
f.close()

# Пример использования
bipartite_graph = BipartiteGraph(graph)
max_matching = bipartite_graph.max_matching()
sorted_max_mathing = dict(sorted(max_matching.items(), key=lambda item: item[1][1]))
with open('out.txt', 'w') as f:
    if len(sorted_max_mathing) != n:
        f.write("N")
    else:
        f.write("Y\n")
        for el in sorted_max_mathing:
            f.write(str(el) + ' ')
