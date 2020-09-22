from selenium import webdriver
import os
import time

@given(u'i logged in successfully')
def login(context):
    
    # Init web driver
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(3)
    context.browser.get("https://gist.github.com")

    # Init credentials
    git_user = os.environ.get("username")
    git_password = os.environ.get("password")

    # Login form interaction
    sign_in_btn = context.browser.find_element_by_xpath("/html/body/div[1]/div/div[5]/a[1]").click()
    username = context.browser.find_element_by_xpath('//*[@id="login_field"]').send_keys(git_user)
    password = context.browser.find_element_by_xpath('//*[@id="password"]').send_keys(git_password)
    sign_in_form_btn = context.browser.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[9]').click()

    # Login assertion
    assert context.browser.find_element_by_xpath('//*[@id="user-links"]/details/details-menu/div[1]/a').get_attribute('href').split('com')[1].split('/')[1]  == git_user


@when(u'i create a gist')
def step_impl(context):
    raise NotImplementedError(u'STEP: When i create a gist')


@then(u'i should be able to edit the gist')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then i should be able to edit the gist')


@then(u'i should be able to post a comments')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then i should be able to post a comments')


@then(u'i can delete a comment successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then i can delete a comment successfully')

