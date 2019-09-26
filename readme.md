# Fermi Simulation with ECS

How to setup:

``` bash
$ ./scripts/setup.sh
```

How to run:

``` bash
$ python3 simulate.py
```

## Entity Component System

This simulation framework features an Entity Component System Framework similar to [Specs](https://github.com/slide-rs/specs). We have a nice demo of [Bouncy World](https://github.com/Liby99/fermipy/blob/master/notebooks/bouncy_world.ipynb) and you can checkout the output video. In general, ECS allows much nicer design of simulation programs and ensures maintainability, robustness and extensibility.

We divide the whole frameworks to several parts:

### Component

In ECS, a _Component_ represents a set of data. In traditional Object Oriented Programming, people needs to put all the fields together. But in ECS, we tend to separate data as much as possible to avoid overhead. For example, a _Star_ might contain _Age_ information, _Life_ information and _Position_. But their usages are mostly disjoint. So we separate them into three components. As an example:

``` python
class SunlikeStarPosition(Component):
  def __init__(self, position: Vector3):
    self.position = position
```

Component classes should be inheriting `Component`. At the same time, a component should contain only the essential data. No action is required to be associated. (Note: This is also called Data Oriented Program Design, as opposed to Object Oriented).

### System

Another big thing is the `System`. System is required to read and mutate the world state. Similar to `Component`, we should also separate as much as possible for debuggable, maintainable and extensible simulation. As an example, the star aging system and star movement system can be separated. As the name suggests, a star aging system should only rely on reading and mutating the age component.

``` python
class SunlikeStarAgingSystem(System):
  DATA = [SunlikeStarAge]
  def run(self, ages):
    for (entity, age) in ages:
      age.step()
```

In this example we are creating a `SunlikeStarAgingSystem`. The first thing to notice is that it inherits `System`, which is required for all systems. It has to have a static `DATA` field, which is an array or a tuple of `Component` classes. In this case, since the system only needs the age component, we declare that we need `SunlikeStarAge`.

Every `System` also requires a `run` method to be implemented. In addition to `self`, we will receive the component stores through function arguments. In this case, since we only declare that we need `SunlikeStarAge`, then we will only receive a single store, in this case, `ages`. If we declare that we want multiple stores, we simply extend the `DATA` list. All the stores will be received in the order they appear in `DATA`.

It's very natural to want to iterate through all the `SunlikeStarAge` components, since for each of them we want the age to step once ahead. So we start by using a for loop. Note that when iterating through a store, or a conjunction of stores, you will always receive an `entity` which is a unique id to represent the entity that contains this component. Currently we don't need it. The second element in the tuple will be our `age` component. Finally, we just use the `step` function implemented in `SunlikeStarAge` to advance the age one step forward.

In the above example we covered the iteration process over the component storage. We also have several more use cases:

#### Add a Component to an existing Entity

Let's say you already have the entity id and you want to add a new component to it. You can do the following

``` python
class SomeSystem(System):
  DATA = [SomeComponent]
  def run(self, some_components):
    entity_id = ...
    some_components.insert(entity_id, SomeComponent())
```

#### Remove a Component from an existing Entity

Similar to above, when you want to remove `SomeComponent` from the entity with `entity_id`

``` python
class SomeSystem(System):
  DATA = [SomeComponent]
  def run(self, some_components):
    entity_id = ...
    some_components.remove(entity_id)
```

#### Create an Entity

Creating a new Entity simply means letting the world allocate you a new Entity Id. You can then add a component to that existing entity or do anything else you want. To get a new Entity Id, you can

``` python
class SomeSystem(System):
  DATA = [...]
  def run(self, ...):
    new_entity_id = self.world.create_entity()
```

#### Remove an Entity

Removing an entity requires the possession of the entity id. This will remove all the component related to that Entity as well.

``` python
class SomeSystem(System):
  DATA = [...]
  def run(self, ...):
    entity_id = ...
    self.world.remove_entity(entity_id)
```

#### Getting a Component from an Existing Entity

``` python
class SomeSystem(System):
  DATA = [SomeComponent, ...]
  def run(self, some_components, ...):
    entity_id = ...
    comp = some_components[entity_id]
```

#### Iterate through entities with two or more components

Sometimes you might want to find all the entities that have two or more components. In that case you want to use `Storage.join` to join two or more components. Note that the yield result will also contain the entity id in the first place. And all the rest of the components will remain the order you put into `Storage.join`.

``` python
class SomeSystem(System):
  DATA = [Comp1, Comp2, ...]
  def run(self, comp_1s, comp_2s, ...):
    for (ent, comp_1, comp_2, ...) in Storage.join(comp_1s, comp_2s, ...):
      # Do other things
```

## Testing

For example you have a function called `test_storage_2`, you can invoke the test using

``` bash
$ python3 test.py test_storage_2
```

When writing a new test, you can go to anywhere and add a decorator `@test`. For example, you can create a new function in `tests/test_storage.py` and type

``` python
@test
def hello_world_test():
  print("Hello world")
```

Then in command line you can invoke this test using

``` bash
$ python3 test.py hello_world_test
```