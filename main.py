import ExecuteTesting as ET

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
#   testing URL Change function
test.goToURLTest("https://www.reddit.com") #  Testing Purposes
test.endTime()
test.timeElapsed()
