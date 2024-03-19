import time
import random
from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TablePage(BasePage):
    # Locators
    SORT_RULES = {'По популярности': 'popular', 'По рейтингу': 'rate', 'По возрастанию цены': 'priceup',
                  'По убыванию цены': 'pricedown', 'По новинкам': 'newly', 'Сначала выгодные': 'benefit'}
    CATEGORIES = {
        'Ножка для стола': '8226',
        'Стол обеденный': '7648',
        'Стол-книжка': '7650',
        'Стол-трансформер': '7649',
        'Столешница для стола': '8234'
    }

    LOCATOR_SORT_RULES_BUTTON = (By.CSS_SELECTOR, 'button.dropdown-filter__btn.dropdown-filter__btn--sorter')
    LOCATOR_CATALOG_BUTTON = (By.CSS_SELECTOR, 'button.nav-element__burger')
    LOCATOR_SORT_RULES_OPTIONS = (
        By.XPATH, "/html/body/div[1]/main/div[2]/div/div[2]/div/div[4]/div/div/div/div/div[1]/div[2]/div/div/ul/li")
    LOCATOR_CATEGORY_BUTTON = (
        By.XPATH, "/html/body/div[1]/main/div[2]/div/div[2]/div/div[4]/div/div/div/div/div[1]/div[3]/button")
    LOCATOR_CATEGORY_LIST = (
        By.XPATH, "/html/body/div[1]/main/div[2]/div/div[2]/div/div[4]/div/div/div/div/div[1]/div[3]/div/div[1]/ul/li")

    def apply_sort_rules(self):
        sort_rules = self.element_is_visible(self.LOCATOR_SORT_RULES_BUTTON)
        sort_rules.click()

        list_elements = self.elements_are_visible(self.LOCATOR_SORT_RULES_OPTIONS)
        list_elements.pop(0)
        random_element = random.choice(list_elements)
        random_keyword = random_element.text
        random_element.click()
        return self.SORT_RULES[random_keyword]

    def choose_category(self):
        category_button = self.element_is_visible(self.LOCATOR_CATEGORY_BUTTON)
        category_button.click()
        categories_list = self.elements_are_visible(self.LOCATOR_CATEGORY_LIST)
        random_element = random.choice(categories_list)
        random_keyword = random_element.text.split('\u2002')[0]
        random_element.click()
        return self.CATEGORIES[random_keyword]
