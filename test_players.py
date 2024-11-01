from player import Player


def test_doctor():
  assert Player.DOCTOR.value == "Doctor"

def test_river():
  assert Player.RIVER.value == "River"