from asyncio import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class, 'styles_listingPageResultsCount')]")
PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-test="@web/ProductCard/title"]')
LISTINGS = (By.CSS_SELECTOR, '[data-test="@web/site-top-of-funnel/ProductCardWrapper"]')
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')


@when('Show product results list')
def show_results_list(context):
    results = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='lp-resultsCount']")


@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
   context.app.search_results_page.verify_search_results()


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):

    products = context.driver.find_elements(*LISTINGS)

    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(f'-{title}')
        product.find_element(*PRODUCT_IMG)
