from selenium.webdriver.common.by import By

class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//fieldset[1]/div/div/input")  # Поле ввода "Имя"
    EMAIL_INPUT = (By.XPATH, "//fieldset[2]/div/div/input")  # Поле ввода "Email"
    PASSWORD_INPUT = (By.XPATH, "//fieldset[3]/div/div/input")  # Поле ввода "Пароль"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти" на странице регистрации
    INCORRECT_PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # Сообщение об ошибке некорректного пароля