import AutoTesting
import os
import datetime
from timeit import default_timer as timer
# start = timer() end = timer() print(end - start)

class ExecuteTesting:
    logfile = ""
    execution_status = "<Execution_Status Here>"
    execution_start = ""
    execution_finish = ""
    notification = []
    errorCounter = 0
    applicationSelection = -1
    browserSelection = -1
    AutoTestingObj = AutoTesting.AutoTesting()
    # Welcome screen to get Application and Browser from user
    #

    def welcomeText(self):
        print("\nWelcome to Automated Testing Script")
        self.applicationSelection = input("Select Application:\n"
                                            "1) Inventory Management\n"
                                            "2) Waterfield \n"
                                            "3) SharePoint\n"
                                            "4) OneStream\n"
                                          )
        self.browserSelection = input("Select Browser:\n"
                                      "1) Google Chrome\n"
                                      "2) Microsoft Edge\n"
                                      "3) Mozilla Firefox\n"
                                      )
        self.AutoTestingObj.applicationCode = self.applicationSelection
        self.AutoTestingObj.browserCode = self.browserSelection
        self.AutoTestingObj.setSettings(self.applicationSelection, self.browserSelection)

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
        AutoTestingObj.intializingVariables()
        now = datetime.datetime.now()
        self.execution_start = str(now.strftime("%x %X"))
        return AutoTestingObj

#   Provides a response to users defined in the notification list that the execution
    #   has completed, the status of the test, and the time/duration of the testing execution
    def reportAutoTesting(self):
        print(
            "Testing Start Time: " + self.execution_start + os.linesep +
            "Num of Errors found: " + str(self.errorCounter) + os.linesep +
            str(self.notification)
        )

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
