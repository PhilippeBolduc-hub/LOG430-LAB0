"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import math
from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

def test_addition_basic():
    calc = Calculator()
    assert calc.addition(2, 3) == 5

def test_addition_zero():
    calc = Calculator()
    assert calc.addition(0, 5) == 5
    assert calc.addition(0, 0) == 0
    assert calc.addition(5, 0) == 5

def test_addition_negative():
    calc = Calculator()
    assert calc.addition(-2, 3) == 1
    assert calc.addition(-2, -3) == -5
    assert calc.addition(2, -3) == -1

def test_addition_floats():
    calc = Calculator()
    assert calc.addition(10.3, 11.5) == 21.8

def test_addition_negative_floats():
    calc = Calculator()
    assert calc.addition(-10.3, -11.5) == -21.8

def test_subtraction_basic():
    calc = Calculator()
    assert calc.subtraction(9, 4) == 5

def test_subtraction_zero():
    calc = Calculator()
    assert calc.subtraction(0, 5) == -5
    assert calc.subtraction(0, 0) == 0
    assert calc.subtraction(5, 0) == 5

def test_subtraction_negative():
    calc = Calculator()
    assert calc.subtraction(-2, 3) == -5
    assert calc.subtraction(-2, -3) == 1
    assert calc.subtraction(2, -3) == 5

def test_subtraction_floats():
    calc = Calculator()
    result = calc.subtraction(10.3, 11.5)
    assert math.isclose(result, -1.2, rel_tol=1e-9)

def test_subtraction_negative_floats():
    calc = Calculator()
    result = calc.subtraction(-10.3, -11.5)
    assert math.isclose(result, 1.2, rel_tol=1e-9)

def test_multiplication_basic():
    calc = Calculator()
    assert calc.multiplication(8, 4) == 32

def test_multiplication_zero():
    calc = Calculator()
    assert calc.multiplication(0, 5) == 0
    assert calc.multiplication(0, 0) == 0
    assert calc.multiplication(5, 0) == 0

def test_multiplication_negative():
    calc = Calculator()
    assert calc.multiplication(-2, 3) == -6
    assert calc.multiplication(-2, -3) == 6
    assert calc.multiplication(2, -3) == -6

def test_multiplication_floats():
    calc = Calculator()
    result = calc.multiplication(3.3, 4.5)
    assert math.isclose(result, 14.85, rel_tol=1e-9)

def test_multiplication_negative_floats():
    calc = Calculator()
    result = calc.multiplication(-3.3, 4.5)
    assert math.isclose(result, -14.85, rel_tol=1e-9)

def test_division_basic():
    calc = Calculator()
    assert calc.division(8, 4) == 2

def test_division_zero():
    calc = Calculator()
    assert calc.division(0, 5) == 0
    result = calc.division(10, 0)
    assert result == "Erreur : division par zéro"
    assert calc.last_result == "Error"

def test_division_negative():
    calc = Calculator()
    assert calc.division(-6, 3) == -2
    assert calc.division(-6, -3) == 2
    assert calc.division(6, -3) == -2

def test_division_floats():
    calc = Calculator()
    result = calc.division(11.5, 2)
    assert math.isclose(result, 5.75, rel_tol=1e-9)

def test_division_negative_floats():
    calc = Calculator()
    result = calc.division(-11.5, 2)
    assert math.isclose(result, -5.75, rel_tol=1e-9)






# TODO: ajoutez les tests