from selenium.webdriver.common.by import By
from utilities.screenshots import takeScreenshot


def getByType(locatorType):
    locatorType = locatorType.lower()
    if locatorType == "id":
        return By.ID
    elif locatorType == "xpath":
        return By.XPATH
    elif locatorType == "css_selector":
        return By.CSS_SELECTOR
    elif locatorType == "name":
        return By.NAME
    elif locatorType == "class_name":
        return By.CLASS_NAME
    elif locatorType == "tag_name":
        return By.TAG_NAME
    elif locatorType == "link_text":
        return By.LINK_TEXT
    elif locatorType == "partial_link_text":
        return By.PARTIAL_LINK_TEXT
    else:
        print("Locator type is not Supported")


def getElement(driver, locator, locatorType):
    byType = getByType(locatorType)
    element = driver.find_element(byType, locator)
    return element


def sendKeysElement(driver, locator, locatorType='ID', text=''):
    element = getElement(driver, locator, locatorType)
    element.send_keys(text)


def clickElement(driver, locator, locatorType='ID'):
    element = getElement(driver, locator, locatorType)
    element.click()


def scrollToElement(driver, locator, locatorType):
    element = getElement(driver, locator, locatorType)
    driver.execute_scrpit("arguements[0].scrollIntoView(true);", element)
