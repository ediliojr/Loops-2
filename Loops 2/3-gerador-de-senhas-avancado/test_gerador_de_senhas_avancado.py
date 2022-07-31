import pytest

from gerador_de_senhas_avancado import (advanced_password_generator)

def test_size():
  assert len(advanced_password_generator(10)) == 10
  assert len(advanced_password_generator(5)) == 5
  assert len(advanced_password_generator(0)) == 0

def test_type():
  assert type(advanced_password_generator(10)) == type("string")

def test_not_only_letters():
  assert not advanced_password_generator(5).isalpha()
