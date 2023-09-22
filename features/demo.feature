Feature: Alerts

  @tag1
  Scenario: accept simple alert
    Given the user is in main page
    When the user clicks the simple alert button
    And the user accepts the alert
    Then the message "You successfully clicked an alert" is displayed


  Scenario Outline: accept accept/dismiss alert
    Given the user is in main page
    When the user clicks the accept/dismiss alert button
    And the user <accion> the alert
    Then the message "<message>" is displayed

    Examples:
      | accion  | message             |
      | accepts | You clicked: Ok     |
      | dismiss | You clicked: Cancel |