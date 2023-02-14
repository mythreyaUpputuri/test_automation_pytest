from selenium.webdriver.common.by import By
from utilities.handleElements import clickElement, sendKeysElement
import time


class RegistrationPage():
    firstName = "input#firstname"  # CSS Selector
    lastName = "input#lastname"  # CSS Selector
    email = "input#email_address"  # CSS Selector
    password = "input#password"  # CSS Selector
    confirmPwd = "input#password-confirmation"  # CSS Selector
    createAccount = "//button[@title= 'Create an Account']" # XPATH
    accountSucessBanner = "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']"

    def __init__(self, driver):
        self.driver = driver

    def enterFirstName(self, first_name):
        sendKeysElement(self.driver, self.firstName, "CSS_SELECTOR", first_name)

    def enterLastName(self, last_name):
        sendKeysElement(self.driver, self.lastName, "CSS_SELECTOR", last_name)

    def enterEmail(self, email_id):
        sendKeysElement(self.driver, self.email, "CSS_SELECTOR", email_id)

    def enterPassword(self, pwd):
        sendKeysElement(self.driver, self.password, "CSS_SELECTOR", pwd)

    def confirmPassword(self, pwd):
        sendKeysElement(self.driver, self.confirmPwd, "CSS_SELECTOR", pwd)

    def clickCreateAccount(self):
        clickElement(self.driver, self.createAccount, "XPATH")

    # def noNewsLetter(self):
    #     noSubscribeButton = self.driver.find_element(By.CSS_SELECTOR, self.noSubscribe)
    #     selection = noSubscribeButton.is_selected()
    #     if not selection:
    #         noSubscribeButton.click()
    #
    # def yesNewsLetter(self):
    #     yesSubscribeButton = self.driver.find_element(By.CSS_SELECTOR, self.yesSubscribe)
    #     selection = yesSubscribeButton.is_selected()
    #     if not selection:
    #         yesSubscribeButton.click()


