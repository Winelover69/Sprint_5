from locators.main_page_locators import MainPageLocators
from locators.constructor_page_locators import ConstructorPageLocators

class TestConstructor:
    def setup_method(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        assert browser.find_element(*ConstructorPageLocators.CONSTRUCTOR_HEADER).is_displayed()
        self.browser = browser

    def test_go_to_buns_section(self): # Проверка перехода к разделу «Булки»
        self.browser.find_element(*MainPageLocators.BUNS_TAB).click()
        assert self.browser.find_element(*ConstructorPageLocators.BUNS_SECTION).is_displayed()
        assert self.browser.find_element(*ConstructorPageLocators.BUNS_TAB_ACTIVE).is_displayed()

    def test_go_to_sauces_section(self): # Проверка перехода к разделу «Соусы»
        self.browser.find_element(*MainPageLocators.SAUCES_TAB).click()
        assert self.browser.find_element(*ConstructorPageLocators.SAUCES_SECTION).is_displayed()
        assert self.browser.find_element(*ConstructorPageLocators.SAUCES_TAB_ACTIVE).is_displayed()

    def test_go_to_fillings_section(self): # Проверка перехода к разделу «Начинки»
        self.browser.find_element(*MainPageLocators.FILLINGS_TAB).click()
        assert self.browser.find_element(*ConstructorPageLocators.FILLINGS_SECTION).is_displayed()
        assert self.browser.find_element(*ConstructorPageLocators.FILLINGS_TAB_ACTIVE).is_displayed()
