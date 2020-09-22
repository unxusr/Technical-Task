from selenium import webdriver

@given(u'i logged in successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i logged in successfully')


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

