from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# import time


class AutoTesting:
    url = ""
    browser = ""
    driver = ""
    application = ""
    filePath = ""
    serviceObject = ""
    applications = []
    browsers = []
    testing = "hello world"
    def initVariables(self):
        app = input("Select Application:")
        currentBrowser = input("Select Browser:")
        filePath = input("Driver File Path:")
        self.application = app
        self.browser = currentBrowser
        self.filePath = filePath

    def setApplication(self):
      print("setAppHere")

    def getApplication(self):
        print("getAppHere")

#   Testing Purposes
testVar = AutoTesting()
print(testVar.testing)
testVar.initVariables()
print(testVar.application)
print(testVar.browser)
print(testVar.filePath)
