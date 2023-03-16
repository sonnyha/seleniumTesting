import AutoTesting
import os
import datetime
import time
import requests


from timeit import default_timer as timer
# start = timer() end = timer() print(end - start)

class ExecuteTesting:
    logfile = "\n"
    execution_status = "<Execution_Status Here>"
    execution_start = ""
    test_start_time = 0
    test_end_time = 0
    notification = []
    errorCounter = 0
    applicationSelection = -1
    browserSelection = -1
    AutoTestingObj = AutoTesting.AutoTesting()
    closeAppCode = -1
    connectionCode = -1
    # Welcome screen to get Application and Browser from user

    def welcomeText(self):
        print("\nWelcome to Automated Testing Script")
        self.applicationSelection = int(input("Select Application:\n"
                                            "1) Inventory Management\n"
                                            "2) Waterfield \n"
                                            "3) SharePoint\n"
                                            "4) OneStream\n"
                                            "5) Bad URL Test\n"
                                          ))
        self.browserSelection = int(input("Select Browser:\n"
                                      "1) Google Chrome\n"
                                      "2) Microsoft Edge\n"
                                      "3) Mozilla Firefox\n"
                                      ))
        self.AutoTestingObj.setSettings(self.applicationSelection, self.browserSelection)
        self.AutoTestingObj.applicationCode = self.applicationSelection
        self.AutoTestingObj.browserCode = self.browserSelection

    def connectionTest(self):
            self.connectionCode = requests.get(self.AutoTestingObj.url, verify=False).status_code
            print("Status Code: " + str(self.connectionCode))
    def connectionFailed(self):
        self.logfile = "\nConnection could not be made to " + self.AutoTestingObj.application + "! (Failed)" + "\nError Code: " + str(self.connectionCode)

    def connectionSuccessful(self):
        self.logfile = self.logfile + "\nConnection made to " + self.AutoTestingObj.application + " (successful)"

    def saveLogFile(self):
        return self.logfile

    def printSettings(self):
        print(self.AutoTestingObj.application)
        print(self.AutoTestingObj.browser)
        print(self.AutoTestingObj.url)

    def printAllSettings(self):
        print("\n--------------Settings and Configuration------------------")
        print("Application: ", self.AutoTestingObj.application)
        print("Browser: ", self.AutoTestingObj.browser)
        print("URL: ", self.AutoTestingObj.url)
        print("File Path: ", self.AutoTestingObj.filePath)
        print("Application Code: ", self.AutoTestingObj.applicationCode)
        print("Browser Code: ", self.AutoTestingObj.browserCode)

    def printLog(self):
        print(self.logfile)

    # Selenium has an exception library and will be implemented into
    # this block in the future
    def errorTest(self, testingFunction, *args, **kwargs):
        try:
            testingFunction(*args, **kwargs)
        except Exception as exceptionRaised:
            print(f"Exception Type: {exceptionRaised}")
            self.notification.append(exceptionRaised)
            self.errorCounter = self.errorCounter + 1
            return exceptionRaised

#   Defines a new log file and execution status,
#   the creates a new instance of AutoTesting and begins the testing process
    def launchAutoTesting(self):
        AutoTestingObj = AutoTesting.AutoTesting()
        now = datetime.datetime.now()
        self.execution_start = str(now.strftime("%x %X"))
        self.logfile = self.logfile + "----------Log File For " + self.AutoTestingObj.application + "---------------"
        self.logfile = self.logfile + "\nGo To Application " + self.AutoTestingObj.application + " (successful)"

#   Provides a response to users defined in the notification list that the execution
    #   has completed, the status of the test, and the time/duration of the testing execution
    def reportAutoTesting(self):
        print(
            "Testing Start Time: " + self.execution_start + os.linesep +
            "Num of Errors found: " + str(self.errorCounter) + os.linesep +
            str(self.notification)
        )

    def goToApplication(self):
        self.AutoTestingObj.goToApplication()

    def setServiceObject(self):
        self.AutoTestingObj.setServiceObject()

# dummy functions to test for raising exceptions
    def divisionByZero(self):
        result = 1/0
        return result

    def charPlusInt(self):
        result = 'c' + 1
        return result

    def outOfIndex(self):
        result = [1, 2]
        return result[3]

    def this_passes(self):
        result = 1/1
        return result

    def openTest(self):
        return open("fakeTextFile.txt")

    def goToURLTest(self, url):
        self.AutoTestingObj.goToURL(url)
        self.logfile = self.logfile + "\nGo To URL: " + url + " (successful)"
        time.sleep(2)
        return

    def startTime(self):
        self.test_start_time = time.time()

    def endTime(self):
        self.test_end_time = time.time()

    def timeElapsed(self):
        time_elapsed = self.test_end_time - self.test_start_time
        print("Time Elapsed: ", str("%.2f" % time_elapsed) + " seconds")

    def closeAppPrompt(self):
        self.closeAppCode = self.AutoTestingObj.exitApplication()
        return self.closeAppCode

    def clickOnObject(self, locator, locatorName):
        self.AutoTestingObj.clickOnObj(locator, locatorName)
        self.logfile = self.logfile + "\nClick On web element " + locator + ": " + locatorName + " (successful)"
        return




# Libraries needed
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# def handleError(driver, locator):
#     try:
#         # Find the web element using the given locator
#         element = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located(locator)
#         )
#         return element
#     except NoSuchElementException as e:
#         # This block will execute if the element is not found
#         # Here, we print the exception message and return the exception object
#         print(f"An exception occurred: {e}")
#         return e
