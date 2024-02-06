import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def chrome_browser(user_language):
    """
    Запустить драйвер Chrome, но перед этим добавить в его конструктор опцию – язык интерфейса.

    :param user_language: язык интерфейса
    :return: драйвер Chrome
    """
    options = ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    return webdriver.Chrome(options=options)


def firefox_browser(user_language):
    """
    Запустить драйвер Firefox, но перед этим добавить в его конструктор опцию – язык интерфейса.

    :param user_language: язык интерфейса
    :return: драйвер Firefox
    """
    options = FirefoxOptions()
    options.set_preference('intl.accept_languages', user_language)

    return webdriver.Firefox(options=options)


def pytest_addoption(parser):
    """
    Считать и обработать параметры командной строки (имя браузера и язык интерфейса)
    с помощью встроенной функции pytest_addoption:
    https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption.

    :param parser: атрибут объекта request
    """
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser')
    parser.addoption('--language', action='store', default='ru', help='Choose browser language')


@pytest.fixture(scope='function')
def browser(request):
    """
    Запустить браузер.

    :param request: встроенная фикстура pytest
    :return: драйвер браузера
    """
    # Запросить параметры browser_name и language
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')

    if browser_name == 'chrome':
        browser = chrome_browser(language)
    elif browser_name == 'firefox':
        browser = firefox_browser(language)
    else:
        print(f'Browser {browser_name} is not implemented')
        raise pytest.UsageError('Check --browser_name or/and --language')
    yield browser
    browser.quit()
