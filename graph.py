from typing import List
from pydantic import BaseModel
from __future__ import annotations


class Node(BaseModel):
    id: int
    is_s: bool
    is_t: bool
    points_to_nodes: List[Node]
    node_ids_that_point_to_me: List[int]


class Graph(BaseModel):
    nodes: List[Node]
