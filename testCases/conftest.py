from datetime import datetime
import os.path

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver


@pytest.fixture()
def setUp(browser):
    if browser == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())  ### DEFAULT BROWSER
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


#### PYTEST HTML REPORT ####

def pytest_configure(config):
    config._metadata['Project Name'] = 'TEST WEBSITE'


# It is a hook for Delete/Modify environment info in the HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


# Specifying Report folder location and save report with timestamp

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + '/reports/' + datetime.now().strftime(
        "%d-%m-%Y %H-%M-%S") + ".html"
