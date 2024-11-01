from graph import Graph
from player import Player

# We assume that the graph is a Directional ACYCLIC Graph
# Graph: There are nodes and edges
# Directional: Nodes connected to other nodes have a direction
# ACYCLIC: If you follow the directions of the graph, 
#           there are no loops, you cannot get back to where you started following the path
# We also assume that the graph has a 's' and 't' node in the graph. We also assume that
#   the 's' node is a 'source vertex' and the 't' node is a 'sink vertex'
# Source Vertex: A node that has no nodes pointing to it
# Sink Vertex: A node that does not point to any other nodes
# The last thing we assume is that this graph is connected. The problem we are solving says 
#   that there is always a winner, either "River" of "Doctor". If the graph is split into 
#   two different graphs that cannot connect, then there is no winners because 's' and 't' 
#   could be on different 'graph islands' and therefore neither would win 
# If any of these rules are broken when calling who_wins, it will not work as desired. In
#   fact it might be an infinite loop and hurt the running machine
class KeepAwayGame:
  @staticmethod
  def who_wins(g: Graph) -> str:
    base_case_value_or_none = KeepAwayGame.has_base_case_value_or_none(g)

    if base_case_value_or_none is not None:
      return base_case_value_or_none
    
    # If there is only one directed line/links of nodes then River will always win because the Doctor cannot go 'around' her
    if KeepAwayGame.graph_is_a_line(g):
      return Player.RIVER.value
    
    # If there is only one directed line/links of nodes then River will always win because the Doctor cannot go 'around' her
    if KeepAwayGame.graph_is_a_line(g):
      return Player.RIVER.value

  @staticmethod
  def graph_is_a_line(g: Graph) -> bool:
    for n in g.nodes[1:]:
      if len(n.node_ids_that_point_to_me) != 1:
        return False
    return True

    
  @staticmethod
  def has_base_case_value_or_none(g: Graph) -> str | None:
    # Base Case 0: If there are no nodes in the graph, the doctor wins because
    #               RIVER will never be on his node (This case kind of breaks 
    #               the rules set up by the problem, but if it was an easy case 
    #               to handle I tried to handle it)
    if(len(g.nodes) < 1):
      return Player.DOCTOR.value
    
    # Base Case 1: If there is only one node, River wins before the game even starts. 
    #                 She is touching the Doctor before the Doctor can check to see
    #                 if he is in the right spot or River is in the right spot
    if(len(g.nodes) == 1):
      return Player.RIVER.value
    
    return None
  
