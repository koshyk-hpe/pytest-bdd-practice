import logging

log = logging.getLogger(__name__)


class Calculator:
    def add(self, a, b):
        return a + b


def test_addition():
    log.info("Inside test")
    calculator = Calculator()
    result = calculator.add(2, 3)
    assert result == 5
