# Created by manic at 11/9/2023
Feature: Verification tests
  # Enter feature description here

  Scenario: Verify empty cart presence
      Given Open target main page
      When Click on cart icon
      Then Verify cart is empty message shown

  @smoke
  Scenario: Verify Sign in
      Given Open target main page
      When Click on Sign In
      When Click on Menu Sign In
      Then Verify Sign In page opens


  Scenario: Verify Product in Cart
    Given Open Target main page
    When Search for Vortex Pro Air Fryer
    And Add product to cart
    Then Verify Vortex Pro Air Fryer in cart


  Scenario: Verify Benefit Boxes
    Given Open Target Circle page
    Then Verify 5 Benefit Boxes are present


  Scenario: Verify User can Login
    Given Open target main page
    When Click on Sign In
    And Click on Menu Sign In
    And Input Username and Password
    Then Verify User is logged in

  @smoke
  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    When Store original windows
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original

    @smoke
    Scenario: Verify User is unable to login with incorrect credentials
      Given Open sign in page
      When Input Username and Password
      Then Verify User cannot log in
