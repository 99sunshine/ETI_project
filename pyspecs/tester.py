from typing import Dict, Callable

storage : Dict[str, Callable[[], None]] = {}

def test(test_func: Callable[[], None]) -> Callable[[], None]:
  def wrapper():
    print(f"--- Testing {test_func.__name__} ---")
    test_func()
  storage[test_func.__name__] = wrapper
  return wrapper

def invoke_test(func_name: str):
  if func_name in storage:
    storage[func_name]()
  else:
    print(f"No test named {func_name}")