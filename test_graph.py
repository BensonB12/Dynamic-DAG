from graph import Node, Graph

def test_node():
  n0 = Node(id=0)
  assert n0

def test_graph():
  g = Graph([])
  assert g

def test_nodes_go_into_graph():
  n0 = Node(id=0)
  g = Graph([n0])
  assert g.nodes[0] == n0

def test_graph_multiple_nodes():
    n0 = Node(id=0)
    n1 = Node(id=1)
    g = Graph([n0, n1])
    assert len(g.nodes) == 2
    assert g.nodes[0] == n0
    assert g.nodes[1] == n1

def test_graph_has_references():
    n1 = Node(id=1, node_ids_that_point_to_me=[0])
    n0 = Node(id=0, points_to_nodes=[n1])
    g = Graph([n0, n1])
    assert g.nodes[0].points_to_nodes == [n1]
    assert g.nodes[1].node_ids_that_point_to_me == [0]

def test_graph_has_t_and_s():
    n1 = Node(id=1, node_ids_that_point_to_me=[0])
    n0 = Node(id=0, points_to_nodes=[n1])
    g = Graph([n0, n1])
    assert g.source_node == n0
    assert g.sink_node == n1

def test_graph_sets_river_and_doctor_right():
    n1 = Node(id=1, node_ids_that_point_to_me=[0])
    n0 = Node(id=0, points_to_nodes=[n1])
    g = Graph([n0, n1])
    assert g.doctors_tile == n0
    assert g.rivers_tile == n1

def test_graph_moves_doctors_right():
    n1 = Node(id=1, node_ids_that_point_to_me=[0])
    n0 = Node(id=0, points_to_nodes=[n1])
    g = Graph([n0, n1])
    g.move_doctors_tile(n1)
    assert g.doctors_tile == n1

def test_graph_moves_river_right():
    n1 = Node(id=1, node_ids_that_point_to_me=[0])
    n0 = Node(id=0, points_to_nodes=[n1])
    g = Graph([n0, n1])
    g.move_rivers_tile(n0)
    assert g.rivers_tile == n0