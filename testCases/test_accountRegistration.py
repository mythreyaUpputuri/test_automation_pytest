import random
import names  # added it for fun
import time

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.RegistrationPage import RegistrationPage
from pageObjects.MyAccount import MyAccount
from utilities.randomName import user_generator
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen


class TestAccountRegistration:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # for Logging

    @pytest.mark.sanity
    def test_account_registration(self, setUp):
        self.logger.info("**** Test Account Registration started ****")
        self.driver = setUp
        self.driver.set_window_position(+1000, 0)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        time.sleep(5)
        self.hp = HomePage(self.driver)
        self.hp.clickCreateAccount()

        self.regPage = RegistrationPage(self.driver)

        firstName, lastName, email = user_generator()

        self.regPage.enterFirstName(firstName)
        self.regPage.enterLastName(lastName)
        self.regPage.enterEmail(email)
        passwd = ReadConfig.getPassword()
        self.regPage.enterPassword(passwd)
        self.regPage.confirmPassword(passwd)

        self.regPage.clickCreateAccount()
        time.sleep(10)

        self.ma = MyAccount(self.driver)
        self.ma.validateRegistrationBanner()
        self.driver.quit()

        self.logger.info("End of test - Test Account Registration")