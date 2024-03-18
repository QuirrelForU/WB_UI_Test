import time
from pages.main_page import MainPage
import pytest


class TestMainPage:
    def test_sport_nav(self, driver):
        main_page = MainPage(driver, "https://www.wildberries.ru/")
        main_page.open()
        main_page.open_sport_category()
        current_url = driver.current_url
        assert "/catalog/sport" in current_url
