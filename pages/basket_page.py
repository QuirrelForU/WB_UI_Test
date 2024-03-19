from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    # Locators

    LOCATOR_ITEM_COUNT_HEADER = (By.CSS_SELECTOR, 'h1.basket-section__header')

    def get_items_count(self):
        header_element = self.element_is_visible(self.LOCATOR_ITEM_COUNT_HEADER)
        count = header_element.get_attribute('data-count')
        return count
