from pytest_bdd import given, scenarios, then, when


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b


calculator = Calculator()

scenarios("calculator_short.feature")


@given("the calculator is reset")
def reset_calculator():
    calculator.result = 0


@when("I add 2 and 3")
def add_numbers():
    calculator.add(2, 3)


@then("the result should be 5")
def check_result():
    assert calculator.result == 5
