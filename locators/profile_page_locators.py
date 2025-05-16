from selenium.webdriver.common.by import By

class ProfilePageLocators:
    PROFILE_HEADER = (By.XPATH, "//h2[text()='Профиль']")  # Заголовок "Профиль" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")  # Кнопка "Выйти" в личном кабинете
    CONSTRUCTOR_LINK = (By.XPATH, "//a[text()='Конструктор']")  # Ссылка "Конструктор" в личном кабинете
    STELLAR_BURGERS_LOGO = (By.XPATH, "//a[@href='/']")  # Логотип Stellar Burgers в личном кабинете