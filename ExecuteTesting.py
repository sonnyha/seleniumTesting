class ExecuteTesting:
    logfile = ""
    execution_status = ""
    execution_start = ""
    notification = []

#   Defines a new log file and execution status,
#   the creates a new instance of AutoTesting and begins the testing process
    def launchAutoTesting(self):
        return "hello world"

#   Writes errors to the logfile and updates the execution_status on critical failure
    def handlesError(self):
        return "hello error"

#   Provides a response to users defined in the notification list that the execution
    #   has completed, the status of the test, andthe time/duration of the testing execution
    def reportAutoTesting(self):
        return "Yes me lord?"
