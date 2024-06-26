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

    LOCATOR_ADD_TO_BASKET_BUTTONS = (By.CLASS_NAME, "product-card__add-basket")
    LOCATOR_BASKET_BUTTON = (By.CSS_SELECTOR, 'a.navbar-pc__link[data-wba-header-name="Cart"]')

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

    def choose_multiply_categories(self):
        category_button = self.element_is_visible(self.LOCATOR_CATEGORY_BUTTON)
        category_button.click()
        categories_list = self.elements_are_visible(self.LOCATOR_CATEGORY_LIST)

        selected_categories = []
        random_numbers_of_categories = random.randint(2, len(self.CATEGORIES))
        for _ in range(random_numbers_of_categories):
            random_element = random.choice(categories_list)
            random_keyword = random_element.text.split('\u2002')[0]
            random_element.click()
            selected_categories.append(self.CATEGORIES[random_keyword])
            categories_list = [element for element in categories_list if element != random_element]
        return selected_categories

    def add_item_to_basket(self, count=1):
        buy_buttons = self.elements_are_visible(self.LOCATOR_ADD_TO_BASKET_BUTTONS)
        for _ in range(count):
            random_buy_button = random.choice(buy_buttons)
            buy_buttons.remove(random_buy_button)
            random_buy_button.click()

    def open_basket(self):
        basket_button = self.element_is_visible(self.LOCATOR_BASKET_BUTTON)
        basket_button.click()
