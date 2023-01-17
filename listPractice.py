import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObject = Service("/Users/sha549/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=serviceObject)
driver.get("https://www.google.com")
driver.find_element(By.CLASS_NAME, "gLFyf").click()
trendingSearches = driver.find_elements(By.CLASS_NAME, "sbct")

for search in trendingSearches:
    print(search.text)

