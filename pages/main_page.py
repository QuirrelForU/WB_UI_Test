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
