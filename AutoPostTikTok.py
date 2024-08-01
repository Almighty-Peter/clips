# import time
# import random
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
# from webdriver_manager.chrome import ChromeDriverManager as CM

# print('=====================================================================================================')
# print('Heyy, you have to login manully on tiktok, so the bot will wait you 1 minute for loging in manually!')
# print('=====================================================================================================')
# time.sleep(8)
# print('Running bot now, get ready and login manually...')
# time.sleep(4)

# options = webdriver.ChromeOptions()
# bot = webdriver.Chrome(options=options,  executable_path=CM().install())
# bot.set_window_size(1680, 900)

# bot.get('https://www.tiktok.com/login')
# ActionChains(bot).key_down(Keys.CONTROL).send_keys(
#     '-').key_up(Keys.CONTROL).perform()
# ActionChains(bot).key_down(Keys.CONTROL).send_keys(
#     '-').key_up(Keys.CONTROL).perform()
# print('Waiting 50s for manual login...')
# time.sleep(50)
# bot.get('https://www.tiktok.com/upload/?lang=en')
# time.sleep(3)


# def check_exists_by_xpath(driver, xpath):
#     try:
#         driver.find_element_by_xpath(xpath)
#     except NoSuchElementException:
#         return False

#     return True


# def upload(video_path):
#     while True:
#         file_uploader = bot.find_element_by_xpath(
#             '//*[@id="main"]/div[2]/div/div[2]/div[2]/div/div/input')

#         file_uploader.send_keys(video_path)

#         caption = bot.find_element_by_xpath(
#             '//*[@id="main"]/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/span')

#         bot.implicitly_wait(10)
#         ActionChains(bot).move_to_element(caption).click(
#             caption).perform()
#         # ActionChains(bot).key_down(Keys.CONTROL).send_keys(
#         #     'v').key_up(Keys.CONTROL).perform()

#         with open(r"caption.txt", "r") as f:
#             tags = [line.strip() for line in f]

#         for tag in tags:
#             ActionChains(bot).send_keys(tag).perform()
#             time.sleep(2)
#             ActionChains(bot).send_keys(Keys.RETURN).perform()
#             time.sleep(1)

#         time.sleep(5)
#         bot.execute_script("window.scrollTo(150, 300);")
#         time.sleep(5)

#         post = WebDriverWait(bot, 100).until(
#             EC.visibility_of_element_located(
#                 (By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]/div[5]/button[2]')))

#         post.click()
#         time.sleep(30)

#         if check_exists_by_xpath(bot, '//*[@id="portal-container"]/div/div/div[1]/div[2]'):
#             reupload = WebDriverWait(bot, 100).until(EC.visibility_of_element_located(
#                 (By.XPATH, '//*[@id="portal-container"]/div/div/div[1]/div[2]')))

#             reupload.click()
#         else:
#             print('Unknown error cooldown')
#             while True:
#                 time.sleep(600)
#                 post.click()
#                 time.sleep(15)
#                 if check_exists_by_xpath(bot, '//*[@id="portal-container"]/div/div/div[1]/div[2]'):
#                     break

#         if check_exists_by_xpath(bot, '//*[@id="portal-container"]/div/div/div[1]/div[2]'):
#             reupload = WebDriverWait(bot, 100).until(EC.visibility_of_element_located(
#                 (By.XPATH, '//*[@id="portal-container"]/div/div/div[1]/div[2]')))
#             reupload.click()

#         time.sleep(1)


# # ================================================================
# # Here is the path of the video that you want to upload in tiktok.
# # Plese edit the path because this is different to everyone.
# upload(r"C:\Users\redi\Videos\your-video-here.mov")
# # ================================================================

"""
Script for generating outlook.com account with randomly generated data
Built with: Selenium, 2Captcha and Faker package
"""

# import os
import random
import secrets
from pynput import keyboard
# import shutil
import string
# import zipfile
from time import sleep
# from pprint import pprint
# from uuid import uuid4
from random import choice
import calendar
import sqlite3
from datetime import datetime


# import requests
from faker import Faker
# from captcha_solver import CaptchaSolver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




# 2Captcha API key here
from proxy_auth import manifest_json, background_js, plugin_file
import pygame


