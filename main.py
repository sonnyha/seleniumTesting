import ExecuteTesting as ET
appOpen = -1

while appOpen != 2:
    test = ET.ExecuteTesting()
    test.welcomeText()
    test.launchAutoTesting()
    test.startTime()
    # testing raising exception function
    print("\n-----------------Exceptions Found-------------------")
    test.errorTest(test.divisionByZero)
    test.errorTest(test.charPlusInt)
    test.errorTest(test.outOfIndex)
    test.errorTest(test.openTest)
    print("\n--------------------Test Results--------------------")
    test.reportAutoTesting()
    print("\n-------------------Print Settings-------------------")
    # test.printSettings()
    test.printAllSettings()
    test.setServiceObject()
    test.goToApplication()
    test.clickOnObject("class", "gLFyf")  # Testing purposes only (will not be in main.py) (only works for 2)
    test.clickOnObject("class", "sbct")  # Testing purposes only (will not be in main.py) (only works for 2)
    test.endTime()
    test.timeElapsed()
    appOpen = int(test.closeAppPrompt())    # Returns 1 (Yes) or 2 (No), Loops if 1


























    # #   testing URL Change function
    # test.goToURLTest("https://www.targaresources.com")      # Testing Purposes
    # test.goToURLTest("https://www.google.com/")             # Testing Purposes
    # test.goToURLTest("https://www.bbc.com/")                # Testing Purposes