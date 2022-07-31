import inspect
import pytest

from aula import (criptografar, descriptografar)

def test_criptografar():
  assert criptografar(10, "HELLO WORLD") == "ROVVY GYBVN", "A mensagem 'HELLO WORLD' deve ser criptografada em 'ROVVY GYBVN'"
  assert criptografar(3, "OLA MUNDO") == "ROD PXQGR", "A mensagem 'OLA MUNDO' deve ser criptografada em 'ROD PXQGR'"
  assert criptografar(5, "MINHA PRIMEIRA FRASE") == "RNSMF UWNRJNWF KWFXJ", "A mensagem 'MINHA PRIMEIRA FRASE' deve ser criptografada em 'RNSMF UWNRJNWF KWFXJ'"
  assert criptografar(0, "CRIPTOGRAFIA E ESCONDER MENSAGENS") == "CRIPTOGRAFIA E ESCONDER MENSAGENS", "A mensagem 'CRIPTOGRAFIA E ESCONDER MENSAGENS' deve ser criptografada em 'CRIPTOGRAFIA E ESCONDER MENSAGENS'"

def test_descriptografar():
  assert descriptografar(10, "ROVVY GYBVN") == "HELLO WORLD", "A mensagem 'HELLO WORLD' foi descriptografada de 'ROVVY GYBVN'"
  assert descriptografar(3, "ROD PXQGR") == "OLA MUNDO", "A mensagem 'OLA MUNDO' foi descriptografada de 'ROD PXQGR'"
  assert descriptografar(5, "RNSMF UWNRJNWF KWFXJ") == "MINHA PRIMEIRA FRASE", "A mensagem 'MINHA PRIMEIRA FRASE' foi descriptografada de 'RNSMF UWNRJNWF KWFXJ'"
  assert descriptografar(0, "CRIPTOGRAFIA E ESCONDER MENSAGENS") == "CRIPTOGRAFIA E ESCONDER MENSAGENS", "A mensagem 'CRIPTOGRAFIA E ESCONDER MENSAGENS' foi descriptografada de 'CRIPTOGRAFIA E ESCONDER MENSAGENS'"