class OutlookAccountCreator:
    """ Class for creating outlook.com account
    with randomly generated details"""
    URLLogin = 'https://www.tiktok.com/login'
    URLUpload = 'https://www.tiktok.com/upload/?lang=en'


    def __init__(self):
        self.driver = self.__open_browser()

    def create_account(self):
        self.driver.get(self.URLLogin)
        sleep(40)
        while False:
            self.driver.get(self.URLUpload)


            WebDriverWait(self.driver, 1000).until(
                EC.element_to_be_clickable((By.ID, 'liveSwitch'))
            )
            self.driver.find_element(By.ID, 'liveSwitch').click()
            print("liveSwitch")

            person = self.__generate_random_details()
            birth_date = person['dob']

            # Enter Email
            WebDriverWait(self.driver, 1000).until(
                EC.element_to_be_clickable((By.ID, 'usernameInput'))
            )
            ActionChains(self.driver) \
                .send_keys_to_element(self.driver.find_element(By.ID, 'usernameInput'), person['username']) \
                .send_keys(Keys.ENTER).pause(3).perform()
            print("usernameInput")
            # Enter Password
            WebDriverWait(self.driver, 1000).until(
                EC.element_to_be_clickable((By.ID, 'Password'))
            )
            ActionChains(self.driver) \
                .send_keys_to_element(self.driver.find_element(By.ID, 'Password'), person['password']) \
                .send_keys(Keys.ENTER).pause(3).perform()
            print("Password")
            # Enter First and Last Name
            WebDriverWait(self.driver, 1000).until(
                EC.element_to_be_clickable((By.ID, 'firstNameInput'))
            )
            WebDriverWait(self.driver, 1000).until(
                EC.element_to_be_clickable((By.ID, 'lastNameInput'))
            )
            ActionChains(self.driver) \
                .send_keys_to_element(self.driver.find_element(By.ID, 'firstNameInput'), person['first_name']) \
                .send_keys_to_element(self.driver.find_element(By.ID, 'lastNameInput'), person['last_name']) \
                .send_keys(Keys.ENTER).pause(3).perform()
            print("firstNameInput")
            print("lastNameInput")
            
            # Enter Country and DOB
            country_option_xpath = f'//option[@value="{person["country"]}"]'
            WebDriverWait(self.driver, 1000).until(
                EC.element_to_be_clickable((By.XPATH, country_option_xpath))
            ).click()
            print(f'country_option')

                    # Enter Email
            WebDriverWait(self.driver, 1000).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="BirthYear"]'))
            )
            ActionChains(self.driver) \
                .send_keys_to_element(self.driver.find_element(By.XPATH, '//*[@id="BirthYear"]'), birth_date.year).perform()
            print(f'BirthYear')

            # Select the birth day
            day_select = WebDriverWait(self.driver, 10000).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="BirthDay"]'))
            )
            
            ActionChains(self.driver) \
                .send_keys_to_element(self.driver.find_element(By.XPATH, '//*[@id="BirthDay"]'), birth_date.day).perform()
            print("BirthDay")
            # Select the birth month
            month_select = WebDriverWait(self.driver, 10000).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="BirthMonth"]'))
            )
            
            ActionChains(self.driver) \
                .send_keys_to_element(self.driver.find_element(By.XPATH, '//*[@id="BirthMonth"]'), calendar.month_name[birth_date.month]).perform()
            print("BirthMonth")
            # Click the signup button
            signup_button = WebDriverWait(self.driver, 1000).until(
                EC.element_to_be_clickable((By.ID, 'nextButton'))
            )
            signup_button.click()


            

            
            




            # Prepare the data
            email = person['username'] + '@outlook.com'
            password = person['password']
            firstName = person['first_name']
            lastName = person['last_name']
            dob = person['dob'].strftime('%d, %b %Y')
            country = person['country']

            # Insert the data into the database
            conn = sqlite3.connect('/Users/peternyman/Clips/outlook.db')
            cursor = conn.cursor()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                dob TEXT NOT NULL,
                country TEXT NOT NULL
            )
            ''')

            cursor.execute('''
            INSERT INTO people (email, password, first_name, last_name, dob, country)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (email, password, firstName, lastName, dob, country))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()

            print("--------------------------------------------------------")
            print(email)
            print(password)
            print(dob)



    

    @staticmethod
    def __open_browser():
        # TODO: add user agent
        #chrome_options = webdriver.ChromeOptions()
        
        chrome_options = Options()
        #chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        


account_creator = OutlookAccountCreator()

account_creator.create_account()


