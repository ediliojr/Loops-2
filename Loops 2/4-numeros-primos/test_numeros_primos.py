from numeros_primos import (prime_numbers)

def test_prime_numbers():
  assert prime_numbers(0) == []
  assert prime_numbers(1) == []
  assert prime_numbers(2) == []
  assert prime_numbers(3) == [2]
  assert prime_numbers(4) == [2,3]
  assert prime_numbers(9) == [2,3,5,7]
  assert prime_numbers(15) == [2,3,5,7,11,13]
