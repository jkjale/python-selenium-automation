Feature: Product Search functionality

#  Scenario: User can search for a product
#    Given Open Target.com
#    When Search for tea
#    Then Verify search results shown for tea
#    And Verify tea in URL
#
#
#  Scenario: Searched products show name and image
#    Given Open Target.com
#    When Search for tea
#    Then Verify search results shown for tea
#    And Each product's name and image are shown

  @smoke
  Scenario: User can see favorites tooltip for search results
    Given Open Target.com
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown