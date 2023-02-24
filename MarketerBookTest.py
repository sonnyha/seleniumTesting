from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

url = "http://inventorymanagementdev:4431/"

#   Keeps window open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#   Path to WebDriver
serviceObject = Service("/Users/sha549/Documents/chromedriver.exe")

driver = webdriver.Chrome(service=serviceObject, options=chrome_options)

#   URL being loaded
#   Inventory Management System Dev Environment
driver.get(url)
driver.maximize_window()

outputArray = []

#   Waiting for Header to load... time out after 10 seconds
WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, "header")))

#   Test if element is there and return a string that tells if element is visible
if EC.presence_of_element_located((By.ID, "header")):
    print("Header Element Shown...")
    outputArray.append("Header Shown")
else:
    print("Header Element missing...")
    outputArray.append("Header missing...")

#   Going into Marketer Book
driver.find_element(By.PARTIAL_LINK_TEXT, "Marketer Book").click()
# driver.implicitly_wait(5)
WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, "begin_inventory_table")))

#   Click on 'N/A' Tab under the Beginning Inventory (Marketer Book)
driver.find_element(By.XPATH, '//*[@id="tabstrip-BeginInventory"]/ul/li[2]').click()
print("Testing Beginning Inventory 'N/A' Tab ")
outputArray.append("Testing Beginning Inventory 'N/A' Tab ")
time.sleep(1)

#   Click on 'N/A' Tab under the Ending Inventory (Marketer Book)
driver.find_element(By.XPATH, '//*[@id="tabstrip-EndInventory"]/ul/li[2]').click()
print("Testing Ending Inventory 'N/A' Tab ")
outputArray.append("Testing Ending Inventory 'N/A' Tab ")
time.sleep(1)

#   Array for Holding Direction Names
List1 = ["", "Marketer", "Supply", "Demand", "Gain/Loss", "Other Revenue", "Other Expenses", "Other Inventory"]

for i in range(1, 8):
    Xpath = '//*[@id="gridDisplayTab"]/ul/li[' + str(i) + ']'
    driver.find_element(By.XPATH, Xpath).click()
    print("Marketer Tab Functional ", List1[i])
    outputArray.append("Marketer Tab Functional " + List1[i])
    time.sleep(1)

HeaderDropDownList = ["Accounting Period Dropdown", "Inventory Pool DropDown", "Quantity Unit Dropdown", "Price Unit Dropdown"]

XpathDictionary = {
    "Accounting Period Dropdown": "//body[1]/div[1]/main[1]/section[1]/div[2]/div[1]/div[1]/span[1]/span[1]/span[2]/span[1]",
    "Inventory Pool DropDown": "//body[1]/div[1]/main[1]/section[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[2]/span[1]",
    "Quantity Unit Dropdown": "//body[1]/div[1]/main[1]/section[1]/div[2]/div[1]/div[3]/span[1]/span[1]/span[2]/span[1]",
    "Price Unit Dropdown": "//body[1]/div[1]/main[1]/section[1]/div[2]/div[1]/div[3]/span[2]/span[1]/span[2]/span[1]"
}

for dropdown in HeaderDropDownList:
    driver.find_element(By.XPATH, XpathDictionary[dropdown]).click()
    print("Testing " + dropdown)
    time.sleep(.5)

driver.find_element(By.ID, "RefreshButton").click()
WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, "filter-controls")))
print("Testing Refresh button")

#   Testing Period Increase Button
WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, "filter-controls")))
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "periodIncrease")))
time.sleep(2)
button.click()
print("Testing Period Increase Button")

#   Testing Period Decrease Button
WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, "filter-controls")))
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "periodDecrease")))
time.sleep(2)
button.click()
print("Testing Period Decrease Button")

# WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "//body[1]/div[1]/main[1]/section[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[2]/span[1]")))
# driver.find_element(By.XPATH, "//input[@id='inventoryPoolDropDown']")
#   Output to Text File (outputFile.txt)
with open('outputFile.txt', 'w') as f:
    for line in outputArray:
        f.write(line)
        f.write('\n')

# driver.close()



