# Ler um número e gerar todos os números primos menores que o número fornecido retornando uma lista com todos eles.
# Sobre números primos
# exemplos:
# prime_numbers(10) -> [2,3,5,7]
# prime_numbers(13) -> [2,3,5,7,11]

from asyncio.windows_events import NULL
from unittest import skipIf

from pytest import skip


def prime_numbers(number):
  lista=[]

  u=0
  for u in range(2,number):

    if u %2 != 0 and u%3 != 0 and u%5 !=0 and u%7!=0:
      lista.append(u)
    if u==2 or u==3 or u==5 or u==2 or u==7:
      lista.append(u)

  print (lista)
  return lista
  pass

(prime_numbers(3))
