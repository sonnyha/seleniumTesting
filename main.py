import ExecuteTesting as ET
import TestingFunction as TestFunc
appOpen = -1
logfile = ""

while appOpen != 2:
    test = ET.ExecuteTesting()
    test.welcomeText()
    test.launchAutoTesting()
    test.startTime()
    # # testing raising exception function
    # print("\n-----------------Exceptions Found-------------------")
    # test.errorTest(test.divisionByZero)
    # test.errorTest(test.charPlusInt)
    # test.errorTest(test.outOfIndex)
    # test.errorTest(test.openTest)
    # print("\n--------------------Test Results--------------------")
    # test.reportAutoTesting()
    # print("\n-------------------Print Settings-------------------")
    # test.printAllSettings()
    # test.setServiceObject()
    test.goToApplication()
    try:
        test.connectionTest()
    except Exception as exceptionRaised:
        test.connectionFailed()
    else:
        test.connectionSuccessful()
        print("Connection Initiated...")



    # # #   Testing URL Change function in main.py
    # test.goToURLTest("https://www.targaresources.com")      # Testing Purposes (will not be in main.py)
    # test.goToURLTest("https://www.bbc.com/")                # Testing Purposes (will not be in main.py)
    # test.goToURLTest("https://www.google.com/")             # Testing Purposes (will not be in main.py)
    # #   Testing clickOnObject function in main.py
    # test.clickOnObject("class", "gLFyf")  # Testing purposes only (will not be in main.py) (only works for 2)
    # test.clickOnObject("class", "sbct")  # Testing purposes only (will not be in main.py) (only works for 2)

    test.endTime()
    test.timeElapsed()
    appOpen = int(test.closeAppPrompt())    # Returns 1 (Yes) or 2 (No), Loops if 1
    logfile = logfile + test.logfile
    # test.printLog()
test.printAllSettings()
print(logfile)
print("\nThank you, come again.")























