from graph import Graph
from player import Player


class KeepAwayGame:
  @staticmethod
  def who_wins(g: Graph) -> str:
    return Player.RIVER.value