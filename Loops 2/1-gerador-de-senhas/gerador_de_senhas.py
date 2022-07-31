
import string # Leia mais sobre a biblioteca string. https://docs.python.org/pt-br/3/library/string.html#string.ascii_letters
import random


# Crie um gerador de senhas aleatórias com somente letras do tamanho passado como parâmetro
def password_generator(password_size):
  palavra= ''
  for u in range(password_size):
    palavra+=(random.choice(string.ascii_letters))
  print(palavra)
  return(palavra)
password_generator(10)
