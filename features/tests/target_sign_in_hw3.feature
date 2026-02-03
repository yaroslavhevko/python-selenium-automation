# Created by yaroslavhevko at 1/31/26
Feature: Test case for Sign In

  Scenario: User can see Sign in message
    Given Open Target main page
    When Click on account icon
    And Click on sign in icon
    Then Sign in message is shown
