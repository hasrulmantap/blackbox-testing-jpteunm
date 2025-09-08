import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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

try:
    body = driver.find_element(By.TAG_NAME, "body")
    assert body.is_displayed()
    print("Usability basic checks passed!")
except Exception as e:
    print("Usability test failed!", e)
    raise SystemExit(1)
finally:
    driver.quit()

