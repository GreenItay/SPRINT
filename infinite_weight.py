import networkx as nx
import typing

from algorithmics.utils.coordinate import Coordinate
from algorithmics.enemy.radar import Radar
from algorithmics.enemy.enemy import Enemy

def create_radar_graph(source: Coordinate, target :Coordinate, radar: Radar):
    """
    :param: source - Coordinate of beginning on the radar
    :param: target - Coordinate inside the radar or on edge
    :param: radar - Radar object
    :return: g - nx.Graph object with legal lines between neighbors inside the grid
    """
    points_density = 0.3
    radius = radar.radius
    points_in_side = int(radar.radius * points_density) + 2
    grid = [[0 for i in range(points_in_side)] for j in range(points_in_side)]
    center_of_radar: Coordinate = radar.center
    start_of_grid: Coordinate = Coordinate(center_of_radar.x - radius, center_of_radar.y - radius)
    division_ratio = 2 / points_density

    g = nx.Graph()

    points_in_side = int(radar.radius * points_density) + 2
    for i in range(points_in_side):
        for j in range(points_in_side):
            grid[i][j] = Coordinate(start_of_grid.x + i * division_ratio, start_of_grid.y + j * division_ratio)
            #g.add_node(grid[i][j], pos=(grid[i][j].x, grid[i][j].y))

    source_indices = find_closest_coord_on_grid(grid, source)
    print(source_indices)
    grid[source_indices[0]][source_indices[1]] = source

    target_indices = find_closest_coord_on_grid(grid, target)
    grid[target_indices[0]][target_indices[1]] = target

    for i in range(points_in_side):
        for j in range(points_in_side):
            g.add_node(grid[i][j], pos=(grid[i][j].x, grid[i][j].y))

    for i in range(points_in_side):
        for j in range(points_in_side):
            get_edges_to_neighbors(i, j, 7, grid, g, [radar])


    #g.add_edge(source, target)
    return g

def find_closest_coord_on_grid(grid, coord1):
    shortest_dist = coord1.distance_to(grid[0][0])
    closest_coord = Coordinate(0,0)
    closest_index = (0,0)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if coord1.distance_to(grid[i][j]) < shortest_dist:
                closest_coord = grid[i][j]
                closest_index = (i,j)
                shortest_dist = coord1.distance_to(grid[i][j])
    return closest_index


def optimal_path_in_radar(g: nx.Graph, source: Coordinate, target: Coordinate):
    return nx.shortest_path(g, source, target, 'dist')

def add_edges_to_g(g, grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            ...

def get_edges_to_neighbors(i, j, distance, grid, g, enemies):
    """return a list - edges"""
    current = grid[i][j]
    for neighbor in find_neighbors(grid, i, j, distance):
        # print(neighbor)
        #print(current.distance_to(neighbor))
        if is_legal_line(current, neighbor, enemies):
            g.add_edge(current, neighbor, dist=current.distance_to(neighbor))

def find_neighbors(grid, _i, _j, distance) -> list[Coordinate]:
    neighbors = []

    for i in range(_i, _i + distance + 1): # out of bounds
        for j in range(_j - distance, _j + distance + 1):
            if i != _i or j != _j:
                if(0<= i < len(grid) and 0<= j < len(grid[0])):
                    neighbors.append(grid[i][j])
                    #print(grid[i][j])
    if(_i == 0 and _j == 5):
        print(neighbors)
    return neighbors

def is_legal_line(n1: Coordinate, n2: Coordinate, enemies: list[Enemy]):
    for enemy in enemies:
        if isinstance(enemies[0], Radar):
            radar: Radar = enemy

            line = n2 - n1
            rad1 = radar.center - n1
            cos1 = Coordinate.dot(line, rad1) / (line.norm() * rad1.norm())
            rad2 = radar.center - n2
            cos2 = Coordinate.dot(line, rad2) / (line.norm() * rad2.norm())

            if abs(cos1) > 0.7 or abs(cos2) > 0.7:  # 45 < angle < 135
                return False

    return True


def find_location_of_point_on_grid(c: Coordinate):
    ...

