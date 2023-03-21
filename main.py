import ExecuteTesting as ET

appOpen = -1
logfile = ""

while appOpen != 2:
    test = ET.ExecuteTesting()
    test.welcomeText()                      # Gathers input for application and browser (exit option as well)
    test.launchAutoTesting()                # Sets time of test and initializes logfile
    test.startTime()                        # Store beginning time for time elapsed
    test.goToApplication()                  # Launches web driver to respective application
    try:
        test.connectionTest()               # Checks for connection status code
    except Exception as exceptionRaised:
        test.connectionFailed()             # if something breaks with webdriver
    else:
        if test.connectionCode == 404:      # if connection not made
            test.connectionFailed()
        else:
            test.connectionSuccessful()
            print("Connection Initiated...")
    test.endTime()                          # Ending Time
    print(test.timeElapsed())                      # timeElapsed = (Ending Time - Start Time)
    appOpen = int(test.closeAppPrompt())    # Returns 1 (Yes) or 2 (No), Loops if 1
    logfile += test.logfile        # Storing logs
test.printAllSettings()                     # Print settings
print(logfile)                              # Print log
print("\nThank you, come again.")

















