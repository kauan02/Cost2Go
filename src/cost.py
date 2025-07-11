import time
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def scrap():
    local = input("Tap the city (ex: Toledo, Spain): ")
    today_data = datetime.today().strftime("%Y-%m-%d")
    driver = webdriver.Firefox()
    driver.get("https://www.numbeo.com/cost-of-living/")
    search_bar = driver.find_element(By.ID, "city_selector_city_id")
    search_bar.send_keys(local)
    time.sleep(1)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(3)

    try:
        table = driver.find_element(By.CLASS_NAME, "data_wide_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        city_data = []

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 2:
                name = cells[0].text
                price = cells[1].text
                city_data.append({
                    "item": name,
                    "price": price
                })

        try:
            with open("city_data.json", "r", encoding="utf-8") as f:
                all_city = json.load(f)
        except FileNotFoundError:
            all_city = {}

        if local not in all_city:
            all_city[local] = {}

        all_city[local][today_data] = city_data

        with open("all_city.json", "w", encoding="utf-8") as f:
            json.dump(all_city, f, indent=2, ensure_ascii=False)

        print(f"Data saved to {local} at {today_data} succesfully!")

    except Exception as e:
        print("Error to extract the table:", e)

    finally:
        driver.quit()

scrap()
