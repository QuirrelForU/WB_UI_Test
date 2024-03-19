from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    # Locators

    LOCATOR_ITEM_COUNT_HEADER = (By.CSS_SELECTOR, 'h1.basket-section__header')
    LOCATOR_ITEM_PLUS = (By.CLASS_NAME, "count__plus")
    LOCATOR_ITEM_MINUS = (By.CLASS_NAME, "count__minus")

    def get_items_count(self):
        header_element = self.element_is_visible(self.LOCATOR_ITEM_COUNT_HEADER)
        count = header_element.get_attribute('data-count')
        return count

    def item_plus(self, count=1):
        item_plus_button = self.element_is_visible(self.LOCATOR_ITEM_PLUS)
        for _ in range(count):
            item_plus_button.click()

    def item_minus(self, count=1):
        item_minus_button = self.element_is_visible(self.LOCATOR_ITEM_MINUS)
        for _ in range(count):
            item_minus_button.click()

    def item_delete(self):
        pass
