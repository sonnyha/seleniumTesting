import ExecuteTesting as ET

print("------------------Testing Execute Testing------------------")

# Simulating a test result that passes or fails
dummy_test1 = True
dummy_test2 = False
test = ET.ExecuteTesting()

print("------------------Object's Initial State------------------")
# Object When called
test.launchAutoTesting()
print(test.logfile, test.execution_status, test.execution_start, test.notification)
test.reportAutoTesting()

print("------------------Object Passes Testing------------------")
# Object when it passes testing
test.handlesError(dummy_test1)
print(test.logfile, test.execution_status, test.execution_start, test.notification)
test.reportAutoTesting()

print("------------------Object Fails Testing------------------")
# Object when it fails testing
test.handlesError(dummy_test2)
print(test.logfile, test.execution_status, test.execution_start, test.notification)
test.reportAutoTesting()

