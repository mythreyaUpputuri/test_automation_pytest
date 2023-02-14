# from selenium.webdriver.common.by import By
from utilities.handleElements import clickElement


class HomePage():
    createAccount = "//div[@class='panel header']//a[text()='Create an Account']"  # XPATH
    signIn = "//div[@class='panel header']//a[contains(text(),'Sign In')]"  # XPATH

    def __init__(self, driver):
        self.driver = driver

    def clickSignIn(self):
        clickElement(self.driver, self.signIn, 'XPATH')

    def clickCreateAccount(self):
        clickElement(self.driver, self.createAccount, 'XPATH')


