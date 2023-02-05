from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\BFT\Project\Python\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

link = "https://www.amazon.com.tr/Crucial-CT8G4SFRA266-2666MHz-SODIMM-BELLEK/dp/B08C56KXQJ/ref=asc_df_B08C56KXQJ/?tag=trshpngglede-21&linkCode=df0&hvadid=510501085631&hvpos=&hvnetw=g&hvrand=16558171917978239057&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9056803&hvtargid=pla-935330937540&th=1"
driver.get(link)

price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)

search_bar = driver.find_element(By.NAME,"field-keywords")
print(search_bar.get_attribute("id"))

pruduct_name = driver.find_element(By.CSS_SELECTOR,"#title")
print(pruduct_name.text)

pruduct_name = driver.find_element(By.XPATH,'//*[@id="bylineInfo"]')
print(pruduct_name.text)

driver.quit()


#
#
#
#

def search_on_youtube(url=link, text="hello word"):
    driver.get(url)

    search_bar = driver.find_element(By.NAME, "search_query")
    search_bar.send_keys(text)
    search_bar.send_keys(Keys.ENTER)

    # search_button = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]')
    # search_button.click()
    # search_button.send_keys(Keys.ENTER)
    #
    # body = browser.find_element(By.CSS_SELECTOR,'body')
    # body.click()
    # body.send_keys(Keys.PAGE_DOWN)

#
#
#

# def list(url="https://orteil.dashnet.org/cookieclicker/"):
#     driver.get(url)
#     time.sleep(3)
#     driver.find_element(By.ID, "langSelect-EN").click()
#     time.sleep(3)
#
#     p = driver.find_element(By.XPATH, '//*[@id="products"]')
#     price_list = []
#     # for t in p.find_elements(By.CSS_SELECTOR, '[class^="product"]'):
#     #     price = t.find_element(By.CLASS_NAME, 'price').text
#     #     if price != "":
#     #         price_list.append(price)
#     #
#     for t in driver.find_elements(By.CLASS_NAME, 'price'):
#         if t.text != "":
#             price_list.append(t.text)
#
#     print(price_list)
# price_list = [int(price.text) for price in driver.find_elements(By.CLASS_NAME, 'price') if price.text != ""]

