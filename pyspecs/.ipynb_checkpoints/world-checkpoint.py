from typing import Dict, List

from .system import System
from .storage import Storage

class World:
  def __init__(self):
    self.count : int = 0
    self.storages : Dict[str, Storage] = {}
    self.systems : List[System] = []

  def register_system(self, system: System):
    self.systems.append(system)

  def register_component(self, comp):
    if not comp.__name__ in self.storages:
      self.storages[comp.__name__] = Storage()

  def get_storage(self, comp):
    if comp.__name__ in self.storages:
      return self.storages[comp.__name__]
    else:
      return None

  def setup(self):
    for system in self.systems:
      for comp in system.DATA:
        self.register_component(comp)

  def remove_entity(self, index: int):
    for store_name in self.storages:
      store = self.storages[store_name]
      if index in store:
        store.remove(index)

  def create_entity(self):
    self.count += 1
    return self.count

  def run(self, num_steps=1):
    for _ in range(num_steps):
      for system in self.systems:
        stores = [self.storages[comp.__name__] for comp in system.DATA]
        system.world = self
        system.run(*stores)