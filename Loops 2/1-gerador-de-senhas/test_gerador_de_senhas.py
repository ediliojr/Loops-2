import pytest

from gerador_de_senhas import (password_generator)

def test_size():
  assert len(password_generator(10)) == 10
  assert len(password_generator(5)) == 5
  assert len(password_generator(0)) == 0

def test_type():
  assert type(password_generator(10)) == type("string")

def test_only_letters():
  assert password_generator(5).isalpha()
