from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch Chrome
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.com")

    # Find the search box
    search_box = driver.find_element(By.NAME, "q")

    # Enter search query
    search_box.send_keys("Python Selenium tutorial")

    # Press Enter
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(3)

    # Print page title
    print(driver.title)

finally:
    driver.quit()