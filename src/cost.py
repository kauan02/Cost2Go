import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def scrap():
    local = input("Tap the city: ")
    
    driver = webdriver.Firefox()
    
    print("Starting...")
    driver.get("https://www.numbeo.com/cost-of-living/")
    
    search_bar = driver.find_element(By.ID, "city_selector_city_id")
    search_bar.send_keys(local)
    time.sleep(1)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(3)
    
    table = driver.find_element(By.CLASS_NAME, "data_wide_table")
    rows = table.find_elements(By.TAG_NAME, "tr")
    
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) >= 2:
            print(cells[0].text + ": ", cells[1].text)
    
    driver.quit()
    
scrap()