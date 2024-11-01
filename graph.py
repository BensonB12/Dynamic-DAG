from __future__ import annotations
from typing import List
from pydantic import BaseModel


class Node(BaseModel):
    id: int
    is_s: bool = False
    is_t: bool = False
    points_to_nodes: List[Node] = []
    node_ids_that_point_to_me: List[int] = []


class Graph(BaseModel):
    nodes: List[Node]
