Feature: Basic Calculator

  Scenario: Addition of two numbers
    Given the calculator is reset
    When I add 2 and 3
    Then the result should be 5