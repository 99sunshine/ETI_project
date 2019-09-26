from typing import Tuple, Generator
from .component import Component

class Storage:
  def __init__(self):
    self.storage : Dict[int, Component] = {}

  def __get__(self, index) -> Component:
    return self.storage[index]

  def __iter__(self) -> Generator[Tuple[int, Component], None, None]:
    for key in self.storage:
      yield (key, self.storage[key])

  def __contains__(self, index: int) -> bool:
    return index in self.storage

  def insert(self, index: int, item: Component):
    self.storage[index] = item

  def remove(self, index: int):
    del self.storage[index]

  def join(*storages) -> Generator[Tuple[int, Component], None, None]:
    for (key, elem) in storages[0]:
      elems = [key, elem]
      flag = True
      for store in storages[1:]:
        if key in store.storage:
          elems.append(store.storage[key])
        else:
          flag = False
          break
      if flag:
        yield tuple(elems)
