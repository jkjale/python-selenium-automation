Feature: Verify there are at least 10 benefit cells on Circle page

  @smoke
  Scenario: User can see at least 10 benefit cells
    Given Open Target.com/circle
    Then At least 10 benefit cells are shown