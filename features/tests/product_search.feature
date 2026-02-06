Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Target main page
    When Input Coffee into search field
    And Click on search icon
    And Show product results list
    Then Product results for Coffee are shown



  Scenario: User can search for a product
    Given Open Target main page
    When Input Lego into search field
    And Click on search icon
    And Show product results list
    Then Product results for Lego are shown



  Scenario: User can search for a product
    Given Open Target main page
    When Input Milk into search field
    And Click on search icon
    And Show product results list
    Then Product results for Milk are shown
    