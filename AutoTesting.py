import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# tool box module.... these are functions that can be used for all applications


class AutoTesting:
    url = ""
    browser = ""
    driver = ""
    application = ""
    filePath = ""
    serviceObject = ""
    applicationCode = -1
    browserCode = -1
    # Application Option
    applications = {
        1: "Inventory Management",
        2: "Waterfield",
        3: "SharePoint",
        4: "OneStream"
    }
    # Types of browsers
    browsers = {
        1: "Google Chrome",
        2: "Microsoft Edge",
        3: "Mozilla Firefox"
    }

    #
    def setSettings(self, application, browser):
        self.application = self.applications[application]
        self.browser = self.browser[browser]

    def exit(self):
        return "exit"

    def intializingVariables(self):
        return "init variable"

    def setApplication(self):
        return "set appplication"

    def getApllication(self):
        return "get application"

    def setBrowser(self):
        return "set browser"
    def getBrowserName(self):
        return "get browser name"
    def setPathToServiceObject(self):
        return "set path to service object"
    def getPathToServiceObject(self):
        return "get path to service object"
    def setURL(self):
        return "set URL"
    def getURL(self):
        return "get URL"
    def verifyComponents(self):
        return "verify components"
    def setMissingComponents(self):
        return "set missing Components"
    def changeBrowser(self):
        return"change browser"
    def beginTest(self):
        return "begin test"
    def cancelTest(self):
        return "cancel test"
    def pause(self):
        return "pause"
    def resume(self):
        return "resume"

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

# #   Testing Purposes
# testVar = AutoTesting()
# testVar.initVariables()
# print("---------Selections Made----------")
# print(testVar.application + os.linesep + testVar.browser + os.linesep + testVar.filePath)


