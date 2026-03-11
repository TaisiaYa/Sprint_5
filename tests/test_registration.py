from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generator import (
    generate_unique_email,
    generate_valid_password,
    generate_invalid_password,
    generate_invalid_email,
    generate_email_without_domain
)
from locators import *
from constants import BASE_URL, DEFAULT_TIMEOUT, USER_TEST_NAME


def test_successful_registration(browser):
    # Генерируем данные
    email = generate_unique_email()
    password = generate_valid_password()
    name = USER_TEST_NAME
    
    # Переходим на страницу регистрации
    browser.get(BASE_URL)
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)
    ).click()
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_REGISTER_LINK)
    ).click()
    
    # Регистрируем пользователя
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(REG_NAME_INPUT)
    ).send_keys(name)
    browser.find_element(*REG_EMAIL_INPUT).send_keys(email)
    browser.find_element(*REG_PASSWORD_INPUT).send_keys(password)
    browser.find_element(*REG_REGISTER_BUTTON).click()
    
    # Проверяем успешную регистрацию (редирект на страницу входа)
    login_header = WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(LOGIN_HEADER)
    )
    assert login_header.is_displayed(), "Регистрация не выполнена, заголовок 'Вход' не найден"


def test_registration_invalid_password(browser):
    # Генерируем данные с невалидным паролем
    email = generate_unique_email()
    password = generate_invalid_password()  # пароль меньше 6 символов
    name = USER_TEST_NAME
    
    # Переходим на страницу регистрации
    browser.get(BASE_URL)
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)
    ).click()
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_REGISTER_LINK)
    ).click()
    
    # Пытаемся зарегистрироваться с коротким паролем
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(REG_NAME_INPUT)
    ).send_keys(name)
    browser.find_element(*REG_EMAIL_INPUT).send_keys(email)
    browser.find_element(*REG_PASSWORD_INPUT).send_keys(password)
    browser.find_element(*REG_REGISTER_BUTTON).click()
    
    # Проверяем появление ошибки
    password_error = WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(REG_PASSWORD_ERROR)
    )
    assert password_error.is_displayed(), "Ошибка о некорректном пароле не отображается"
