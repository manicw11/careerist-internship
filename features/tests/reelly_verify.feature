# Created by manic at 12/19/2023
Feature: Reelly verification tests
  # Enter feature description here

  Scenario: Verify the Connect The Company tab opens
    Given Open Reelly main page
    And Verify Sign In page opens
    When Input Reelly Username and Password
    And Verify Login is successful
    And Store original windows
    And Click on Connect The Company
    And Switch to the newly opened window
    Then Verify Connect The Company tab opens