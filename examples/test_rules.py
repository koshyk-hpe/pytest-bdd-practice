import logging

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

log = logging.getLogger(__name__)

scenarios("calculator_rules.feature")


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result += a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result


@pytest.fixture
def calculator():
    return Calculator()


@given("a calculator", target_fixture="calculator_instance")
def given_calculator(calculator):
    log.info("resetting the calc - pre req")
    calculator.result = 0
    return calculator


@when(parsers.parse("I add {a:d} and {b:d}"), target_fixture="result")
def add_numbers(calculator_instance, a, b):
    log.info("adding - test step")
    return calculator_instance.add(a, b)


@when("I add the following numbers:", target_fixture="total_sum")
def add_multiple_numbers(calculator_instance, datatable):
    log.info("adding - test step")
    for row in datatable[1:]:
        calculator_instance.add(int(row[0]), int(row[1]))
    return calculator_instance.result


@when(parsers.parse("I subtract {b:d} from {a:d}"), target_fixture="result")
def subtract_numbers(calculator_instance, a, b):
    log.info("subtracing - test step")
    return calculator_instance.subtract(a, b)


@then(parsers.parse("the result should be {expected:d}"))
def check_result(result, expected):
    log.info("validation - result")
    assert result == expected


@then(parsers.parse("the total sum should be {expected:d}"))
def check_total_sum(total_sum, expected):
    log.info("validation - result")
    assert total_sum == expected
