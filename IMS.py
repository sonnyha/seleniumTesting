from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serviceObject = Service("/Users/sha549/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=serviceObject)
driver.get("http://inventorymanagementdev:4431/")
WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, "header")))
driver.implicitly_wait(5)






