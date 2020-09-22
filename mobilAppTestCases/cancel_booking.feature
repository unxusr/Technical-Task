Feature: Cancel booking
	Scenario: Book a ride and cancel it right after
		Given I booked a ride
		When I press on "Track active ride"
		Then I swipe up to see the cancel button
		And I Press the cancel button
		And I get a confirmation message for charging 0 for canceling trip 
		And I press "CANCEL TRIP" 
		And Trip canceled successfully


