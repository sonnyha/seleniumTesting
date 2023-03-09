import AutoTesting
import os
import datetime

class ExecuteTesting:
    logfile = ""
    execution_status = "<Execution_Status Here>"
    execution_start = ""
    notification = []
    errorCounter = 0

    def errorTest(self, func, *args, **kwargs):
        try:
            # raise 10/0
            func(*args, **kwargs)
        except Exception as e:
            print(f"Exception Type: {e}")
            return e
        # finally:
        #     print("Executing finally clause")

#   Defines a new log file and execution status,
#   the creates a new instance of AutoTesting and begins the testing process
    def launchAutoTesting(self):
        AutoTestingObj = AutoTesting.AutoTesting()
        AutoTestingObj.intializingVariables()
        now = datetime.datetime.now()
        self.execution_start = str(now.strftime("%x %X"))
        return AutoTestingObj

#   Writes errors to the logfile and updates the execution_status on critical failure
#     def handlesError(self, result):
#         if result is True:
#             self.logfile = self.logfile + "Failed on Line 29"
#             self.execution_status = "Error Found"
#             self.notification.append("Web Element Not Found")
#             self.errorCounter = self.errorCounter + 1
#             return "Error ACA290x"
#         return "No Errors"

#   Provides a response to users defined in the notification list that the execution
    #   has completed, the status of the test, and the time/duration of the testing execution
    def reportAutoTesting(self):
        print(
            "Testing Start Time: " + self.execution_start + os.linesep +
            "Num of Errors found: " + str(self.errorCounter) + os.linesep +
            str(self.notification)
        )



#   Libraries needed
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
