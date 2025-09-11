from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Use the new headless mode for better compatibility
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Explicitly set the path to the Chromium binary, as used in your workflow
chrome_bin = os.environ.get("CHROME_BIN", "/usr/bin/chromium-browser")
chrome_options.binary_location = chrome_bin

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
url = "https://jpteunm.com"
driver.get(url)

try:
    assert ("JPTE" in driver.title) or ("UNM" in driver.title)
    links = driver.find_elements(By.LINK_TEXT, "Login")
    if links:
        assert links[0].is_displayed()
    print("Functional test passed!")
except AssertionError as e:
    print("Functional test failed!", e)
    raise SystemExit(1)
finally:
    driver.quit()
