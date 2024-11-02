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

# Graph a
#    1
#   ^ \
#  /   v
# 0 -> 2
def test_graph_a():
   n2 = Node(id=2, node_ids_that_point_to_me=[0, 1])
   n1 = Node(id=1, node_ids_that_point_to_me=[0], points_to_nodes=[n2])
   n0 = Node(id=0, points_to_nodes=[n1, n2])
   g = Graph([n0, n1, n2])
   game = KeepAwayGame(g)
   assert game.who_wins() == Player.RIVER.value

# Graph b
#    1
#   ^ \
#  /   v
# 0 -> 2 -> 3
def test_graph_b():
   n3 = Node(id=3, node_ids_that_point_to_me=[2])
   n2 = Node(id=2, node_ids_that_point_to_me=[0, 1], points_to_nodes=[n3])
   n1 = Node(id=1, node_ids_that_point_to_me=[0], points_to_nodes=[n2])
   n0 = Node(id=0, points_to_nodes=[n1, n2])
   g = Graph([n0, n1, n2, n3])
   game = KeepAwayGame(g)
   assert game.who_wins() == Player.RIVER.value

# Graph c
#         2 
#        ^ \
#       /   v
# 0 -> 1 -> 3 -> 4
def test_graph_c():
   n4 = Node(id=4, node_ids_that_point_to_me=[3])
   n3 = Node(id=3, node_ids_that_point_to_me=[1], points_to_nodes=[n4])
   n2 = Node(id=2, node_ids_that_point_to_me=[1], points_to_nodes=[n3])
   n1 = Node(id=1, node_ids_that_point_to_me=[0], points_to_nodes=[n3, n2])
   n0 = Node(id=0, points_to_nodes=[n1])
   g = Graph([n0, n1, n2, n3, n4])
   game = KeepAwayGame(g)
   assert game.who_wins() == Player.RIVER.value


# Graph d
#         2 -> 4
#        ^     \
#       /       v
# 0 -> 1 -> 3 -> 5
def test_graph_d():
   n5 = Node(id=5, node_ids_that_point_to_me=[3,4])
   n4 = Node(id=4, node_ids_that_point_to_me=[2], points_to_nodes=[n5])
   n3 = Node(id=3, node_ids_that_point_to_me=[1], points_to_nodes=[n5])
   n2 = Node(id=2, node_ids_that_point_to_me=[1], points_to_nodes=[n4])
   n1 = Node(id=1, node_ids_that_point_to_me=[0], points_to_nodes=[n3, n2])
   n0 = Node(id=0, points_to_nodes=[n1])
   g = Graph([n0, n1, n2, n3, n4, n5])
   game = KeepAwayGame(g)
   assert game.who_wins() == Player.DOCTOR.value

# Graph e
#         2 -> 4 -> 6 -> 8 -> 10
#        ^     \   ^          \
#       /       v /            v
# 0 -> 1 -> 3 -> 5 -> 7 -> 9 -> 11 -> 12
def test_graph_e():
    n12 = Node(id=12, node_ids_that_point_to_me=[11])
    n11 = Node(id=11, node_ids_that_point_to_me=[9, 10], points_to_nodes=[n12])
    n10 = Node(id=10, node_ids_that_point_to_me=[8], points_to_nodes=[n11])
    n9 = Node(id=9, node_ids_that_point_to_me=[7], points_to_nodes=[n11])
    n8 = Node(id=8, node_ids_that_point_to_me=[6], points_to_nodes=[n10])
    n7 = Node(id=7, node_ids_that_point_to_me=[5], points_to_nodes=[n9])
    n6 = Node(id=6, node_ids_that_point_to_me=[4, 5], points_to_nodes=[n8])
    n5 = Node(id=5, node_ids_that_point_to_me=[3, 4], points_to_nodes=[n6, n7])
    n4 = Node(id=4, node_ids_that_point_to_me=[2], points_to_nodes=[n5, n6])
    n3 = Node(id=3, node_ids_that_point_to_me=[1], points_to_nodes=[n5])
    n2 = Node(id=2, node_ids_that_point_to_me=[1], points_to_nodes=[n4])
    n1 = Node(id=1, node_ids_that_point_to_me=[0], points_to_nodes=[n2, n3])
    n0 = Node(id=0, points_to_nodes=[n1])

    g = Graph([n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12])
    game = KeepAwayGame(g)
    assert game.who_wins() == Player.DOCTOR.value
   

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