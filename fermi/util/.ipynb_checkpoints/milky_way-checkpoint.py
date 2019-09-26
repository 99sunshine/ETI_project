import math
from random import *

from .vector3 import Vector3

class MilkyWay:

  radius = 22.5
  thickness = 0.4

  def sample_sunlike_star_formation_amount() -> int:
    """
    TODO
    """
    return int(1)

  @staticmethod
  def sample_star_position() -> Vector3:
    """
    TODO
    """
    theta = random() * math.pi * 2.0
    r = math.sqrt(random()) * MilkyWay.radius
    h = random() * MilkyWay.thickness
    return Vector3(r * math.cos(theta), r * math.sin(theta), h)

  @staticmethod
  def sample_sunlike_star_age() -> int:
    """
    This will return an instance of sunlike star maximum age
    according to the following distribution:
      TODO
    """
    return int(3 + 10 * random()) # TODO

  @staticmethod
  def sample_is_habitable_planet() -> bool:
    """
    TODO
    """
    return random() < 0.001 # TODO

  @staticmethod
  def sample_planet_n_life_stages() -> int:
    """
    TODO
    """
    return randint(5, 15) # TODO

  @staticmethod
  def get_star_formation_rate() -> float:
    """
    TODO
    """
    star_formation_rate = 1500000 + 1500000 * random() # number of star / year (adjust to the time step(million year))
    return star_formation_rate

  @staticmethod
  def is_habitable_planet_possibility() -> float:
    """
    TODO
    """
    habitable_planet_percentage = 0.0025 + 0.0086 * random() #  (Petiguraa et al. 2013)
    return habitable_planet_percentage

  @staticmethod
  def is_snla_possibility() -> float:
    """
    TODO
    """
    return 0.3 # TODO

  @staticmethod
  def is_snll_possibility() -> float:
    """
    TODO
    """
    return 0.1 # TODO