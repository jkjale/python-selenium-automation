Feature: Target Help page functionality

#  Scenario: User can view the UI layout of Help page
#    Given Open help.target.com/help
#    Then "Target Help" header is shown
#    And Search input is shown
#    And Search icon is shown
#    And "What would you like to do" section is shown
#    And "contact us" and "product recalls" section is shown
#    And "Browse all Help pages" header is shown


  Scenario Outline: User can select all Help topics in Returns page
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic <dropdown_option>
    Then Verify help <header> page opened
    Examples:
      | dropdown_option      | header             |
      | Promotions & Coupons | Current promotions |
      | Orders & Purchases   | Print a receipt    |
