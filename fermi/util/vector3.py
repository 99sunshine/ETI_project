from __future__ import annotations
import math

class Vector3:
  def __init__(self, x: float, y: float, z: float):
    self.x = x
    self.y = y
    self.z = z

  def __add__(self, other: Vector3) -> Vector3:
    return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

  def __sub__(self, other: Vector3) -> Vector3:
    return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

  def __mult__(self, scale: float) -> Vector3:
    return Vector3(self.x * scale, self.y * scale, self.z * scale)

  def __repr__(self) -> str:
    return f"({self.x}, {self.y}, {self.z})"

  def magnitude(self) -> float:
    return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)