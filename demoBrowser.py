from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# import options from selenium.webdriver.chrome.options
chrome_options = Options()

# adds an argument to chrome_options...this disables the notifications you get from websites
chrome_options.add_argument('--disable-notifications')

# stops browser from closing
chrome_options.add_experimental_option("detach", True)

# declare 'serviceObject' to the path of the webdriver
serviceObject = Service("/Users/sha549/Documents/chromedriver.exe")

# declare 'driver' from webdriver library
driver = webdriver.Chrome(service=serviceObject, options=chrome_options)

driver.maximize_window()
driver.get("https://www.reddit.com/r/OverwatchUniversity")

# driver attributes
print(driver.title)
print(driver.current_url)

# select elements by ID, Xpath, CSS Selector, name, Classname, linktext.... find_element()
# you have to import 'By' as well 'from selenium.webdriver.common.by import By'
# consider using the chrome extension 'selectorshub' to find unique ids/classes or xpath/css
driver.find_element(By.ID, "header-search-bar").send_keys("Kiriko")
driver.find_element(By.CLASS_NAME, "_2aqH0n-kSzFY7HZZ5GL-Jb").click()