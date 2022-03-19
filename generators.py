# generators.py

from types import GeneratorType

def squares_gen(lst:list) -> GeneratorType:
  for x in lst:
    yield x**2

digits = [0,1,2,3,4,5,6,7,8,9]
digits_squared = squares_gen(digits)
# With generator expression:
digits_squared2 = (x**2 for x in digits)
# Once iterated, the generator is empty!


def fibonacci_gen(max_term:int) -> GeneratorType:
  """ Returns a generator for the fibonacci sequence up to the n term """

  n1:int = 0
  n2:int = 1
  counter:int = 0

  while counter <= max_term:
    if counter == 0:
      counter += 1
      yield n1
    elif counter == 1:
      counter += 1
      yield n2
    else:
      counter += 1
      aux = n1 + n2
      n1,n2 = n2,aux
      yield aux
