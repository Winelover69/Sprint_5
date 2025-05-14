from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators

class TestProfile:
    def test_go_to_personal_cabinet(self, browser): # Проверка перехода по клику на «Личный кабинет»
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()
        assert browser.find_element(*ProfilePageLocators.PROFILE_HEADER).is_displayed()

    def test_go_to_constructor_from_profile_link(self, logged_in_user): # Проверка перехода по клику на «Конструктор» из личного кабинета
        logged_in_user.find_element(*ProfilePageLocators.CONSTRUCTOR_LINK).click()
        assert logged_in_user.find_element(*MainPageLocators.CONSTRUCTOR_LINK).is_displayed()
        assert logged_in_user.find_element(*MainPageLocators.STELLAR_BURGERS_LOGO).is_displayed()

    def test_go_to_constructor_from_profile_logo(self, logged_in_user): # Проверка перехода по клику на логотип Stellar Burgers из личного кабинета
        logged_in_user.find_element(*ProfilePageLocators.STELLAR_BURGERS_LOGO).click()
        assert logged_in_user.find_element(*MainPageLocators.CONSTRUCTOR_LINK).is_displayed()
        assert logged_in_user.find_element(*MainPageLocators.STELLAR_BURGERS_LOGO).is_displayed()

    def test_logout(self, logged_in_user): # Проверка выхода по кнопке «Выйти» в личном кабинете
        logged_in_user.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()
        logged_in_user.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
        assert logged_in_user.current_url == "https://stellarburgers.nomoreparties.site/login"