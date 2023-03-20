from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

#   IMSTester is a module used for testing Inventory Management System (IMS)
#   Testing Functions for IMS
#   Still In Progress...

def startIMSTest():
    url = "http://inventorymanagementdev:4431/"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    serviceObject = Service("/Users/sha549/Documents/chromedriver.exe")
    driver = webdriver.Chrome(service=serviceObject, options=chrome_options)
    driver.get(url)
    driver.maximize_window()

#   Test if element is there and return a string that tells if element is visible
def headerCheck():
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, "header")))
    if EC.presence_of_element_located((By.ID, "header")):
        print("Header Element Shown...")
    else:
        print("Header Element missing...")
def goToMarketerBook():
    driver.find_element(By.PARTIAL_LINK_TEXT, "Marketer Book").click()
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, "begin_inventory_table")))

    #   Checking the N/A tab under the Beginning Inventory (Marketer Book) and Ending Inventory
def checkNA():
    driver.find_element(By.XPATH, '//*[@id="tabstrip-BeginInventory"]/ul/li[2]').click()
    print("Testing Beginning Inventory 'N/A' Tab ")
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="tabstrip-EndInventory"]/ul/li[2]').click()
    print("Testing Ending Inventory 'N/A' Tab ")
    time.sleep(1)

def checkDirectionTabs():
    List1 = ["", "Marketer", "Supply", "Demand", "Gain/Loss", "Other Revenue", "Other Expenses", "Other Inventory"]
    for i in range(1, 8):
        Xpath = '//*[@id="gridDisplayTab"]/ul/li[' + str(i) + ']'
        driver.find_element(By.XPATH, Xpath).click()
        print("Marketer Tab Functional ", List1[i])
        time.sleep(1)

def marketerHeaderCheck():
    HeaderDropDownList = ["Accounting Period Dropdown",
                          "Inventory Pool DropDown",
                          "Quantity Unit Dropdown",
                          "Price Unit Dropdown"]
    XpathDictionary = {
        "Accounting Period Dropdown":
            "//body[1]/div[1]/main[1]/section[1]/div[2]/div[1]/div[1]/span[1]/span[1]/span[2]/span[1]",
        "Inventory Pool DropDown":
            "//body[1]/div[1]/main[1]/section[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[2]/span[1]",
        "Quantity Unit Dropdown":
            "//body[1]/div[1]/main[1]/section[1]/div[2]/div[1]/div[3]/span[1]/span[1]/span[2]/span[1]",
        "Price Unit Dropdown":
            "//body[1]/div[1]/main[1]/section[1]/div[2]/div[1]/div[3]/span[2]/span[1]/span[2]/span[1]"
    }

    for dropdown in HeaderDropDownList:
        driver.find_element(By.XPATH, XpathDictionary[dropdown]).click()
        print("Testing " + dropdown)
        time.sleep(.5)

def refreshMarketerBook():
    driver.find_element(By.ID, "RefreshButton").click()
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, "filter-controls")))
    print("Testing Refresh button")

def AccountingPeriodInceaseButton():
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, "filter-controls")))
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "periodIncrease")))
    time.sleep(2)
    button.click()
    print("Testing Period Increase Button")

def AccountingPeriodDeceaseButton():
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, "filter-controls")))
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "periodDecrease")))
    time.sleep(2)
    button.click()
    print("Testing Period Decrease Button")
def output(Arr):
    with open('outputFile.txt', 'w') as f:
        for line in Arr:
            f.write(line)
            f.write('\n')

