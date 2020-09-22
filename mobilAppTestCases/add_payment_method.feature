Feature: Add payment method
	Scenario: Add card as new payment method
		Given I pressed on the menu icon
		When I press on "Payment" 
		Then I see "Add Card" title
		And I enter my card number in "Card Number" field
		And I enter card expiry month in "Expiry Month" field
		And I enter card expiry year in "Expiry Year" field
		And I enter name on the card in "Card Holder" field
		And I enter card CVC in "CVC" field
		And I submit data by pressing "NEXT" button
		Then I see my the card added successfully
		And I see last four numbers only of my card
