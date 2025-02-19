Feature: Calculator Operations

  Scenario Outline: Addition operation
    Given the calculator is reset
    When I add <a> and <b>
    Then the result should be <expected>

    @positive
    Examples: Valid Cases
      | a  | b  | expected |
      | 5  | 3  | 8        |
      | 10 | 2  | 12       |
      | 7  | 8  | 15       |

    @negative
    Examples: Invalid Cases
      | a   | b   | expected |
      | "x" | 3   | error    |
      | 5   | "y" | error    |
      | None | 4  | error    |

  Scenario Outline: Subtraction operation
    Given the calculator is reset
    When I subtract <b> from <a>
    Then the result should be <expected>

    @positive
    Examples: Valid Cases
      | a  | b  | expected |
      | 8  | 5  | 3        |
      | 20 | 7  | 13       |
      | 50 | 20 | 30       |

    @negative
    Examples: Invalid Cases
      | a   | b   | expected |
      | "x" | 5   | error    |
      | 10  | "y" | error    |
      | None | 3  | error    |
