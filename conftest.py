import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from generator import generate_unique_email, generate_valid_password
from locators import *
from constants import BASE_URL, DEFAULT_TIMEOUT, DEFAULT_TEST_NAME

@pytest.fixture
def browser():

    # Настройка Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    # Возвращаем драйвер в тест
    yield driver
    
    # Закрываем браузер после теста
    driver.quit()


@pytest.fixture
def registered_user(browser):
  
    # Генерируем уникальные данные
    email = generate_unique_email()
    password = generate_valid_password()
    name = DEFAULT_TEST_NAME
    
    # Регистрируем пользователя
    browser.get(BASE_URL)
    
    # Клик "Войти в аккаунт"
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)
    ).click()
    
    # Клик "Зарегистрироваться"
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_REGISTER_LINK)
    ).click()
    
    # Заполняем форму регистрации
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(REG_NAME_INPUT)
    ).send_keys(name)
    
    browser.find_element(*REG_EMAIL_INPUT).send_keys(email)
    browser.find_element(*REG_PASSWORD_INPUT).send_keys(password)
    browser.find_element(*REG_REGISTER_BUTTON).click()
    
    # Ждем редиректа на страницу входа
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(LOGIN_HEADER)
    )
    
    # Возвращаем данные пользователя
    return {"email": email, "password": password, "name": name}


@pytest.fixture
def logged_in_user(browser, registered_user):
    
    # Логинимся
    browser.find_element(*LOGIN_EMAIL_INPUT).send_keys(registered_user["email"])
    browser.find_element(*LOGIN_PASSWORD_INPUT).send_keys(registered_user["password"])
    browser.find_element(*LOGIN_BUTTON).click()
    
    # Ждем входа (проверяем наличие кнопки заказа)
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(MAIN_ORDER_BUTTON)
    )

    # Возвращаем данные пользователя
    return registered_user