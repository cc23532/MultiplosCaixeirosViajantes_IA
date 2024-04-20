import random
import math

def calculate_euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distance)


def generate_distance_matrix(*points):
    num_points = len(points)
    distance_matrix = [[0] * num_points for _ in range(num_points)]
    for i in range(num_points):
        for j in range(i+1, num_points):
            distance = calculate_euclidean_distance(points[i], points[j])
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance
    return distance_matrix


def get_total_distance(tour, distances):
    total_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_distance += distances[city1][city2]
    total_distance += distances[tour[-1]][tour[0]]
    return total_distance


def initialize_routes(num_salesmen, distances, max_cities_by_route):
    n_cities = len(distances)
    unvisited = list(range(1, n_cities))
    random.shuffle(unvisited)
    salesman_routes = [[] for _ in range(num_salesmen)]
    
    for i in range(num_salesmen):
        salesman_routes[i].append(0)
    
    for i in range(n_cities - 1):
        for j in range(num_salesmen):
            if len(salesman_routes[j]) < max_cities_by_route:
                salesman_routes[j].append(unvisited[i])
                break
                
    for i in range(num_salesmen):
        if 0 not in salesman_routes[i]:
            salesman_routes[i].append(0)

    routes_with_distance = []
    for route in salesman_routes:
        total_distance = get_total_distance(route, distances)
        routes_with_distance.append((route, total_distance))
    
    return routes_with_distance


def adjust_routes(salesman_routes, distances, max_cities_by_route):
    num_salesmen = len(salesman_routes)
    min_distance_salesman = min(range(num_salesmen), key=lambda i: salesman_routes[i][1])
    max_distance_salesman = max(range(num_salesmen), key=lambda i: salesman_routes[i][1])
    farthest_city = max(salesman_routes[min_distance_salesman][0], key=lambda city: distances[city][salesman_routes[max_distance_salesman][0][0]])
    target_salesman = min(range(num_salesmen), key=lambda i: distances[farthest_city][salesman_routes[i][0][0]])
    
    if len(salesman_routes[min_distance_salesman][0]) < max_cities_by_route:
        new_route = list(salesman_routes[target_salesman][0])
        new_route.insert(-1, farthest_city)
        salesman_routes[min_distance_salesman][0].remove(farthest_city)
        
        new_total_distance = get_total_distance(new_route, distances)
        salesman_routes[target_salesman] = (new_route, new_total_distance)
        
    for i, (route, _) in enumerate(salesman_routes):
        salesman_routes[i] = (route, get_total_distance(route, distances))

    return salesman_routes

points = [(500, 500), (891, 373), (70, 208), (241, 823), (172, 503), (253, 214), (81, 673), (103, 274), (453, 299), (753, 382), (811, 961), (543, 780), (835, 538), (430, 783), (16, 818), (907, 630), (264, 880), (935, 236), (56, 713), (856, 253), (49, 282), (256, 309), (105, 916), (813, 489), (584, 416), (935, 387), (430, 589), (478, 105), (832, 987), (78, 707), (764, 141), (498, 458), (991, 417), (856, 637), (964, 876), (542, 918), (989, 870), (796, 551), (411, 717), (753, 683), (529, 447), (787, 612), (153, 218), (598, 356), (338, 58), (727, 12), (383, 258), (497, 899), (941, 290), (113, 238), (652, 681), (596, 257), (8, 171), (924, 315), (944, 728), (367, 833), (864, 883), (281, 582), (758, 33), (244, 472), (629, 295), (387, 696), (813, 654), (128, 866), (343, 136), (554, 699), (909, 666), (396, 288), (961, 959), (614, 318), (698, 374), (552, 982), (919, 359), (118, 239), (858, 500), (636, 568), (222, 141), (796, 524), (960, 157), (84, 48), (158, 966), (206, 266), (716, 441), (235, 465), (456, 147), (447, 479)]
distances = generate_distance_matrix(*points)
n_cities = len(distances)

num_salesmen = 5
max_cities_by_route = 17

salesman_routes = initialize_routes(num_salesmen, distances, max_cities_by_route)
print("Rotas iniciais:")
for route, total_distance in salesman_routes:
    print(f"Rota: {route}, Distância Total: {total_distance}")

salesman_routes = adjust_routes(salesman_routes, distances, max_cities_by_route)
print("\nRotas ajustadas:")
for route, total_distance in salesman_routes:
    print(f"Rota: {route}, Distância Total: {total_distance}")
