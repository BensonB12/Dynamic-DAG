from graph import Graph
from player import Player

# We assume that the graph is a Directional ACYCLIC Graph
# Graph: There are nodes and edges
# Directional: Nodes connected to other nodes have a direction
# ACYCLIC: If you follow the directions of the graph, 
#           there are no loops, you cannot get back to where you started following the path
# We also assume that the graph has a single 's' and a single 't' node in the graph. We also assume that
#   the 's' node is a 'source vertex' and the 't' node is a 'sink vertex'
# Source Vertex: A node that has no nodes pointing to it
# Sink Vertex: A node that does not point to any other nodes
# If any of these rules are broken when calling who_wins, it will not work as desired. In
#   fact it might be an infinite loop and hurt the running machine
class KeepAwayGame:
  def __init__(self, g: Graph):
    self.g = g

  def who_wins(self) -> str:
    base_case_value_or_none = self._has_base_case_value_or_none()

    if base_case_value_or_none is not None:
      return base_case_value_or_none
    
    return self._step_return_winner(self.g, Player.DOCTOR).value
    
  def _has_base_case_value_or_none(self) -> str | None:
    # Base Case 0: If there are no nodes in the graph, the doctor wins because
    #               RIVER will never be on his node (This case kind of breaks 
    #               the rules set up by the problem, but if it was an easy case 
    #               to handle I tried to handle it)
    if(len(self.g.nodes) < 1):
      return Player.DOCTOR.value
    
    # Base Case 1: If there is only one node, River wins before the game even starts. 
    #                 She is touching the Doctor before the Doctor can check to see
    #                 if he is in the right spot or River is in the right spot
    if(len(self.g.nodes) == 1):
      return Player.RIVER.value
    
    return None
  
  def _step_return_winner(self, g: Graph, playersTurn: Player) -> Player | None:
    winner = self._check_for_winner(g)

    if winner is not None:
      return winner

    list_of_winners = []
    if(playersTurn == Player.DOCTOR):
      for n in g.doctors_tile.points_to_nodes:
        if n == g.rivers_tile:
          if len(g.doctors_tile.points_to_nodes):
            list_of_winners.append(Player.RIVER)
          break
        new_graph = Graph(g.nodes)
        new_graph.move_doctors_tile(n)
        new_graph.move_rivers_tile(g.rivers_tile)
        list_of_winners.append(self._step_return_winner(new_graph, Player.RIVER))
    else:
      for i in g.rivers_tile.node_ids_that_point_to_me:
        n = g.node_dict[i]
        if n == g.doctors_tile:
          return Player.RIVER
        new_graph = Graph(g.nodes)
        new_graph.move_rivers_tile(n)
        new_graph.move_doctors_tile(g.doctors_tile)
        list_of_winners.append(self._step_return_winner(new_graph, Player.DOCTOR))

    set_with_only_players = set([p for p in list_of_winners if p is not None])

    if set_with_only_players == {Player.DOCTOR, Player.RIVER}:
      return Player.DOCTOR
    elif set_with_only_players == {Player.DOCTOR}:
      return Player.DOCTOR
    elif set_with_only_players == {Player.RIVER}:
      return Player.RIVER
    else:
        return None

  def _check_for_winner(self, g: Graph) -> Player | None:
    # If both players are on the same tile, River wins!
    if g.doctors_tile == g.rivers_tile:
      return Player.RIVER
    
    # If Doctor is on the 'vertex sink' or River is on the 'vertex source' then the Doctor wins!
    if g.doctors_tile == g.sink_node or g.rivers_tile == g.source_node:
      return Player.DOCTOR
    
    return None
    
