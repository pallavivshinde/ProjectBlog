import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        print("\nRUNNING TESTCASE IN CHROME BROWSER")
        driver=webdriver.Chrome()

    elif browser=='edge':
        print("\nRUNNINNG TESTCASE IN EDGE BROWSER")
        driver=webdriver.Edge()

    else:
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver=webdriver.Chrome(options=chrome_options)
        print("\n RUNNING IN HEADLESS MODE")

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
