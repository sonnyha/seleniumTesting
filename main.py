import ExecuteTesting as ET
import TestingFunction as TestFunc


appOpen = -1
logfile = ""

while appOpen != 2:
    test = ET.ExecuteTesting()
    test.welcomeText()
    test.launchAutoTesting()
    test.startTime()
    test.goToApplication()
    try:
        test.connectionTest()
    except Exception as exceptionRaised:
        test.connectionFailed()
    else:
        if test.connectionCode == 404:
            test.connectionFailed()
        else:
            test.connectionSuccessful()
            print("Connection Initiated...")
    test.endTime()
    test.timeElapsed()
    appOpen = int(test.closeAppPrompt())    # Returns 1 (Yes) or 2 (No), Loops if 1
    logfile = logfile + test.logfile
test.printAllSettings()
print(logfile)
print("\nThank you, come again.")








# # #   Testing URL Change function in main.py
# test.goToURLTest("https://www.targaresources.com")      # Testing Purposes (will not be in main.py)
# test.goToURLTest("https://www.bbc.com/")                # Testing Purposes (will not be in main.py)
# test.goToURLTest("https://www.google.com/")             # Testing Purposes (will not be in main.py)
# #   Testing clickOnObject function in main.py
# test.clickOnObject("class", "gLFyf")  # Testing purposes only (will not be in main.py) (only works for 2)
# test.clickOnObject("class", "sbct")  # Testing purposes only (will not be in main.py) (only works for 2)


















