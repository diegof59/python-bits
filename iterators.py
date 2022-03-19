# iterators.py

class Multiples:
  """ Multiples of a number, iterator """

  def __init__(self, num=1, max=None):
    self._num = num
    self._max = max

  def __iter__(self):
    self._multiple = 0
    return self
  
  def __next__(self):
    if not self._max or self._multiple <= self._max:
      result = self._multiple
      self._multiple += self._num
      return result
    else:
      raise StopIteration
  
class FibonacciIterator:
  """ Fibonacci sequence iterator up to given term """

  def __init__(self, max_term):
    self._max_term = max_term

  def __iter__(self):
    self._n1 = 0
    self._n2 = 1
    self._counter = 0 # counter: Current sequence position
    return self

  def __next__(self):

    if self._counter <= self._max_term:
      if self._counter == 0:
        self._counter += 1
        return self._n1
      elif self._counter == 1:
        self._counter += 1
        return self._n2
      else:
        self._counter += 1
        aux = self._n1 + self._n2
        self._n1, self._n2 = self._n2, aux
        return aux
    else:
      raise StopIteration
    

def multiplication_table_5(n:int,max:int=10):
  """ Prints the multiplication table of 5 """
  multiples = Multiples(5,50)

  # for loop implementation:
  m_iter = iter(multiples)
  while True:
    try:
      element = next(m_iter)
      # for contents
      print(element)
      # ---
    except StopIteration:
      break
  # end for

def fibo(n:int):
  """ Prints the fibonnaci sequence up to the n term"""
  
  fibo = FibonacciIterator(n)
  for num in fibo:
    print(num)