import logging

from pytest_bdd import given, parsers, scenarios, then, when

log = logging.getLogger(__name__)


scenarios("calculator_param.feature")


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
    log.info("resetting calc - pre req")
    calculator.result = 0


@when(parsers.cfparse("I add {a:d} and {b:d}"))
def add_numbers(a: int, b: int):
    log.info("adding - step")
    calculator.add(a, b)


@when(parsers.cfparse("I subtract {b:d} from {a:d}"))
def subtract_numbers(a: int, b: int):
    log.info("subtracting - step")
    calculator.subtract(a, b)


@then(parsers.cfparse("the result should be {expected:d}"))
def check_result(expected: int):
    log.info("validation - result")
    assert calculator.result == expected
