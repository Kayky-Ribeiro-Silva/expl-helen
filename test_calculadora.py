from calculadora import somar, dividir
import pytest

def test_somar():
    resultado = somar(5, 3)
    assert resultado == 8

def test_dividir():
    resultado = dividir(10, 2)
    assert resultado == 5

def test_dividir_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)