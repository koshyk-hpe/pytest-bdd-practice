Feature: Basic Calculator

  Scenario Outline: Addition of numbers
    Given the calculator is reset
    When I add <a> and <b>
    Then the result should be <expected>

    Examples:
      | a  | b  | expected |
      | 2  | 3  | 5        |
      | 10 | 15 | 25       |
      | 7  | 8  | 15       |

  Scenario Outline: Subtraction of numbers
    Given the calculator is reset
    When I subtract <b> from <a>
    Then the result should be <expected>

    Examples:
      | a  | b  | expected |
      | 8  | 5  | 3        |
      | 20 | 7  | 13       |
      | 50 | 20 | 30       |
