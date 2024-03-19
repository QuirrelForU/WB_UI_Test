import random
import time
from pages.tables_page import TablePage
from pages.basket_page import BasketPage
import pytest


class TestBasketPage:
    def test_add_to_basket(self, driver):
        table_page = TablePage(driver, "https://www.wildberries.ru/catalog/mebel/mebel-dlya-kuhni/stoly")
        table_page.open()
        table_page.add_item_to_basket(count := random.randint(1, 5))
        time.sleep(1)
        basket_page = BasketPage(driver, "https://www.wildberries.ru/lk/basket")
        basket_page.open()
        assert int(basket_page.get_items_count()) == count
