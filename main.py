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

print("--------------------Test Results--------------------")
test.reportAutoTesting()
print("")
test.printSettings()
print("")
test.printAllSettings()
# filePath = "/Users/sha549/Documents/chromedriver.exe"
# serviceObject = "Service(" + filePath + ")"
# print(serviceObject)