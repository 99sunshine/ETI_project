from pyspecs import *
from ..components import *
from ..util import MilkyWay

class SunlikeStarFormingSystem(System):

  DATA = [SunlikeStarAge, SunlikeStarLife, SunlikeStarPosition]

  def run(self, ages, lifes, positions):
    for _ in range(MilkyWay.sample_sunlike_star_formation_amount()):
      entity = self.world.create_entity()
      ages.insert(entity, SunlikeStarAge(MilkyWay.sample_sunlike_star_age()))
      positions.insert(entity, SunlikeStarPosition(MilkyWay.sample_star_position()))
      if MilkyWay.sample_is_habitable_planet():
        lifes.insert(entity, SunlikeStarLife(MilkyWay.sample_planet_n_life_stages()))