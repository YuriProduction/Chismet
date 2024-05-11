f = open('in.txt', 'r')
n = int(f.readline())
sets = []
for i in range(n):
    set_elements = list(map(int, f.readline().split()[:-1]))  # Исключаем завершающий 0
    sets.append((set_elements, i))
f.close()
sets.sort(key=lambda x: len(x[0]))
result_set = set()
answer = []
flag = True
for pair in sets:
    additional = 0
    for elem in pair[0]:
        if elem not in result_set:
            result_set.add(elem)
            answer.append((elem, pair[1]))
            break
        additional += 1
    if additional == len(pair[0]):
        flag = False

if not flag:
    with open('out.txt', 'w') as f:
        f.write("N")

else:
    answer.sort(key=lambda x: x[1])
    with open('out.txt', 'w') as f:
        f.write("Y\n")
        for pair in answer:
            f.write(str(pair[0]) + ' ')
