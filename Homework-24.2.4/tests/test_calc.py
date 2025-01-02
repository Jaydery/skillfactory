from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calculator = Calculator

    def test_multiply_success(self):
        assert self.calculator.multiply(self, 2, 3) == 6

    def test_division_success(self):
        assert self.calculator.division(self, 8, 2) == 4

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 3, 1) == 2

    def test_adding_success(self):
        assert self.calculator.adding(self, 1, 1) == 2

    def teardown(self):
        print(' - проведено тестов')