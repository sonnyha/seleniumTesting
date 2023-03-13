import ExecuteTesting as ET


test = ET.ExecuteTesting()
test.welcomeText()
test.launchAutoTesting()

# testing raising exception function
print("-----------------Exceptions Found-------------------")
test.errorTest(test.divisionByZero)
test.errorTest(test.charPlusInt)
test.errorTest(test.outOfIndex)
test.errorTest(test.openTest)

print("\n--------------------Test Results--------------------")
test.reportAutoTesting()
print("")
test.printSettings()
print("")
test.printAllSettings()
test.goToApplication()
