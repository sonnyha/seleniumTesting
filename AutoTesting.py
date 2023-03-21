import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import SessionNotCreatedException
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
    filePath = "/Users/sha549/Documents/chromedriver.exe"     # File Path hardcoded for now
    serviceObject = Service(filePath)
    application = ""
    applicationCode = -1
    browserCode = -1
    closeProgram = -1
    # Application Option
    applications = {
        1: ["Inventory Management (Prod)", "http://inventorymanagement.targa.com/"],
        2: ["Inventory Management (Dev)", "http://inventorymanagementdev.targa.com/"],
        4: ["OneStream", "http://onestream.com/"],
        5: ["Bad URL Test", "http://ThisIsAFakeURL23049012387wx1.com/"]
    }
    # Types of browsers
    browsers = {
        1: ["Google Chrome",  webdriver.Chrome, "/Users/sha549/Documents/chromedriver.exe"],
        2: ["Microsoft Edge", webdriver.Edge, "/Users/sha549/Documents/msedgedriver.exe"],
        3: ["Mozilla Firefox", webdriver.Firefox, "/Users/sha549/Documents/chromedriver.exe"]
    }

    def setSettings(self, appCode, browserCode):
        self.application = self.applications[appCode][0]
        self.browser = self.browsers[browserCode][0]
        self.url = self.applications[appCode][1]

    #   Everything points to Chrome driver for now
    def setServiceObject(self):
        self.serviceObject = Service(self.browsers[self.browserCode][2])

    def goToApplication(self):
        try:
            self.driver = self.browsers[self.browserCode][1](service=self.serviceObject)
        except SessionNotCreatedException as exceptionRaised:
            print("\nUnable to start session. \nPlease check webdriver and browser version.\n")
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


# add selenium exceptions here:





# class AutoTesting:
#     url = ""
#     browser = ""
#     driver = ""
#     application = ""
#     filePath = ""
#     serviceObject = ""
#     applications = {
#         1: "Marketer Book",
#         2: "Inventory Valuation",
#         3: "Inventory Management System"
#     }
#     browsers = {
#         1: "Google Chrome",
#         2: "Mozilla Firefox",
#         3: "Microsoft Edge"
#     }
#
#     def initVariables(self):
#         print(os.linesep +
#                 'Marketer Book - 1' + os.linesep +
#                 'Inventory Valuation - 2' + os.linesep +
#                 'Inventory Management System (Both)- 3' + os.linesep
#         )
#         app = input("Select Application Number: ")
#         checkForValidNum = False
#
#         #   Protects from Invalid Inputs
#         while checkForValidNum is not True:
#             try:
#                 self.applications[int(app)]
#                 checkForValidNum = True
#                 self.applications[int(app)]
#             except ValueError:
#                 print("Invalid Selection... try again!")
#                 app = input("Select Application Number: ")
#             except KeyError:
#                 print("Invalid Selection... try again!")
#                 app = input("Select Application Number: ")
#
#         print(os.linesep +
#                 'Google Chrome - 1' + os.linesep +
#                 'Mozilla Firefox - 2' + os.linesep +
#                 'Microsoft Edge - 3' + os.linesep
#         )
#         currentBrowser = input("Select Browser Number: ")
#         filePath = input("Driver File Path: ")
#         self.application = self.applications[int(app)]
#         self.browser = self.browsers[int(currentBrowser)]
#         #   Hard coded for now
#         self.filePath = "/Users/sha549/Documents/chromedriver.exe"
#
#     def setApplication(self, app):
#         self.application = app
#
#     def getApplication(self):
#         return self.application
