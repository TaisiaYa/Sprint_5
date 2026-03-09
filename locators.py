from selenium.webdriver.common.by import By

# Локаторы главной страницы
# Кнопка «Войти в аккаунт» на главной странице
MAIN_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")

# Кнопка «Личный кабинет» в шапке сайта
MAIN_PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")

# Кнопка «Конструктор» в шапке сайта
MAIN_CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")

# Логотип Stellar Burgers
MAIN_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

# Кнопка «Оформить заказ»
MAIN_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

# Разделы конструктора
MAIN_BUNS_SECTION = (By.XPATH, ".//span[text()='Булки']/parent::div")
MAIN_SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']/parent::div")
MAIN_FILLINGS_SECTION = (By.XPATH, ".//span[text()='Начинки']/parent::div")

# Активный раздел (проверка переключения)
MAIN_ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc')]")


# Локаторы страницы входа
# Заголовок «Вход»
LOGIN_HEADER = (By.XPATH, ".//h2[text()='Вход']")

# Поле Email
LOGIN_EMAIL_INPUT = (By.NAME, "name")

# Поле Пароль
LOGIN_PASSWORD_INPUT = (By.NAME, "Пароль")

# Кнопка «Войти»
LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

# Ссылка «Зарегистрироваться»
LOGIN_REGISTER_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")

# Ссылка «Восстановить пароль»
LOGIN_FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")


# Локаторы страницы регистрации
# Поле Имя
REG_NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")

# Поле Email
REG_EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")

# Поле Пароль
REG_PASSWORD_INPUT = (By.NAME, "Пароль")

# Кнопка «Зарегистрироваться»
REG_REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")

# Ссылка «Войти» (для перехода на страницу входа)
REG_LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")

# Ошибка для некорректного пароля
REG_PASSWORD_ERROR = (By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]")

# Ошибка для обязательного поля (имя, email)
REG_FIELD_ERROR = (By.XPATH, ".//p[contains(@class, 'input__error')]")

# Локаторы страницы профиля (личный кабинет)
# Кнопка «Выход»
PROFILE_LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

# Заголовок «Профиль» (для проверки, что мы в ЛК)
PROFILE_HEADER = (By.XPATH, ".//a[text()='Профиль']")


# Локаторы страницы восстановления пароля
# Кнопка «Войти» (ссылка для перехода на логин)
FORGOT_LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")

