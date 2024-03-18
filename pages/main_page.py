from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class MainPage(BasePage):
    LOCATOR_CATALOG_BUTTON = (By.CSS_SELECTOR, 'button.nav-element__burger')
    LOCATOR_SPORT_CATEGORY_LINK = (By.XPATH, "//a[contains(@class, 'menu-burger__main-list-link--784')]")

    def open_sport_category(self):
        catalog_button = self.element_is_visible(self.LOCATOR_CATALOG_BUTTON)
        catalog_button.click()

        # Выбираем категорию "Спорт"
        sport_category_link = self.element_is_visible(self.LOCATOR_SPORT_CATEGORY_LINK)
        sport_category_link.click()
