from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()

tel = os.environ.get("tel")

chrome_driver_path = os.environ.get("chrome-driver-path")
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    'geolocation': True,
    'profile.default_content_setting_values.notifications': 2
})
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

driver.get("http://www.tinder.com")

sleep(4)
login_button = driver.find_element(By.XPATH, '//*[@id="c1276625974"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

sleep(4)
tel_login = driver.find_element(By.XPATH, '//*[@id="c1497966410"]/div/div/div[1]/div/div[3]/span/div[3]/button')
tel_login.click()

sleep(8)
tel_input = driver.find_element(By.XPATH, '//*[@id="c1497966410"]/div/div/div[1]/div[2]/div/input')
tel_input.send_keys(tel)
tel_input.send_keys(Keys.ENTER)

input("hit enter if you are ready!")

sleep(10)
accept_cookies = driver.find_element(By.XPATH, '//*[@id="c1276625974"]/div/div[2]/div/div/div[1]/button')
accept_cookies.click()
sleep(2)

for _ in range(10000):
    sleep(2)
    try:
        like_button = driver.find_element(By.XPATH,
            '//*[@id="c1276625974"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.XPATH, ".itsAMatch a")
            match_popup.click()

            #super_like_popup = driver.find_element(By.XPATH, '//*[@id="c1497966410"]/div/div/button[2]')
            #super_like_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(3)


driver.quit()
