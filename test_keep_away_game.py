from graph import Graph, Node
from keep_away_game import KeepAwayGame
from player import Player


def test_keep_away_game():
  game = KeepAwayGame()
  assert game

def test_has_winner_base_case_0():
  g = Graph(nodes=[])
  assert KeepAwayGame.who_wins(g) == Player.DOCTOR.value

def test_has_winner_base_case_1():
  nodes = make_a_nodes_line_of_length(1)
  g = Graph(nodes=nodes)
  assert KeepAwayGame.who_wins(g) == Player.RIVER.value

def test_graph_is_small_line():
  nodes = make_a_nodes_line_of_length(3)
  g = Graph(nodes=nodes)
  assert KeepAwayGame.who_wins(g) == Player.RIVER.value

def test_graph_is_large_line():
  nodes = make_a_nodes_line_of_length(10)
  g = Graph(nodes=nodes)
  assert KeepAwayGame.who_wins(g) == Player.RIVER.value

@staticmethod
def make_a_nodes_line_of_length(l: int):
  if l == 1:
     return [Node(id=0, is_s=True, is_t=True)]
  
  nodes = []
  for i in range(l):
    if i == 0:
        node = Node(id=i, is_s=True)
    elif i == 9:
        node = Node(id=i, is_t=True, node_ids_that_point_to_me=[i - 1])
    else:
        node = Node(id=i, node_ids_that_point_to_me=[i - 1])
    nodes.append(node)

  for i in range(l-1):
    nodes[i].points_to_nodes.append(nodes[i + 1])

  return nodes