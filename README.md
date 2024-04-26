# Автоматизированное тестирование UI с использованием Selenium

Практическая работа №3 в ходе прохождения курса "Тестирование программного обеспечения".

Этот проект содержит комплект автоматизированных тестов для тестирования [Wildberries](https://www.wildberries.ru/) с использованием Selenium.

## Использование Page Object Model (POM) для тестирования

Page Object Model  — это шаблон проектирования, который облегчает создание и поддержку автоматизированных тестов с помощью Selenium.

В данной работе:
- Есть базовый класс `BasePage`, который содержит общие методы, такие как открытие страницы и ожидание видимости элементов
- Классы страниц (`BasketPage`, `MainPage`, `TablePage`) наследуются от `BasePage` и содержат методы для взаимодействия со своими страницами
- Селекторы элементов вынесены в константы внутри классов для удобства управления и изменения

Использование POM позволяет создавать структурированный и модульный код для автоматизированных тестов, делая его более читаемым и поддерживаемым.


## Pytest и WebDriver
Для выполнения автоматизированных тестов используется  Pytest и Selenium WebDriver для взаимодействия с браузером.

С помощью Pytest Fixture обеспечивается инициализация и подготовка WebDriver перед выполнением тестов.
```python
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    # Указываем путь к исполняемому файлу драйвера Chrome
    driver_service = Service("chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver_service.start()

    # Инициализируем экземпляр WebDriver с указанием сервиса
    driver = webdriver.Chrome(service=driver_service)

    # Максимизируем окно браузера при запуске теста
    driver.maximize_window()

    # Передаем экземпляр WebDriver в тестовую функцию
    yield driver

    # Закрываем браузер после завершения теста
    driver.quit()
```

## Тесты
Ниже приведены примеры некоторых тестов реализованных в данной работе.
### Позитивные

1. **Открытие страницы каталога спорт товаров**

    Проверка успешного открытия страницы каталога спорт товаров
```python
    def test_open_sport_category(self, driver):
        main_page = MainPage(driver, "https://www.wildberries.ru/")
        main_page.open()
        main_page.open_sport_category()
        current_url = driver.current_url
        assert "/catalog/sport" in current_url
```
2. **Открытие корзины**

    Проверка успешного открытия страницы корзины
```python
    def test_open_basket(self, driver):
        table_page = TablePage(driver, "https://www.wildberries.ru/catalog/mebel/mebel-dlya-kuhni/stoly")
        table_page.open()
        table_page.open_basket()
        current_url = driver.current_url
        assert current_url == "https://www.wildberries.ru/lk/basket"
```
3. **Добавление товара в корзину**

    Проверка успешного добавления товара в корзину
```python
    def test_add_to_basket(self, driver):
        table_page = TablePage(driver, "https://www.wildberries.ru/catalog/mebel/mebel-dlya-kuhni/stoly")
        table_page.open()
        table_page.add_item_to_basket(count := random.randint(1, 5))
        time.sleep(1)
        basket_page = BasketPage(driver, "https://www.wildberries.ru/lk/basket")
        basket_page.open()
        assert int(basket_page.get_items_count()) == count
```

### Негативные

1. **Поиск пустого товара**

    Проверка поиска с пустым запросом
```python
    def test_search_item_enter_empty(self, driver):
        default_url = "https://www.wildberries.ru/"
        main_page = MainPage(driver, default_url)
        main_page.open()
        main_page.search_item_enter("")
        current_url = driver.current_url
        assert default_url == current_url
```
