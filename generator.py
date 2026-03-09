import random


#Генерируем уникальный email для регистрации
#Формат: имя_фамилия_номер_когорты_3цифры@yandex.ru
#Номер когорты: 41

def generate_unique_email():
    
    COHORT_NUMBER = "41"
    first_name = "taya"
    last_name = "yakubovich"
    random_digits = random.randint(100, 999)
    
    return f"{first_name}_{last_name}_{COHORT_NUMBER}_{random_digits}@yandex.ru"

# Генерируем валидный пароль (6+ символов)
def generate_valid_password():
    return "Valid123"

#Генерируем невалидный пароль (менее 6 символов)
def generate_invalid_password():
    return "123"

#Генерируем невалидный email без @
def generate_invalid_email():
    return "invalid_email_without_at"

#Генерируем email без домена
def generate_email_without_domain():
    return "user@"
