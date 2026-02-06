from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on sign in icon')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Sign in message is shown')
def verify_sign_in_msg(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
    assert 'Sign in or create account' in actual_text, f"Expected 'Sign in or create account' text not in {actual_text}"