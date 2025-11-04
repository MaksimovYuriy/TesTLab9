import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from calculator import Calculator

class TestCalculator:
    @pytest.fixture
    def calc(self):
        return Calculator()

    def test_add_positive_numbers(self, calc):
        assert calc.add(2, 3) == 5
        assert calc.add(10, 15) == 25

    def test_add_negative_numbers(self, calc):
        assert calc.add(-2, -3) == -5
        assert calc.add(-10, 5) == -5

    def test_add_float_numbers(self, calc):
        assert calc.add(2.5, 3.7) == pytest.approx(6.2)
        assert calc.add(0.1, 0.2) == pytest.approx(0.3)

    def test_add_invalid_input(self, calc):
        with pytest.raises(ValueError):
            calc.add("2", 3)
        with pytest.raises(ValueError):
            calc.add(2, "3")

    def test_subtract_positive_numbers(self, calc):
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(10, 15) == -5

    def test_subtract_negative_numbers(self, calc):
        assert calc.subtract(-2, -3) == 1
        assert calc.subtract(-10, 5) == -15

    def test_multiply_positive_numbers(self, calc):
        assert calc.multiply(2, 3) == 6
        assert calc.multiply(10, 0) == 0

    def test_multiply_negative_numbers(self, calc):
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(-2, -3) == 6

    # Тесты для метода divide
    def test_divide_positive_numbers(self, calc):
        assert calc.divide(6, 3) == 2
        assert calc.divide(5, 2) == 2.5

    def test_divide_by_zero(self, calc):
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            calc.divide(5, 0)

    def test_divide_negative_numbers(self, calc):
        assert calc.divide(-6, 3) == -2
        assert calc.divide(6, -3) == -2

    def test_power_positive_exponent(self, calc):
        assert calc.power(2, 3) == 8
        assert calc.power(5, 2) == 25

    def test_power_zero_exponent(self, calc):
        assert calc.power(5, 0) == 1
        assert calc.power(0, 0) == 1

    def test_power_negative_exponent(self, calc):
        assert calc.power(2, -1) == 0.5
        assert calc.power(4, -2) == 0.0625

    # Тесты для метода is_even
    def test_is_even_positive_numbers(self, calc):
        assert calc.is_even(4) == True
        assert calc.is_even(7) == False

    def test_is_even_negative_numbers(self, calc):
        assert calc.is_even(-4) == True
        assert calc.is_even(-7) == False

    def test_is_even_zero(self, calc):
        assert calc.is_even(0) == True

    def test_is_even_invalid_input(self, calc):
        with pytest.raises(ValueError):
            calc.is_even(2.5)
        with pytest.raises(ValueError):
            calc.is_even("2")

@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.add(a, b) == expected


@pytest.mark.parametrize("number,expected", [
    (2, True),
    (3, False),
    (0, True),
    (-2, True),
    (-3, False),
])
def test_is_even_parameterized(number, expected):
    calc = Calculator()
    assert calc.is_even(number) == expected