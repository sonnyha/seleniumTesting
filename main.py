from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from importTest import testFunction

#   bare minimum you need for selenium to work
#   initialize the service (where your driver lives, in this case chromedriver)
#   initialize driver... this object is what you will use to manipulate the web application
serviceObject = Service("/Users/sha549/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=serviceObject)

#   this will set 'driver' to the url in question
driver.get("https://www.google.com")
#   waits for x amount of seconds for task to complete, if it's complete it will move on to next step
#   NOTE: it's global, use an explicit wait if it's just one element...
#   wait = WebDriverWait(driver, 10)
#   wait.until(expected_conditions.presence_of_element_located(By.CSS_Selector, ".someClass"))
driver.implicitly_wait(5)

print(testFunction())
