import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import SessionNotCreatedException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import SeleniumManagerException


from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# tool box module.... these are functions that can be used for all applications


class AutoTesting:
    url = ""
    browser = ""
    filePath = ""
    application = ""
    applicationCode = -1
    browserCode = -1
    closeProgram = -1
    # Application Option
    applications = {
        1: ["Inventory Management (Prod)", "http://inventorymanagement.targa.com/"],
        2: ["Inventory Management (Dev)", "http://inventorymanagementdev.targa.com/"],
        3: ["OneStream", "http://onestream.com/"],
        4: ["Bad URL Test", "http://ThisIsAFakeURL23049012387wx1.com/"],
        5: ["Exit", "", ""]
    }
    # Types of browsers
    browsers = {
        1: ["Google Chrome",  webdriver.Chrome, '/Users/sha549/PycharmProjects/seleniumTesting/Drivers/chromedriver.exe'],
        2: ["Microsoft Edge", webdriver.Edge, '/Users/sha549/PycharmProjects/seleniumTesting/Drivers/msedgedriver.exe'],
        3: ["Mozilla Firefox", webdriver.Firefox, '/Users/sha549/PycharmProjects/seleniumTesting/firefoxdriver.exe'],
        4: ["Exit", "", ""]
    }

    def setSettings(self, appCode, browserCode):
        self.application = self.applications[appCode][0]
        self.browser = self.browsers[browserCode][0]
        self.url = self.applications[appCode][1]
        self.filePath = self.browsers[browserCode][2]

    #   Everything points to Chrome driver for now
    def setServiceObject(self):
        self.serviceObject = Service(self.browsers[self.browserCode][2])

    def goToApplication(self):
        serviceObject = Service(self.filePath)
        try:
            self.driver = self.browsers[self.browserCode][1](service=serviceObject)
        except SessionNotCreatedException as exceptionRaised:
            print("\nUnable to start session. \nPlease check webdriver and browser version.\n")
            print("Session Aborted.\n")
            quit()
        except SeleniumManagerException as ManagerException:
            print("\nUnable to start session. \nPlease check your webdriver path.\n")
            print("Session Aborted\n")
            quit()
        except WebDriverException as WebDriverExcept:
            print("\nUnable to start session. \nPlease check your webdriver path and settings\n")
            print("Session Aborted.\n")
            quit()
        else:
            self.driver.get(self.applications[self.applicationCode][1])
        time.sleep(2)

    def goToURL(self, url):
        self.driver.get(url)
        return url

    #   In Progress
    def clickOnObj(self, locator, locatorName):
        match locator.casefold():
            case "class":
                self.driver.find_element(By.CLASS_NAME, locatorName).click()
            case "xpath":
                self.driver.find_element(By.XPATH, locatorName).click()
            case "id":
                self.driver.find_element(By.ID, locatorName).click()
            case "name":
                self.driver.find_element(By.NAME, locatorName).click()
            case "css":
                self.driver.find_element(By.CSS_SELECTOR, locatorName).click()
            case "link":
                self.driver.find_element(By.LINK_TEXT, locatorName).click()
            case "partial":
                self.driver.find_element(By.PARTIAL_LINK_TEXT, locatorName).click()
        time.sleep(2)
        return 0

    def exitApplication(self):
        self.driver.close()
        self.closeProgram = input("\nWould you like to perform another Test? \n 1: Yes \n 2: No\n")
        return self.closeProgram

    def setPathToServiceObject(self, path):
        self.filePath = path

    def getPathToServiceObject(self):
        return self.filePath

    def setURL(self, url):
        self.url = url

    def getURL(self):
        return self.url

    def sendKeys(self, comment, keysToSend):
        return 0
