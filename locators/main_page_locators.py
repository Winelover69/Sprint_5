from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной странице
    PERSONAL_CABINET_LINK = (By.XPATH, "//a[contains(@href, '/profile')]")  # Ссылка "Личный кабинет"
    CONSTRUCTOR_LINK = (By.XPATH, "//span[text()='Конструктор']")  # Ссылка "Конструктор"
    STELLAR_BURGERS_LOGO = (By.XPATH, "//a[@href='/']")  # Логотип Stellar Burgers
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")  # Таб "Булки" в конструкторе
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")  # Таб "Соусы" в конструкторе
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")  # Таб "Начинки" в конструкторе