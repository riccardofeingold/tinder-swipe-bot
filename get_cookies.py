from selenium import webdriver
from cookies import save_cookie
import os
from dotenv import load_dotenv

load_dotenv()

chrome_driver_path = os.environ.get("chrome-driver-path")
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://tinder.com')

foo = input()

save_cookie(driver, '')