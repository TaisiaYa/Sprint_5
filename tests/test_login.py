import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from constants import BASE_URL, DEFAULT_TIMEOUT


def test_login_main_button(browser, registered_user):
    # Переходим на главную и кликаем "Войти в аккаунт"
    browser.get(BASE_URL)
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)
    ).click()
    # Выполняем вход
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(LOGIN_EMAIL_INPUT)
    ).send_keys(registered_user["email"])
    browser.find_element(*LOGIN_PASSWORD_INPUT).send_keys(registered_user["password"])
    browser.find_element(*LOGIN_BUTTON).click()

    # Проверяем успешный вход
    time.sleep(1)
    button = browser.find_element(*MAIN_ORDER_BUTTON)
    assert button.is_displayed(), "Вход не выполнен, кнопка 'Оформить заказ' не найдена"

def test_login_personal_account_button(browser, registered_user):
    # Переходим на главную и кликаем "Личный кабинет"
    browser.get(BASE_URL)
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(MAIN_PERSONAL_ACCOUNT_BUTTON)
    ).click()
    
    # Выполняем вход
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(LOGIN_EMAIL_INPUT)
    ).send_keys(registered_user["email"])
    browser.find_element(*LOGIN_PASSWORD_INPUT).send_keys(registered_user["password"])
    browser.find_element(*LOGIN_BUTTON).click()
    
    # Проверяем успешный вход
    time.sleep(1)
    button = browser.find_element(*MAIN_ORDER_BUTTON)
    assert button.is_displayed(), "Вход не выполнен, кнопка 'Оформить заказ' не найдена"

def test_login_from_registration_form(browser, registered_user):
    # Идем на страницу регистрации
    browser.get(BASE_URL)
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)
    ).click()
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_REGISTER_LINK)
    ).click()
    
    # Переходим на страницу входа через ссылку
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(REG_LOGIN_LINK)
    ).click()
    
    # Выполняем вход
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(LOGIN_EMAIL_INPUT)
    ).send_keys(registered_user["email"])
    browser.find_element(*LOGIN_PASSWORD_INPUT).send_keys(registered_user["password"])
    browser.find_element(*LOGIN_BUTTON).click()
    
    # Проверяем успешный вход
    time.sleep(1)
    button = browser.find_element(*MAIN_ORDER_BUTTON)
    assert button.is_displayed(), "Вход не выполнен, кнопка 'Оформить заказ' не найдена"


def test_login_from_forgot_password_form(browser, registered_user):
    # Идем на страницу восстановления пароля
    browser.get(BASE_URL)
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)
    ).click()
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_FORGOT_PASSWORD_LINK)
    ).click()
    
    # Переходим на страницу входа через ссылку
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(FORGOT_LOGIN_LINK)
    ).click()
    
    # Выполняем вход
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(LOGIN_EMAIL_INPUT)
    ).send_keys(registered_user["email"])
    browser.find_element(*LOGIN_PASSWORD_INPUT).send_keys(registered_user["password"])
    browser.find_element(*LOGIN_BUTTON).click()
    
    # Проверяем успешный вход
    time.sleep(1)
    button = browser.find_element(*MAIN_ORDER_BUTTON)
    assert button.is_displayed(), "Вход не выполнен, кнопка 'Оформить заказ' не найдена"