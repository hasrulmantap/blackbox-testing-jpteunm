import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = '/usr/bin/chromium-browser'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://jpteunm.com")
assert driver.title != ""
driver.quit()
print("Compatibility test (basic) passed!")

