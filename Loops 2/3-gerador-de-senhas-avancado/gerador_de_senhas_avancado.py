from ast import Num
import numbers
import string # Leia mais sobre a biblioteca string. https://docs.python.org/pt-br/3/library/string.html#string.ascii_letters
import random # Você pode gerar números aleatórios com o método random. https://docs.python.org/3/library/random.html

def advanced_password_generator(password_size):
  # Crie um gerador de senhas com números e caracteres de maneira alternada.
  # Ex.: A chamada advanced_password_generator(5) -> Irá resultar em algo parecido com 8j9D9 ou 5b7D6
  palavra = ''
  for u in range(password_size):
    palavra += (random.choice(string.ascii_letters))
    palavra += (str(random.choice([1,2,3,4,5,6,7,8,9,0])))
  print (palavra)
  return palavra
# Use o print com a chamada do método para testar
(advanced_password_generator(0))
