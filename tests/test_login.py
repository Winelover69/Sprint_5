from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators

class TestLogin:
    def test_login_from_main_page(self, browser, registered_user): # Проверка входа по кнопке «Войти в аккаунт» на главной
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"
        assert browser.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).is_displayed()

    def test_login_from_personal_cabinet(self, browser, registered_user): # Проверка входа через кнопку «Личный кабинет»
        browser.get("https://stellarburgers.nomoreparties.site/profile")
        browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"
        assert browser.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).is_displayed()

    def test_login_from_register_form(self, browser, registered_user): # Проверка входа через кнопку в форме регистрации
        browser.get("https://stellarburgers.nomoreparties.site/register")
        browser.find_element(*LoginPageLocators.REGISTER_LINK).click()
        browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"
        assert browser.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).is_displayed()

    def test_login_from_forgot_password_form(self, browser, registered_user): # Проверка входа через кнопку в форме восстановления пароля
        browser.get("https://stellarburgers.nomoreparties.site/forgot-password")
        browser.find_element(*LoginPageLocators.REGISTER_LINK).click()
        browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"
        assert browser.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).is_displayed()