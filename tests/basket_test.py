import random
import time
from pages.tables_page import TablePage
from pages.basket_page import BasketPage
import pytest


class TestBasketPage:

    def test_open_basket(self, driver):
        table_page = TablePage(driver, "https://www.wildberries.ru/catalog/mebel/mebel-dlya-kuhni/stoly")
        table_page.open()
        table_page.open_basket()
        current_url = driver.current_url
        assert current_url == "https://www.wildberries.ru/lk/basket"

    def test_add_to_basket(self, driver):
        table_page = TablePage(driver, "https://www.wildberries.ru/catalog/mebel/mebel-dlya-kuhni/stoly")
        table_page.open()
        table_page.add_item_to_basket(count := random.randint(1, 5))
        time.sleep(1)
        basket_page = BasketPage(driver, "https://www.wildberries.ru/lk/basket")
        basket_page.open()
        assert int(basket_page.get_items_count()) == count

    def test_item_plus_minus_in_basket(self, driver):
        table_page = TablePage(driver, "https://www.wildberries.ru/catalog/mebel/mebel-dlya-kuhni/stoly")
        table_page.open()
        table_page.add_item_to_basket()
        time.sleep(1)
        basket_page = BasketPage(driver, "https://www.wildberries.ru/lk/basket")
        basket_page.open()
        basket_page.item_plus(count := 3)
        basket_page.item_minus()
        assert int(basket_page.get_items_count()) == count
