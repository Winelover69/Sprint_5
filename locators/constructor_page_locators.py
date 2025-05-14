from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок "Соберите бургер"
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")  # Заголовок секции "Булки"
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")  # Заголовок секции "Соусы"
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")  # Заголовок секции "Начинки"
    BUNS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_main') and contains(@class, 'tab_active')]//span[text()='Булки']")  # Активный таб "Булки"
    SAUCES_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_main') and contains(@class, 'tab_active')]//span[text()='Соусы']")  # Активный таб "Соусы"
    FILLINGS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_main') and contains(@class, 'tab_active')]//span[text()='Начинки']")  # Активный таб "Начинки"