import logging

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

scenarios("calculator_tag.feature")
log = logging.getLogger(__name__)


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Invalid input: Only numbers are allowed")
        self.result = a + b

    def subtract(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Invalid input: Only numbers are allowed")
        self.result = a - b


@pytest.fixture
def calculator():
    return Calculator()


@given("the calculator is reset")
def reset_calculator(calculator):
    log.info("resetting the calc - pre req")
    calculator.result = 0


@when(parsers.parse("I add {a} and {b}"))
def add_numbers(calculator, a, b):
    log.info("adding - step")
    try:
        a = int(a) if a.isdigit() else a
        b = int(b) if b.isdigit() else b
        calculator.add(a, b)
    except ValueError:
        calculator.result = "error"


@when(parsers.parse("I subtract {b} from {a}"))
def subtract_numbers(calculator, a, b):
    log.info("subtracting - step")
    try:
        a = int(a) if a.isdigit() else a
        b = int(b) if b.isdigit() else b
        calculator.subtract(a, b)
    except ValueError:
        calculator.result = "error"


@then(parsers.parse("the result should be {expected}"))
def check_result(calculator, expected):
    log.info("validation - result")
    if expected == "error":
        assert calculator.result == "error"
    else:
        assert calculator.result == int(expected)
