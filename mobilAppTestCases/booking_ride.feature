Feature: Book a ride
	Scenario: Book a ride while mobile location is turned off
		Given I turned off my device location
		When I go to book a ride
		Then I see a message telling me that the device location is off
		And I press on where to input field
		And I see my location is not detected
		And I have to insert pickup point manually 
		And I insert Where to? 
		And I see available ride locations and times from the same pickup point i inserted before


