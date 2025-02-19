Feature: Basic Calculator

  Scenario: Addition of two numbers
    Given the calculator is reset
    When I add 2 and 3
    Then the result should be 5

  Scenario: Addition of other numbers
    Given the calculator is reset
    When I add 10 and 15
    Then the result should be 25

  Scenario: Subtraction of two numbers
    Given the calculator is reset
    When I subtract 7 from 10
    Then the result should be 3
