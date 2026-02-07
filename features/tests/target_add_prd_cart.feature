# Created by yaroslavhevko at 2/3/26
Feature: Test case to add any Target’s product into the cart

  Scenario: User can see empty cart
    Given Open Target main page
    When Click on cart icon
    Then Empty Cart message is shown

  Scenario: User can add a product to cart
    Given Open Target main page
    When Search for pen
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigates
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify product in cart is correct
