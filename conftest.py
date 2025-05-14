from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from locators.register_page_locators import RegisterPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from utils.helpers import generate_unique_email, generate_password

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or firefox")

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")
    yield driver
    driver.quit()

@pytest.fixture
def registered_user(browser):
    browser.get("https://stellarburgers.nomoreparties.site/register")
    unique_email = generate_unique_email()
    password = generate_password()
    browser.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Test User")
    browser.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(unique_email)
    browser.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"
    return {"email": unique_email, "password": password}

@pytest.fixture
def logged_in_user(browser, registered_user):
    browser.get("https://stellarburgers.nomoreparties.site/login")
    browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
    browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
    browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    assert browser.current_url == "https://stellarburgers.nomoreparties.site/"
    assert browser.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).is_displayed()
    yield browser
    driver.quit()