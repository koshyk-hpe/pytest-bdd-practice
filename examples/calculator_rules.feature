Feature: Calculator Operations with Rules, Target Fixtures, and DataTables

  Rule: Addition Functionality
    Scenario: Adding two numbers using target fixtures
      Given a calculator
      When I add 5 and 3
      Then the result should be 8

    Scenario: Batch addition of numbers using DataTables
      Given a calculator
      When I add the following numbers:
        | a  | b  |
        | 2  | 3  |
        | 4  | 5  |
        | 7  | 8  |
      Then the total sum should be 29

  Rule: Subtraction Functionality
    Scenario: Subtracting smaller from larger
      Given a calculator
      When I subtract 3 from 7
      Then the result should be 4

    Scenario: Subtracting larger from smaller
      Given a calculator
      When I subtract 10 from 4
      Then the result should be -6
