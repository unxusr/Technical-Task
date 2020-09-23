# Technical-Task

Automate Gist web UI, REST APIs and mobile app test cases


## Assumptions 
1- By looking into REST API documentation i found it has too many components and APIs, so i picked Gist APIs as i'm testing Gist webUI so i assumed testing one component as frontend and backend will be better.

2- `test_fork_gist` API request not allowed by gist owner so i passed it by `pass` statment after testing it for one time for other's gist, I assume to put another gist ID in that request before running.

3- Because it is my github personal account so i changed the password that has been commited before (that was to run tests in travis CI), i assume task reviewer to use his own github credentials (username, password and personal access token), However i kept the generated token in the .env file but with a lower privileges.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages in the requirements.txt.

```bash
pip3 install -r requirements.txt
```

## gistWebUI
This automation test is written in BDD style (Behavior Driven Development).

Consisting of a feature file and steps file using behave and selenium webdriver to run the test

### Gist web UI incident
Due to too many retries on Gist UI and their highly secured system, their spam detecting system detected unusual behavior and blocked my testing account `hellotstr` , therefore i had to work around the issue and used fake sentence and words generated every time the test runs in creating gists and comments but i can't take the risk to give more retries even with fake to not blocking my personal account.

### Explain work around step
In the last step of deleting comment it was hard to get the delete button and clicking it, I tried many different ways to get it work so github spam detecting system flagged my testing account and detected my real personal account too.

By contacting their support they explained the incident and asked me to delete the testing account as their Terms of Service only allow folks a single one.
Therefore i work around that and made api calls in deleting comment step which are `get gist comments` and get the last created one then call `delete gist comment` by its id, this required to get gist id in the first step `create_public_gist` and save it in a global variable to be able to call it in the last method.

### Usage
```shell
# run from repository parent directory
cd Technical-Task
source .env  # needed for a work around step
behave gistWebUI/ 
```

## gistAPI
### Usage
This component writen in python 3 and using unittest lib.

```shell
cd Technical-Task/gistAPI
python3 gists.py
```

## Mobile app test cases
Android platform used in writing test cases.

Test cases written in Gherkin format (BDD style)

It consisting of 4 test cases:
```bash
new_user_login
booking_ride
cancel_booking
add_payment_method
```
### Scenario
A new user login with Facebook account, authorize the app on user's Facebook and asserting it login successfully,

After login successfully booking a ride and device location is turned off, 

Then we can cancel the ride safely as long as we didnt reached the take off time,

Then adding a payment method to the account by filling card details form.

## Bug reporting

**What happens?**

While booking a ride and the device location is turned off found far pickup points from the one inserted manually.

**Expected result:**

To get all available pickup points near to the one that inserted manually.

**Actual result:**

Got far away pickup points from the one inserted manually

**Steps to reproduce:**

1. Turn off device location
2. Open the app
3. Press on "Where to?" field
4. Enter pickup point manually
5. Enter drop off location

## CI/CD
 Travis CI used for this project
Biuld passes for Gist API automation test

https://travis-ci.com/unxusr/Technical-Task.svg?token=pFhfWX7qD8yNqhxyxRDy&branch=master
