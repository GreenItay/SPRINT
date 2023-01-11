from typing import List, Tuple

import networkx as nx

import infinite_weight
from algorithmics.enemy.enemy import Enemy
from algorithmics.utils.coordinate import Coordinate
from algorithmics.enemy.radar import Radar

# Navigator


def calculate_path(source: Coordinate, targets: List[Coordinate], enemies: List[Enemy], allowed_detection: float = 0) \
        -> Tuple[List[Coordinate], nx.Graph]:
    """Calculates a path from source to target without any detection

    Note: The path must start at the source coordinate and end at the target coordinate!

    :param source: source coordinate of the spaceship
    :param targets: target coordinate of the spaceship
    :param enemies: list of enemies along the way
    :param allowed_detection: maximum allowed distance of radar detection
    :return: list of calculated path waypoints and the graph constructed
    """
    print('navigator running')



    for enemy in enemies:
        if isinstance(enemy, Radar):
            print('radar')
            g = infinite_weight.create_radar_graph(source, targets[0], enemy)
            print(g.nodes)


    print('printing nodes')
    print(g.nodes)
    print(g)
    return [source] + targets, g
