import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--user_language', action='store', default=None,
                     help="Введите язык для браузера")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="браузер только хром, других вариантов нет")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("user_language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("имя браузера может быть только хром, других вариантов нет")

    yield browser
    print("\nquit browser..")
    browser.quit()
