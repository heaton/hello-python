Feature: Login

  In order to use the system normally
  As a user
  I want to see my dashborad after I login the system successfully

  Scenario: A normal user logins
    Given a login page
    When I input user1 as username
    And pass1 as password
    And click the Submit button
    Then the page should go to main.html
    And show This is your dashboard!

