from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

ADD_TO_CART_BTN =(By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN =(By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCartButton']") #  [data-test='content-wrapper'] [id*='addToCartButton']  shoul be like that but error pop up
SIDE_NAV_PROD_NAME =(By.XPATH, "//*[@data-test='content-wrapper']//h4")  #By.CSS_SELECTOR, "[data-test='content-wrapper'] h4" has before


@when('Click on Add to Cart button')
def click_on_add_to_cart(context):
    sleep(7)
    context.driver.find_element(*ADD_TO_CART_BTN).click()

    context.driver.wait.until(
        EC.element_to_be_clickable(ADD_TO_CART_BTN),
        message='Side navigate to Add to Cart not clickable'
    )

    elements = context.driver.find_elements(*ADD_TO_CART_BTN)
    element = elements[-1]
    element.click()


@when('Store product name')
def store_product_name(context):
    context.product = context.driver.find_element(*SIDE_NAV_PROD_NAME).text
    context.driver.wait.until(
        EC.element_to_be_clickable(SIDE_NAV_PROD_NAME),
        message='Store product name not found'
    )




@when('Confirm Add to Cart button from side navigates')
def side_nav_click_add_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()











@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'
    sleep(10)



