import time
from pages.tables_page import TablePage
import pytest


class TestMainPage:
    def test_set_sort_rule(self, driver):
        table_page = TablePage(driver, "https://www.wildberries.ru/catalog/mebel/mebel-dlya-kuhni/stoly")
        table_page.open()
        selected_rule = table_page.apply_sort_rules()
        current_url = driver.current_url
        assert f"sort={selected_rule}" in current_url

    def test_set_category(self, driver):
        table_page = TablePage(driver, "https://www.wildberries.ru/catalog/mebel/mebel-dlya-kuhni/stoly")
        table_page.open()
        selected_category = table_page.choose_category()
        current_url = driver.current_url
        assert f"xsubject={selected_category}" in current_url
