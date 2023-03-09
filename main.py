import ExecuteTesting as ET


# dummy function to test for failures
def divisionByZero():
    result = 1/0
    return result


# dummy functions to test for raising exceptions
def this_passes():
    result = 1/1
    return result

def charPlusInt():
    result = 'c' + 1
    return result


def outOfIndex():
    result = [1, 2]
    return result[3]

print("------------------Testing Execute Testing------------------")

# Simulating a test result that passes or fails
dummy_test1 = True
dummy_test2 = False
test = ET.ExecuteTesting()

test.errorTest(divisionByZero)
test.errorTest(charPlusInt)
test.errorTest(outOfIndex)




# print("------------------Object's Initial State------------------")
# # Object When called
# test.launchAutoTesting()
# print(test.logfile, test.execution_status, test.execution_start, test.notification)
# test.reportAutoTesting()
#
# print("------------------Object Passes Testing------------------")
# # Object when it passes testing
# test.handlesError(dummy_test1)
# print(test.logfile, test.execution_status, test.execution_start, test.notification)
# test.reportAutoTesting()
#
# print("------------------Object Fails Testing------------------")
# # Object when it fails testing
# test.handlesError(dummy_test2)
# print(test.logfile, test.execution_status, test.execution_start, test.notification)
# test.reportAutoTesting()


