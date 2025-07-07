from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Starting...")
driver = webdriver.Firefox()
driver.get("https://www.numbeo.com/cost-of-living/")
assert "Cost of Living" in driver.title

try:

    wait = WebDriverWait(driver, 10)

    search_box = wait.until(EC.presence_of_element_located((By.ID, 'city_selector_city_id')))
    search_box.clear()
    search_box.send_keys(print(input("Write the location: ")))
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)

    try:
        close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ui-button-icon-primary ui-icon ui-icon-closethick')))
        close_button.click()
        print("Popup fechado")
    except:
        print("Popup não apareceu")

finally:
    driver.quit()
