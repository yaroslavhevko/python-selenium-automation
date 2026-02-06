from asyncio import sleep
from pyexpat.errors import messages

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

from features.steps.target_storycards import SEARCH_ICON

SEARCH_FIELD =(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
SEARCH_BUTTON =(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")



@when('Click on account icon')
def click_account(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()

@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()

@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_FIELD)
    search.clear()
    search.send_keys(search_word)
    search.clear()
    search.send_keys(search_word)


@when('Search for {product}')
def search_for_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BUTTON).click()
    context.driver.wait.until(
        EC.presence_of_element_located(SEARCH_FIELD),
        message='Search query not found'
    )
    context.driver.wait.until(
        EC.presence_of_element_located(SEARCH_BUTTON),
    message='Search not found'
    ).click()





@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    context.driver.wait.until(
        EC.presence_of_element_located(SEARCH_FIELD),
        message='Search icon not found'
    )



@when('Search item ')
def search_item(context):
    context.driver.get('https://www.target.com/p/A-83781984')