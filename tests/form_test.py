import time
from pages.main_page import MainPage


class TestFormPage:
    def test_form(self, driver):
        main_page = MainPage(driver, "https://www.wildberries.ru/")
        main_page.open()

        main_page.open_sport_category()
        time.sleep(5)
