  # Ler um número e retornar True se for primo e False se não for primo.
  # Sobre o que é um número primo: https://pt.wikipedia.org/wiki/N%C3%BAmero_primo
  # Dica: veja o for/else: https://book.pythontips.com/en/latest/for_-_else.html#else-clause
  # exemplos:
  # prime_numbers(10) -> False
  # prime_numbers(13) -> True
  # prime_numbers(1) -> False
  # prime_numbers(2) -> True

def is_prime_number(number):

  if number==1:
    return False
  if number %2 != 0 and number%3 != 0 and number%5 !=0 and number%7!=0:
    return True
  if number==2 or number==3 or number==5 or number==2 or number==7:
    return True
  else:
    return False
  pass


print(is_prime_number(1))
