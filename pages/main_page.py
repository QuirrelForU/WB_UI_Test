from selenium.webdriver import Keys

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    # Locators

    LOCATOR_CATALOG_BUTTON = (By.CSS_SELECTOR, 'button.nav-element__burger')

    LOCATOR_SPORT_CATEGORY_LINK = (By.XPATH, "//a[contains(@class, 'menu-burger__main-list-link--784')]")
    LOCATOR_SHOES_CATEGORY_LINK = (By.XPATH, "//a[contains(@class, 'menu-burger__main-list-link--629')]")
    LOCATOR_HOUSE_CATEGORY_LINK = (By.XPATH, "//a[contains(@class, 'menu-burger__main-list-link--258')]")
    LOCATOR_FURNITURE_CATEGORY_LINK = (By.XPATH, "//a[contains(@class, 'menu-burger__main-list-link--62827')]")
    LOCATOR_BOOKS_CATEGORY_LINK = (By.XPATH, "//a[contains(@class, 'menu-burger__main-list-link--519')]")

    LOCATOR_SEARCH_INPUT = (By.ID, "searchInput")
    LOCATOR_SEARCH_APPLY_BUTTON = (By.ID, "applySearchBtn")
    LOCATOR_SEARCH_CLEAR_BUTTON = (By.CLASS_NAME, "search-catalog__btn--clear")

    def open_sport_category(self):
        catalog_button = self.element_is_visible(self.LOCATOR_CATALOG_BUTTON)
        catalog_button.click()

        sport_category_link = self.element_is_visible(self.LOCATOR_SPORT_CATEGORY_LINK)
        sport_category_link.click()

    def open_shoes_category(self):
        catalog_button = self.element_is_visible(self.LOCATOR_CATALOG_BUTTON)
        catalog_button.click()

        shoes_category_link = self.element_is_visible(self.LOCATOR_SHOES_CATEGORY_LINK)
        shoes_category_link.click()

    def open_house_category(self):
        catalog_button = self.element_is_visible(self.LOCATOR_CATALOG_BUTTON)
        catalog_button.click()

        house_category_link = self.element_is_visible(self.LOCATOR_HOUSE_CATEGORY_LINK)
        house_category_link.click()

    def open_furniture_category(self):
        catalog_button = self.element_is_visible(self.LOCATOR_CATALOG_BUTTON)
        catalog_button.click()

        furniture_category_link = self.element_is_visible(self.LOCATOR_FURNITURE_CATEGORY_LINK)
        furniture_category_link.click()

    def open_books_category(self):
        catalog_button = self.element_is_visible(self.LOCATOR_CATALOG_BUTTON)
        catalog_button.click()

        books_category_link = self.element_is_visible(self.LOCATOR_BOOKS_CATEGORY_LINK)
        books_category_link.click()

    def search_item_enter(self, search_input):
        search_bar = self.element_is_visible(self.LOCATOR_SEARCH_INPUT)
        search_bar.clear()
        search_bar.send_keys(search_input)
        search_bar.send_keys(Keys.ENTER)

    def search_item_button(self, search_input):
        search_bar = self.element_is_visible(self.LOCATOR_SEARCH_INPUT)
        search_bar.clear()
        search_bar.send_keys(search_input)
        search_button = self.element_is_visible(self.LOCATOR_SEARCH_APPLY_BUTTON)
        search_button.click()

    def search_clear_button(self):
        search_bar = self.element_is_visible(self.LOCATOR_SEARCH_INPUT)
        search_bar.clear()
        search_bar.send_keys('Test string that will be deleted in test')
        search_clear_button = self.element_is_visible(self.LOCATOR_SEARCH_CLEAR_BUTTON)
        search_clear_button.click()
        return search_bar.get_attribute("value")
