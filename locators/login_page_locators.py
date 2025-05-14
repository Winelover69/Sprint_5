from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//fieldset[1]/div/div/input")  # Поле ввода "Email" на странице входа
    PASSWORD_INPUT = (By.XPATH, "//fieldset[2]/div/div/input")  # Поле ввода "Пароль" на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти" на странице входа
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка "Зарегистрироваться" на странице входа
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка "Восстановить пароль" на странице входа