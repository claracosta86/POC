import pytest
from src.examples import Calculator

# Teste original:

# def test_add():
#    calculator = Calculator()
#    result = Calculator.add(2, 3)
#    assert result == 5 
    
def test_add():
     "Teste para adição de dois inteiros"
     calculator = Calculator()
     result = calculator.add(2, 3)
     assert result == 5

def test_add_negative():
     "Teste para adição de dois inteiros negativos"
     calculator = Calculator()
     result = calculator.add(-2, -3)
     assert result == -5

def test_add_large_numbers():
     "Teste para adição de inteiros extremamente grandes"
     calculator = Calculator()
     result = calculator.add(2147483647, 1)
     assert result == 2147483648

def test_add_extremely_large_numbers():
     "Teste para adição de inteiros extremamente grandes"
     calculator = Calculator()
     result = calculator.add(1073741823, 1073741823)
     assert result == 2147483646

def test_add_zero():
     "Teste para adição com zero"
     calculator = Calculator()
     result = calculator.add(0, 3)
     assert result == 3

def test_add_equal_numbers():
     "Teste para adição de dois inteiros iguais"
     calculator = Calculator()
     result = calculator.add(2, 2)
     assert result == 4

def test_add_overflow():
     "Teste para adição com overflow"
     calculator = Calculator()
     with pytest.raises(OverflowError):
         calculator.add(2147483647999999, 1)
        