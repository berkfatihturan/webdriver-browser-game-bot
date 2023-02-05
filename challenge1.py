from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# accest to website
chrome_driver_path = "D:\BFT\Project\Python\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

link = "https://www.python.org/"
driver.get(link)

event_dict = {}
event_locate = driver.find_elements(By.XPATH,
                                    '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')  # find the location
for i, list_item in enumerate(event_locate):
    event_dict[i] = {
        "time": list_item.find_element(By.CSS_SELECTOR, "time").get_attribute("datetime")[:10],
        "name": list_item.find_element(By.CSS_SELECTOR, "a").text,
    }

print(event_dict)

driver.close()
