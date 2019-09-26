from pyspecs import *
from ..components import *

class SunlikeStarDyingSystem(System):

  DATA = [SunlikeStarAge]

  def run(self, ages):
    to_remove = [ent for (ent, age) in ages if age.is_excessing_age()]
    for ent in to_remove:
      self.world.remove_entity(ent)