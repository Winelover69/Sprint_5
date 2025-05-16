from selenium.webdriver.common.by import By

class LoginPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@name='name']")  # Поле ввода "Имя" по атрибуту name
    EMAIL_INPUT = (By.XPATH, "//input[@type='email']")  # Поле ввода "Email" по атрибуту type
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")  # Поле ввода "Пароль" по атрибуту type
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться" по тексту
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти" по тексту
    INCORRECT_PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # Сообщение об ошибке по тексту