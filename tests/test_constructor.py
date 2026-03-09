from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

# Константы
BASE_URL = "https://stellarburgers.education-services.ru/"
DEFAULT_TIMEOUT = 10


def test_switch_to_buns(browser):
    # Открываем главную страницу
    browser.get(BASE_URL)
    
    # Переключаемся на раздел "Соусы", чтобы потом вернуться к "Булкам"
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(MAIN_SAUCES_SECTION)
    ).click()
    
    # Переключаемся на раздел "Булки"
    browser.find_element(*MAIN_BUNS_SECTION).click()
    
    # Проверяем, что раздел "Булки" стал активным
    active_section = WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(MAIN_ACTIVE_SECTION)
    )
    active_section_text = active_section.text
    assert "Булки" in active_section_text, f"Раздел 'Булки' не активен, текущий: {active_section_text}"


def test_switch_to_sauces(browser):
    # Открываем главную страницу
    browser.get(BASE_URL)
    
    # Переключаемся на раздел "Соусы"
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(MAIN_SAUCES_SECTION)
    ).click()
    
    # Проверяем, что раздел "Соусы" стал активным
    active_section = WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(MAIN_ACTIVE_SECTION)
    )
    active_section_text = active_section.text
    assert "Соусы" in active_section_text, f"Раздел 'Соусы' не активен, текущий: {active_section_text}"


def test_switch_to_fillings(browser):
    # Открываем главную страницу
    browser.get(BASE_URL)
    
    # Переключаемся на раздел "Начинки"
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(MAIN_FILLINGS_SECTION)
    ).click()
    
    # Проверяем, что раздел "Начинки" стал активным
    active_section = WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(MAIN_ACTIVE_SECTION)
    )
    active_section_text = active_section.text
    assert "Начинки" in active_section_text, f"Раздел 'Начинки' не активен, текущий: {active_section_text}"