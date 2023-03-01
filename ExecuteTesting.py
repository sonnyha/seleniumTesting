import AutoTesting
import os
class ExecuteTesting:
    logfile = ""
    execution_status = ""
    execution_start = ""
    notification = []

#   Defines a new log file and execution status,
#   the creates a new instance of AutoTesting and begins the testing process
    def launchAutoTesting(self):
        AutoTestingObj = AutoTesting.AutoTesting()
        AutoTestingObj.initVariables()
        return AutoTestingObj

#   Writes errors to the logfile and updates the execution_status on critical failure
    def handlesError(self):
        errorFound = False
        if errorFound is True:
            self.logfile = self.logfile + " error here"
            self.execution_status = "Type of Error"
            return "Error 42069"
        return "No Errors"

#   Provides a response to users defined in the notification list that the execution
    #   has completed, the status of the test, andthe time/duration of the testing execution
    def reportAutoTesting(self):
        print(
            "Testing Start Time: " + self.execution_start + os.linesep +
            "Duration: " + " Minutes(End Time - Start Time)" + os.linesep +
            "Num of Errors found: " + os.linesep +
            "Types of Errors List Here"
        )
