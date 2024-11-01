from graph import Graph, Node
from keep_away_game import KeepAwayGame
from player import Player


def test_has_winner_base_case_0():
  g = Graph([])
  game = KeepAwayGame(g)
  assert game.who_wins() == Player.DOCTOR.value

def test_has_winner_base_case_1():
  nodes = make_a_nodes_line_of_length(1)
  g = Graph(nodes)
  game = KeepAwayGame(g)
  assert game.who_wins() == Player.RIVER.value

def test_graph_is_small_line():
  nodes = make_a_nodes_line_of_length(3)
  g = Graph(nodes)
  game = KeepAwayGame(g)
  assert game.who_wins() == Player.RIVER.value

def test_graph_is_large_line():
  nodes = make_a_nodes_line_of_length(10)
  g = Graph(nodes)
  game = KeepAwayGame(g)
  assert game.who_wins() == Player.RIVER.value

@staticmethod
def make_a_nodes_line_of_length(l: int):
  if l == 1:
     return [Node(id=0)]
  
  nodes = []
  for i in range(l):
    if i == 0:
        node = Node(id=i)
    elif i == 9:
        node = Node(id=i, node_ids_that_point_to_me=[i - 1])
    else:
        node = Node(id=i, node_ids_that_point_to_me=[i - 1])
    nodes.append(node)

  for i in range(l-1):
    nodes[i].points_to_nodes.append(nodes[i + 1])

  return nodes