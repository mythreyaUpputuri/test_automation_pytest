import os.path
import time


def takeScreenshot(driver, testCase):

    fileName = "{}".format(testCase) + str(round(time.time() * 1000)) + ".png"
    screenShotDirectory = os.path.abspath(os.curdir) + "/screenshots/"
    destinationFile = screenShotDirectory + fileName
    print("Destination File is :" + destinationFile)

    try:
        driver.save_screenshot(destinationFile)
    except NotADirectoryError:
        print("not a directory issue")
