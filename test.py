import sys
import tests
from pyspecs import invoke_test

if __name__ == "__main__":
  if len(sys.argv) <= 1:
    print("Please specify a test name")
  for test_name in sys.argv[1:]:
    invoke_test(test_name)
