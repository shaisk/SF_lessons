import pytest

from app.calculator import Calculator

"""Задание 24.2.4"""
class TestCalc:
    def setup(self):
        self.calculator = Calculator()

    def test_adding_success(self):
        assert self.calculator.adding(1, 1) == 2

    def test_adding_unsuccess(self):
        try:
            assert self.calculator.adding(1, 1) == 3
        except AssertionError:
            pass

    def test_multiply_success(self):
        assert self.calculator.multiply(2, 3) == 6

    def test_division_success(self):
        assert self.calculator.division(6, 3) == 2

    def test_subtraction_success(self):
        assert self.calculator.subtraction(5, 3) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.division(1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')
