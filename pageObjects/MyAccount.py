from selenium.webdriver.common.by import By


class MyAccount():
    successfulRegistrationBanner = "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']"

    def __init__(self, driver):
        self.driver = driver

    def validateRegistrationBanner(self):
        actualMessage = self.driver.find_element(By.XPATH, self.successfulRegistrationBanner).text
        if actualMessage == "Thank you for registering with Fake Online Clothing Store.":
            assert True
        else:
            assert False
