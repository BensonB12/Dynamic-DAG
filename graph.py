from __future__ import annotations
from typing import List
from pydantic import BaseModel


class Node(BaseModel):
    id: int
    points_to_nodes: List[Node] = []
    node_ids_that_point_to_me: List[int] = []


from typing import List, Dict

class Graph:
    def __init__(self, nodes: List[Node]):
        self.nodes = nodes
        self.node_dict = {}
        self.doctors_tile = None
        self.rivers_tile = None
        self.source_node = None
        self.sink_node = None
        self._set_node_dict(nodes)

    def _set_node_dict(self, nodes: List[Node]):
        for n in nodes:
            self.node_dict[n.id] = n
            if len(n.node_ids_that_point_to_me) == 0:
                self.doctors_tile = n
                self.source_node = n
            elif len(n.points_to_nodes) == 0:
                self.rivers_tile = n
                self.sink_node = n
    
    def move_doctors_tile(self, node: Node):
        self.doctors_tile = node

    def move_rivers_tile(self, node: Node):
        self.rivers_tile = node
