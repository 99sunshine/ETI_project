from pyspecs import *
from .components import *
from .systems import *

def fermi_world():
  world = World()
  world.register_system(SunlikeStarFormingSystem())
  world.register_system(SunlikeStarAgingSystem())
  world.register_system(SunlikeStarDyingSystem())
  world.setup()
  return world

def main():
  print("Hello world")