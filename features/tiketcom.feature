Feature: Tiket.com Test
  Scenario: Product Train
    Given launch Chrome browser
    When Open Tiket.com homepage
    And Select "Kereta Api" Menu
    And Select Origin Station
    And Select Destination
    And Select Departure Time
    And Set 3 Adults & 2 infants pax
    And Press Search Button
    And Select Train Class, Time departure, Train name
    And Input Pax Data
    And Select Seats
    And Select Payment Method
    Then Verify payment
    And Close Browser

  Scenario: Product Plane
    Given Relaunch Chrome browser
    When Open homepage
    And Login with email
    And Select "Pesawat" Menu
    And Select "Pulang-pergi" Option
    And Select Origin Point
    And Select Destination Point
    And Select Departure date
    And Select Comeback Date
    And Select Pax & Class
    And Search Route
    And Select flight
    And Select flight home
    And Go to Pax Detail Page
    And Input Pax Info
    And Select Payment Method with Virtual Account
    Then Complete the order
    And Logout
    And Close the Browser


