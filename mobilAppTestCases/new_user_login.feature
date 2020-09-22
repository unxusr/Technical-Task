Feature: Login with social network account
	Scenario: New user login with facebook
		Given I open the app for the first time
		When I press on Facebook login button
		Then The app request access to my Facebook profile informations
		And I press continue as my user
		And I redirected to the app home page
		And I see my Facebook photo and name in the side menu


