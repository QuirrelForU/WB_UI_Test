import time
from pages.main_page import MainPage
import pytest


class TestMainPage:
    def test_open_sport_category(self, driver):
        main_page = MainPage(driver, "https://www.wildberries.ru/")
        main_page.open()
        main_page.open_sport_category()
        current_url = driver.current_url
        assert "/catalog/sport" in current_url

    def test_open_shoes_category(self, driver):
        main_page = MainPage(driver, "https://www.wildberries.ru/")
        main_page.open()
        main_page.open_shoes_category()
        current_url = driver.current_url
        assert "/catalog/obuv" in current_url

    def test_open_house_category(self, driver):
        main_page = MainPage(driver, "https://www.wildberries.ru/")
        main_page.open()
        main_page.open_house_category()
        current_url = driver.current_url
        assert "/catalog/dom-i-dacha" in current_url

    def test_open_furniture_category(self, driver):
        main_page = MainPage(driver, "https://www.wildberries.ru/")
        main_page.open()
        main_page.open_furniture_category()
        current_url = driver.current_url
        assert "/catalog/dom/mebel" in current_url

    def test_open_books_category(self, driver):
        main_page = MainPage(driver, "https://www.wildberries.ru/")
        main_page.open()
        main_page.open_books_category()
        current_url = driver.current_url
        assert "/catalog/knigi" in current_url

    def test_search_item_enter(self,driver):
        main_page = MainPage(driver, "https://www.wildberries.ru/")
        main_page.open()
        main_page.search_item_enter("Чай")
        time.sleep(5)