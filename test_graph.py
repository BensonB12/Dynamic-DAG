from graph import Node, Graph

def test_node():
  n0 = Node(id=0)
  assert n0

def test_graph():
  g = Graph(nodes=[])
  assert g

def test_nodes_go_into_graph():
  n0 = Node(id=0)
  g = Graph(nodes=[n0])
  assert g.nodes[0] == n0

def test_graph_multiple_nodes():
    n0 = Node(id=0)
    n1 = Node(id=1)
    g = Graph(nodes=[n0, n1])
    assert len(g.nodes) == 2
    assert g.nodes[0] == n0
    assert g.nodes[1] == n1

def test_graph_has_references():
    n1 = Node(id=1, node_ids_that_point_to_me=[0])
    n0 = Node(id=0, points_to_nodes=[n1])
    g = Graph(nodes=[n0, n1])
    assert g.nodes[0].points_to_nodes == [n1]
    assert g.nodes[1].node_ids_that_point_to_me == [0]

def test_graph_has_t_and_s():
    n1 = Node(id=1, node_ids_that_point_to_me=[0], is_s=True)
    n0 = Node(id=0, points_to_nodes=[n1], is_t=True)
    g = Graph(nodes=[n0, n1])
    assert g.nodes[0].is_t
    assert g.nodes[1].is_s
