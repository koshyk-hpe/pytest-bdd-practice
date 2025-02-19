import logging

from pytest_bdd import given, scenario, then, when

log = logging.getLogger(__name__)


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b


calculator = Calculator()


@scenario("calculator_with.feature", "Addition of two numbers")
def test_addition():
    pass


@given("the calculator is reset")
def reset_calculator():
    log.info("resetting calc - pre condition")
    calculator.result = 0


@when("I add 2 and 3")
def add_numbers():
    log.info("adding numbers - step")
    calculator.add(2, 3)


@then("the result should be 5")
def check_result():
    log.info("validation - expected result")
    assert calculator.result == 5
