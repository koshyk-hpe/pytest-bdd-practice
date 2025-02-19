import logging

from pytest_bdd import given, parsers, scenarios, then, when

scenarios("calculator_with.feature")
log = logging.getLogger(__name__)


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b

    def subtract(self, a, b):
        self.result = a - b


calculator = Calculator()


@given("the calculator is reset")
def reset_calculator():
    log.info("resetting the calc - pre req")
    calculator.result = 0


@when(parsers.parse("I add {a:d} and {b:d}"))
def add_numbers(a, b):
    log.info("adding - step")
    calculator.add(a, b)


@when(parsers.parse("I subtract {b:d} from {a:d}"))
def subtract_numbers(a, b):
    log.info("subtracting - step")
    calculator.subtract(a, b)


@then(parsers.parse("the result should be {expected:d}"))
def check_result(expected):
    log.info("validation - result")
    assert calculator.result == expected
