# dummy functions to test for raising exceptions
class FailedFunctions:
    def divisionByZero(self):
        result = 1/0
        return result

    def charPlusInt(self):
        result = 'c' + 1
        return result

    def outOfIndex(self):
        result = [1, 2]
        return result[3]

    def this_passes(self):
        result = 1/1
        return result

    def openTest(self):
        return open("fakeTextFile.txt")
