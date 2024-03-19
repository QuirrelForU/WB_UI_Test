import time
import random
from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TablePage(BasePage):
    # Locators
    SORT_RULES = {'По популярности': 'popular', 'По рейтингу': 'rate', 'По возрастанию цены': 'priceup',
                  'По убыванию цены': 'pricedown', 'По новинкам': 'newly', 'Сначала выгодные': 'benefit'}

    LOCATOR_FILTER_BUTTON = (By.CSS_SELECTOR, 'button.dropdown-filter__btn.dropdown-filter__btn--sorter')
    LOCATOR_CATALOG_BUTTON = (By.CSS_SELECTOR, 'button.nav-element__burger')
    LOCATOR_FILTER_OPTIONS = (By.XPATH,
                              "/html/body/div[1]/main/div[2]/div/div[2]/div/div[4]/div/div/div/div/div[1]/div[2]/div/div/ul/li")

    def apply_sort_rules(self):
        sort_rules = self.element_is_visible(self.LOCATOR_FILTER_BUTTON)
        sort_rules.click()

        list_elements = self.elements_are_visible(self.LOCATOR_FILTER_OPTIONS)
        list_elements.pop(0)
        random_element = random.choice(list_elements)
        random_keyword = random_element.text
        random_element.click()
        return self.SORT_RULES[random_keyword]
