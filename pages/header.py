from selenium.webdriver.common.by import By
from time import sleep
from features.steps.target_header_steps import SEARCH_FIELD
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")

    def search(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)
        sleep(10)

    def click_cart(self):
        self.click(*self.CART_ICON)




