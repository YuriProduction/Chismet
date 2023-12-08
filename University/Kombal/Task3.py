from heapq import heappop, heappush


def dijkstra(graph, start, end):
    queue = [(0, start, [], None)]
    final_doors = []
    visited = set()
    while queue:
        (cost, current, path, door_number) = heappop(queue)
        if current not in visited:
            visited.add(current)
            path = path + [current]
            if door_number is not None:
                final_doors.append(door_number)
            if current == end:
                return (cost, path, final_doors)
            for (next_node, edge_cost, door_number) in graph[current]:
                if next_node not in visited:
                    heappush(queue, (cost + edge_cost, next_node, path, door_number))
    return float('inf')


# граф представляет собой словарь, где ключи - это вершины, а значения - списки кортежей,
# представляющих соседние вершины и стоимость перехода к ним
# graph = {
#     1: [(2, 1), (3, 2)],
#     2: [(1, 1), (3, 2), (4, 3)],
#     3: [(1, 2), (2, 2), (4, 1)],
#     4: [(2, 3), (3, 1)]
# }

# print(dijkstra(graph, 1, 4))

with open('in.txt', 'r') as f:
    input_data = list(map(int, f.readline().split(' ')))
    N = input_data[0]
    M = input_data[1]
    standed_up_in = input_data[2]
    balance = input_data[3]
    doors = {}
    for i in range(N):
        info_room = list(map(int, f.readline().split(' ')))
        count_doors_in_room = info_room[0]
        info_room = info_room[1:]
        for j in range(count_doors_in_room):
            if info_room[j] not in doors:
                doors[info_room[j]] = []
                doors[info_room[j]].append(i + 1)
            else:
                doors[info_room[j]].append(i + 1)

    line = f.readline()
    string = line
    while line:
        line = f.readline()
        string += line
    string = string.replace('\n', ' ').rstrip()
    cost_doors_arr = list(map(int, string.split(' ')))
    cost_doors_dict = {}
    for i in range(M):
        cost_doors_dict[i + 1] = cost_doors_arr[i]

graph = {}
graph['Exit'] = None
for key, value in doors.items():
    if len(value) == 1:  # значит это выход
        if value[0] not in graph:
            graph[value[0]] = []
        graph[value[0]].append(['Exit', cost_doors_dict[key], key])
    else:
        if value[0] not in graph:
            graph[value[0]] = []
        if value[1] not in graph:
            graph[value[1]] = []
        graph[value[0]].append([value[1], cost_doors_dict[key], key])
        graph[value[1]].append([value[0], cost_doors_dict[key], key])

res = dijkstra(graph, standed_up_in, 'Exit')
f = open('out.txt', 'w')
if res == 'inf':
    f.write('N')
else:
    mn = int(res[0])
    if mn > balance:
        f.write('N')
    else:
        f.write('Y\n')
        f.write(str(mn) + '\n')
        for door in res[2]:
            f.write(str(door) + ' ')

f.close()
