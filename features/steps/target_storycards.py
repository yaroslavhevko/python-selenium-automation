from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
SEARCH_ICON = (By.CSS_SELECTOR, "[data-lnk='@web/SlingshotComponents/common/Storyblock']")


@given('Open Target circle page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')



@when('Find Unlock added value')
def find_unlock_add_value(context):
    context.driver.find_element(By.XPATH, "//h2[text()='Unlock added value']")


@then('Circle messages is shown')
def verify_circle_msg(context):
   links = context.driver.find_elements(*SEARCH_ICON)
   print(links)