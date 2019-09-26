from pyspecs import *
from fermi import *

@test
def test_storage_1():
  world = World()
  world.register_system(SunlikeStarFormingSystem())
  world.register_system(SunlikeStarAgingSystem())
  world.setup()
  for _ in range(10):
    world.run()
  store = world.get_storage(SunlikeStarAge)
  for (ent, age) in store:
    print(ent, age)

@test
def test_storage_2():
  world = World()
  world.register_system(SunlikeStarFormingSystem())
  world.register_system(SunlikeStarAgingSystem())
  world.register_system(SunlikeStarDyingSystem())
  world.setup()
  for _ in range(20):
    world.run()
  age_store = world.get_storage(SunlikeStarAge)
  pos_store = world.get_storage(SunlikeStarPosition)
  for (ent, age, pos) in Storage.join(age_store, pos_store):
    print(ent, age, pos)