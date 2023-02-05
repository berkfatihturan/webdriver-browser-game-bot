import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

chrome_driver_path = "D:\BFT\Project\Python\chromedriver.exe"
link = "https://orteil.dashnet.org/cookieclicker/"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

UPGRADE_CHOSEN_NUM = 52
PRODUCT_CHOSEN_NUM = 24
RAND_NUM_COUNT = 100
TIMER = 15


def get_products_price():
    price_list = []
    for price in driver.find_elements(By.CSS_SELECTOR, '[id*="productPrice"]'):
        if price.text != "":
            p = reformat(price.text)
            price_list.append(int(p))

    return price_list


def get_upgrade_list():
    upgrade_list = []
    update_box = driver.find_element(By.ID, 'upgrades')
    for i in update_box.find_elements(By.CSS_SELECTOR, '[class*="enabled"]'):
        upgrade_list.append(i)

    return upgrade_list


def is_ok() -> bool:
    time.sleep(5)
    try:
        driver.find_element(By.ID, "loader")
    except NoSuchElementException:
        return True
    else:
        return False


def reformat(text):
    text = text.replace(",", "").replace(".", "").replace(" million", "00000").replace(" billion", "000000")
    return text


def cookieClicker(url: str = link):
    driver.get(url)
    if not is_ok():
        cookieClicker()
        return 0

    driver.find_element(By.ID, "langSelect-EN").click()
    if not is_ok():
        cookieClicker()
        return 0

    end_time = time.time() + 60 * TIMER  # timer

    product_price_list = get_products_price()
    upgrade_List = get_upgrade_list()

    chosen_product = random.choice(product_price_list)

    while end_time > time.time():
        cookies = int(reformat(driver.find_element(By.ID, "cookies").text.split(" ")[0]))
        rnd_number = random.randint(1, RAND_NUM_COUNT)

        if rnd_number == UPGRADE_CHOSEN_NUM:  # random time upgrade
            if len(upgrade_List) != 0:
                try:
                    random.choice(upgrade_List).click()
                except StaleElementReferenceException:
                    print("Skip1")

            upgrade_List = get_upgrade_list()

        if cookies > chosen_product:  # cookies adequate to chosen product
            driver.find_element(By.XPATH, f'//*[@id="product{product_price_list.index(chosen_product)}"]').click()
            rnd_number = PRODUCT_CHOSEN_NUM  # send to if for select next rand value

        if rnd_number == PRODUCT_CHOSEN_NUM:  # select next random product
            try:
                product_price_list = get_products_price()
                chosen_product = random.choice(product_price_list)
                print(chosen_product)
            except NoSuchElementException:
                print("Skip2")

        driver.find_element(By.ID, "bigCookie").click()

    driver.close()


cookieClicker()
