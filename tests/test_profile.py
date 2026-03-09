from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

# Константы
BASE_URL = "https://stellarburgers.education-services.ru/"
DEFAULT_TIMEOUT = 10


def test_go_to_personal_account(browser, logged_in_user):
    # Переходим на главную и кликаем "Личный кабинет"
    browser.get(BASE_URL)
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(MAIN_PERSONAL_ACCOUNT_BUTTON)
    ).click()
    
    # Проверяем, что открылась страница профиля
    profile_header = WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(PROFILE_HEADER)
    )
    assert profile_header.is_displayed(), "Страница профиля не открылась"


def test_go_to_constructor_from_profile(browser, logged_in_user):
    # Переходим в личный кабинет
    browser.get(BASE_URL)
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(MAIN_PERSONAL_ACCOUNT_BUTTON)
    ).click()
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(PROFILE_HEADER)
    )
    
    # Кликаем "Конструктор"
    browser.find_element(*MAIN_CONSTRUCTOR_BUTTON).click()
    
    # Проверяем, что вернулись на главную
    order_button = WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(MAIN_ORDER_BUTTON)
    )
    assert order_button.is_displayed(), "Переход в конструктор не выполнен"


def test_go_to_main_via_logo_from_profile(browser, logged_in_user):
    # Переходим в личный кабинет
    browser.get(BASE_URL)
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(MAIN_PERSONAL_ACCOUNT_BUTTON)
    ).click()
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(PROFILE_HEADER)
    )
    
    # Кликаем на логотип
    browser.find_element(*MAIN_LOGO).click()
    
    # Проверяем, что вернулись на главную
    order_button = WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(MAIN_ORDER_BUTTON)
    )
    assert order_button.is_displayed(), "Переход на главную не выполнен"


def test_logout_from_profile(browser, logged_in_user):
    # Переходим в личный кабинет
    browser.get(BASE_URL)
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(MAIN_PERSONAL_ACCOUNT_BUTTON)
    ).click()
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(PROFILE_HEADER)
    )
    
    # Выходим из аккаунта
    browser.find_element(*PROFILE_LOGOUT_BUTTON).click()
    
    # Проверяем, что оказались на странице входа
    login_header = WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(LOGIN_HEADER)
    )
    assert login_header.is_displayed(), "Выход из аккаунта не выполнен"
