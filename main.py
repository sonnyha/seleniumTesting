from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#   bare minimum you need for selenium to work
#   initialize the service (where your driver lives, in this case chromedriver)
#   initialize driver... this object is what you will use to manipulate the web application
serviceObject = Service("/Users/sha549/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=serviceObject)

#   this will set 'driver' to the url in question
driver.get("https://www.google.com")
