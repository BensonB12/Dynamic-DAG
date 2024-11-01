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
  n0 = Node(id=0, is_s=True, is_t=True)
  g = Graph(nodes=[n0])
  assert KeepAwayGame.who_wins(g) == Player.RIVER.value