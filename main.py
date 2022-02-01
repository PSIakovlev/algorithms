from math import factorial
list_points = [[0, 2],
               [2, 5],
               [5, 2],
               [6, 6],
               [8, 3]]
list_paths = []
n = len(list_points)
factorial_n = int(factorial(n - 1))


def make_paths(step=1):
    """
    Рекурсивная функция создаёт список уникальных путей
    """
    iteration = 0
    while iteration < factorial_n:
        for point in list_points[1:]:
            for j in range(int(factorial(n - step) / (n - step))):
                if iteration != 24:
                    if not (point in list_paths[iteration]):
                        list_paths[iteration].append(point)
                        iteration += 1
    if step != n - 1:
        return make_paths(step + 1)


# Добавление первой точки в список путей
for i in range(factorial_n):
    list_paths.append([])
    list_paths[i].append(list_points[0])

make_paths()

# Добавление последней точки в список путей
for i in range(factorial_n):
    list_paths[i].append(list_points[0])

# Блок поиска кратчейшего маршрута
i = 0
min_i = 0
min_length = 0
for path in list_paths:
    length_path = 0
    current_point = path[0]
    for x, y in path[1:]:
        res = ((current_point[0] - x) ** 2 + (current_point[1] - y) ** 2) ** 0.5
        length_path += res
        current_point = [x, y]
    if min_length != 0:
        if min_length > length_path:
            min_length = length_path
            min_i = i
    else:
        min_length = length_path
        min_i = i
    i += 1

# Вывод точек и расстояний кратчайшего пути
current_point = list_paths[min_i][0]
length_path = 0
for x, y in list_paths[min_i][1:]:
    res = ((current_point[0] - x) ** 2 + (current_point[1] - y) ** 2) ** 0.5
    length_path += res
    print(f'{current_point} - > {[x, y]}, расстояние между точками = {res}, пройденное расстояние = {length_path}')
    current_point = [x, y]
