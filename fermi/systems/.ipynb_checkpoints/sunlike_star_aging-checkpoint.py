from pyspecs import *
from ..components import *

class SunlikeStarAgingSystem(System):

  DATA = [SunlikeStarAge]

  def run(self, ages):
    for (entity, age) in ages:
      age.step()