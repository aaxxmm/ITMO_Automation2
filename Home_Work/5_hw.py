from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def check_elements():
    # Настройка WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Запуск браузера в фоновом режиме
    service = Service(path_to_chromedriver=r"C:\Program Files\сhromedriver\chromedriver.exe")  # Укажите путь к вашему chromedriver

    # Запуск браузера
    browser = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Переход на страницу
        browser.get("https://www.saucedemo.com/")

        # Поиск элементов
        username_field = browser.find_element(By.ID, "user-name")
        password_field = browser.find_element(By.ID, "password")
        submit_button = browser.find_element(By.ID, "login-button")

        # Проверка наличия элементов
        if username_field and password_field and submit_button:
            print("Элементы найдены")
        else:
            print("Элементы не найдены")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        # Закрытие браузера
        browser.quit()


# Вызов функции
check_elements()