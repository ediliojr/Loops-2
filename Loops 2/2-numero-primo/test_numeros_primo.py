from numeros_primo import (is_prime_number)

def test_prime_numbers():
  assert is_prime_number(0) == False
  assert is_prime_number(1) == False
  assert is_prime_number(2) == True
  assert is_prime_number(4) == False
  assert is_prime_number(13) == True
  assert is_prime_number(15) == False
