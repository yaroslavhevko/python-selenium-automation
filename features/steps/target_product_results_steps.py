from asyncio import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@when('Show product results list')
def show_results_list(context):
    results = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='lp-resultsCount']")
