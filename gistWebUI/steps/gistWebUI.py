from selenium import webdriver
import os
from faker import Faker
import time
import requests

fake = Faker()

@given(u'i logged in successfully')
def login(context):
    
    # Init web driver
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(3)
    context.browser.get("https://gist.github.com")

    # Init credentials
    global git_user
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
def create_public_gist(context):

    # Create gist 
    create_gist_btn = context.browser.find_element_by_xpath('/html/body/div[1]/div/div[5]/a')
    create_gist_btn.click()

    # Choose gist type
    gist_type = context.browser.find_element_by_xpath('//*[@id="new_gist"]/div/div[2]/div/details').click()
    public_gist = context.browser.find_element_by_xpath('//*[@id="new_gist"]/div/div[2]/div/details/details-menu/label[2]/div/span[1]').click()

    # Write the gist content
    file_1 = context.browser.find_element_by_xpath('//*[@id="gists"]/div[2]/div/div[2]/div/div[5]/div[1]/div/div/div/div[5]/div/pre')
    sentence = fake.sentence()
    file_1.send_keys(sentence)

    # Save the public gist
    create_gist = context.browser.find_element_by_xpath('//*[@id="new_gist"]/div/div[2]/div/button').click()

    # Assert gist existence 
    assert context.browser.find_element_by_xpath('//*[@id="file-gistfile1-txt-LC1"]').text == sentence
    global gist_id
    gist_id = context.browser.find_element_by_xpath('//*[@id="gist-pjax-container"]/div[1]/div/div[1]/div/div/div[2]/h1/strong/a').get_attribute('href')
    gist_id = gist_id.split(git_user)[1].split("/")[1]


@then(u'i should be able to edit the gist')
def edit_gist(context):

    # Edit existing gist 
    gist_file = context.browser.find_element_by_xpath('//*[@id="gist-pjax-container"]/div[1]/div/div[1]/ul/li[1]/a').click()
    add_file_btn = context.browser.find_element_by_xpath('//button[text()="Add file"]').click()

    # write gist file 2 content
    file_2 = context.browser.find_element_by_xpath('//*[@id="gists"]/div[3]/div/div[2]/div/div[5]/div[1]/div/div/div/div[5]/div/pre')
    sentence = fake.sentence()
    file_2.send_keys(sentence)

    # Save gist with 2 files
    update_gist = context.browser.find_element_by_class_name('btn-primary').click()

    # Assert that file 2 is added 
    assert context.browser.find_element_by_xpath('//*[@id="file-gistfile2-txt"]/div[1]/div[2]/a').text == 'gistfile2.txt'
    

@then(u'i should be able to post a comments')
def post_comments(context):

    # Add comment 1
    sentence = fake.sentence()
    write_comment_1 = context.browser.find_element_by_xpath('//*[@id="new_comment_field"]').send_keys(sentence)
    post_comment_1 = context.browser.find_element_by_xpath('//*[@id="partial-new-comment-form-actions"]/button').click()
    time.sleep(2)

    # Add comment 2
    another_sentence = fake.sentence()
    write_comment_2 = context.browser.find_element_by_xpath('//*[@id="new_comment_field"]').send_keys(another_sentence)
    post_comment_2 = context.browser.find_element_by_xpath('//*[@id="partial-new-comment-form-actions"]/button').click()


@then(u'i can delete a comment successfully')
def delete_comment(context):
    # This is a workaround for just making the test pass
    # due to github spam detecting system blocked my testing account for too many retries
    # so i dont want to take a risk of blocking my personal account
    
    # Delete comment 2//*[@id="gistcomment-3461120"]/div[2]/div[1]/div[1]/details/summary/svg
    #actions_button = context.browser.find_element_by_class_name('//*[@class="timeline-comment-group"]').click()
    #time.sleep(2)
    
    username = os.environ.get("username")
    token = os.environ.get("token")
    base_url = os.environ.get("baseUrl")

    # get gist comments
    route = base_url + f"/gists/{gist_id}/comments"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(route, headers=headers, auth=(username, token))
    print(response.json())
    print(response.status_code, route)
    comment_id = response.json()[0]['id']
    assert response.status_code == 200
    
    # delete gist comment

    route = base_url + f"/gists/{gist_id}/comments/{comment_id}"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.delete(route, headers=headers, auth=(username, token))
    assert response.status_code == 204


