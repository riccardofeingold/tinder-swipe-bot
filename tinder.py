from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
from time import sleep
import os
from dotenv import load_dotenv

class TinderBot:
    def __init__(self):
        load_dotenv()
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('prefs', {
            'geolocation': True,
            'profile.default_content_setting_values.notifications': 2
        })
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        # Change chrome driver path accordingly
        self.chrome_driver_path = os.environ.get("chrome-driver-path")
        self.driver = webdriver.Chrome(self.chrome_driver_path, chrome_options=self.chrome_options, options=self.options)

        self.base_window = self.driver.window_handles[0]

    def login(self):
        self.driver.get('https://tinder.com')

    def login_with_gmail(self, username, pwd):
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div['
                                                       '1]/div/button')
        login_btn.click()
        gmail_login_window = self.driver.window_handles[1]
        self.driver.switch_to(gmail_login_window)

    def auto_swipe(self):
        while True:
            sleep(random.randint(2, 5))
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_superstar()
                    except Exception:
                        try:
                            self.close_match()
                        except Exception:
                            sleep(5)

    def like(self):
        try:
            like_button = self.driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span')
        except Exception:
            like_button = self.driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button/span/span')
        like_button.click()

    def dislike(self):
        try:
            dislike_button = self.driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button/span/span')
        except Exception:
            dislike_button = self.driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button/span/span')

        dislike_button.click()

    def close_popup(self):
        popup_1 = self.driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div[2]/button[2]')
        popup_1.click()

    def close_superstar(self):
        star_popup = self.driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/button[2]')
        star_popup.click()

    def close_match(self):
        match_popup = self.driver.find_element(By.XPATH, '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = TinderBot()
bot.auto_swipe()