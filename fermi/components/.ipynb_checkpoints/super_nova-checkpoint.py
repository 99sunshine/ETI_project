from pyspecs import Component
from ..util import Vector3

class SuperNovaAge(Component):
  def __init__(self, max_age: int):
    self.age = 0
    self.max_age = max_age

class SuperNovaPosition(Component):
  def __init__(self, position: Vector3):
    self.position = position