from locators.register_page_locators import RegisterPageLocators
from utils.helpers import generate_unique_email, generate_password

class TestRegistration:
    def test_successful_registration(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/register")
        unique_email = generate_unique_email()
        password = generate_password()

        browser.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Test User")
        browser.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(unique_email)
        browser.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_incorrect_password_error(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/register")
        browser.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Test User")
        browser.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_unique_email())
        browser.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys("123")
        browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        assert browser.find_element(*RegisterPageLocators.INCORRECT_PASSWORD_ERROR).is_displayed()