from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObject = Service("/Users/sha549/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=serviceObject)
driver.get("http://inventorymanagementdev:4431/")





