import pytest
from Selenium.base.selenium_driver import Driver


@pytest.fixture(scope="class")
def one_time_setup(request, browser):
    print("Running one time setup")
    obj = Driver(browser)
    driver = obj.start_driver()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time teardown")


@pytest.fixture(scope="session")
def pytest_addoption(parser):
    parser.addoption("--browser", help="firefox/chrome")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")





