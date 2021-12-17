from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import random
from time import sleep
import os
from dotenv import load_dotenv
import pyperclip

load_dotenv()

username = os.environ.get("username")
pwd = os.environ.get("pwd")
pyperclip.copy(pwd)

chrome_driver_path = os.environ.get("chrome-driver-path")
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    'geolocation': True,
    'profile.default_content_setting_values.notifications': 2
})
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

driver.get("http://www.bumble.com")

sleep(4)
login_button = driver.find_element(By.XPATH, '//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
login_button.click()

sleep(4)
apple_login = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[1]/div')
apple_login.click()

base_window = driver.window_handles[0]
apple_login_window = driver.window_handles[1]
driver.switch_to.window(apple_login_window)

sleep(4)
username_input = driver.find_element(By.XPATH, '//*[@id="account_name_text_field"]')
username_input.send_keys(username)
sleep(1)
username_input.send_keys(Keys.ENTER)

sleep(4)
# pwd_input = driver.find_element(By.XPATH, '//*[@id="password_text_field"]')

input("Enter verification code")

sleep(4)

driver.switch_to.window(base_window)
sleep(2)

give_likes = True
xpath_of_like_btn = '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span'
while give_likes:
    for _ in range(25):
        sleep(random.randint(2, 23))
        try:
            like_button = driver.find_element(By.XPATH, xpath_of_like_btn)
            like_button.click()

        # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
        except NoSuchElementException:
            xpath_of_like_btn = input("Past XPATH of like button or you've reach the end")
            if xpath_of_like_btn == 'end':
                break
        except ElementClickInterceptedException:
            input("There's something preventing to press me the like button")

    decision = input("Do you want to continue?")
    if decision == "n":
        give_likes = False


driver.quit()
