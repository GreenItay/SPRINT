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
            g.add_node(grid[i][j], pos=(grid[i][j].x, grid[i][j].y))
    for i in range(points_in_side):
        for j in range(points_in_side):
            get_edges_to_neighbors(i, j, 2, grid, g)
            #g.add_edge(grid[i][j], grid[i][j])

    g.add_edge(source, target)
    return g 

def optimal_path_in_radar(g: nx.Graph, source: Coordinate, target: Coordinate):
    return nx.shortest_path(g, source, target, 'dist')

def add_edges_to_g(g, grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            ...

def get_edges_to_neighbors(i, j, distance, grid, g):
    """return a list - edges"""
    current = grid[i][j]
    for neighbor in find_neighbors(grid, i, j, distance):
        #print(neighbor)
        print(current.distance_to(neighbor))
        g.add_edge(current, neighbor, dist=current.distance_to(neighbor))

def find_neighbors(grid, _i, _j, distance) -> list[Coordinate]:
    neighbors = []

    for i in range(_i, _i + distance + 1): # out of bounds
        for j in range(_j, _j + distance + 1):
            if i != _i or j != _j:
                if(i < len(grid) and j < len(grid[0])):
                    neighbors.append(grid[i][j])
                    print(grid[i][j])
    return neighbors


def is_legal_line(n1: Coordinate, n2: Coordinate, enemies: list[Enemy]):
    radar = enemies[0]

    return True

def find_location_of_point_on_grid(c: Coordinate):
    ...

