from behave import given, when, then, step
from easyselenium import *

@given('a login page')
def step_goto_login(context):
    goto("http://localhost:8000/")

@when('I input {value} as username')
def step_input_username(context, value):
    inputText('#user', value)

@when('{value} as password')
def step_input_password(context, value):
    inputText('#pass', value)

@when('click the Submit button')
def step_submit(context):
    click('body > form > div:nth-child(4) > button')

@then('the page should go to {page}')
def step_submit(context, page):
    assert page in driver.current_url
        
@then('show {content}')
def step_check_page(context, content):
    assert getText('body > div:nth-child(2)') == content

def after_all(context):
    driver.close()

