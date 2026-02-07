from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


TOTAL_AMOUNT = (By.CSS_SELECTOR, "h2 [class*='styles_cart-summary-span']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.target.com/cart')



@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.driver.wait.until(
        EC.presence_of_element_located(TOTAL_AMOUNT),
        message='Subtotal text did not appear'
    )

    cart_summary = context.driver.find_element(*TOTAL_AMOUNT).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} item not in cart summary"

@then('Verify product in cart is correct')
def verify_product(context):
    actual =context.driver.find_element(*PRODUCT_NAME).text
    expected =context.product
    assert actual[:20] == expected[:20],\
        f'Expected product {expected[:20]} but got {actual[:20]}'



@then('Empty Cart message is shown')
def verify_empty_cart_msg(context):
   context.app.cart_page.verify_empty_cart_msg()

   # actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    #assert 'Your cart is empty' in actual_text, f"Expected 'Your cart is empty' text not in {actual_text}"
