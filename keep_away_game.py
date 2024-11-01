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
# If any of these rules are broken when calling who_wins, it will not work as desired. In
#   fact it might be an infinite loop and hurt the running machine
class KeepAwayGame:
  @staticmethod
  def who_wins(g: Graph) -> str:
    base_case_value_or_none = KeepAwayGame.has_base_case_value_or_none(g)

    if base_case_value_or_none is not None:
      return base_case_value_or_none
    
  @staticmethod
  def has_base_case_value_or_none(g: Graph) -> str | None:
    # Base Case 0: If there are no nodes in the graph, the doctor wins because
    #               RIVER will never be on his node
    if(len(g.nodes) < 1):
      return Player.DOCTOR.value
    
    # Base Case 1: If there is only one node, River wins before the game even starts. 
    #                 She is touching the Doctor before the Doctor can check to see
    #                 if he is in the right spot or River is in the right spot
    if(len(g.nodes) == 1):
      return Player.RIVER.value
    
    return None
  
