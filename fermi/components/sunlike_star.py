from pyspecs import Component
from ..util import Vector3

class SunlikeStarAge(Component):
  def __init__(self, max_age: int):
    self.age = 0
    self.max_age = max_age

  def step(self, step_count: int = 1):
    self.age += step_count

  def is_excessing_age(self):
    return self.age >= self.max_age

  def __repr__(self):
    return f"Age: {self.age}, Max age: {self.max_age}"

class SunlikeStarPosition(Component):
  def __init__(self, position: Vector3):
    self.position = position

  def __repr__(self):
    return f"Position: {self.position}"

class SunlikeStarLife(Component):
  def __init__(self, n_life_stages: int):
    self.life_stage = 0
    self.n_life_stages = n_life_stages

  def step(self, step_count: int = 1):
    self.life_stage += step_count