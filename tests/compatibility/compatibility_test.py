import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
chrome_bin = os.environ.get("CHROME_BIN", r"C:\Program Files\Google\Chrome\Application\chrome.exe")
if os.path.exists(chrome_bin):
    options.binary_location = chrome_bin

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://jpteunm.com")
assert driver.title != ""
driver.quit()
print("Compatibility test (basic) passed!")

