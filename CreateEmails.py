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
# from time import sleep
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

def play_sound(file_path):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    pygame.mixer.music.load(file_path)

    # Play the sound
    pygame.mixer.music.play()

    # Keep the program running until the sound finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(5)

def on_press(key):
    if key == keyboard.Key.enter:
        return False  # Stop the listener

def wait_for_enter():
    print("Waiting for Enter key...")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


# API_2_CAPTCHA = '6ed35827f9a7e40e1c1acb767f8aa5e3'


# class Proxies:
#     proxy_list = []

#     @staticmethod
#     def load_proxies(file_path: str):
#         """
#         Reads a text file with proxies
#         :param file_path: Path to proxy file with proxies in <user>:<pas>@<ip>:<port> format each on one line
#         """
#         lst = []
#         if file_path:
#             if os.path.exists(file_path):
#                 with open(file_path, 'r') as file:
#                     lst = [x for x in file.read().split('\n') if x.strip()]
#             else:
#                 print('File: {}. Does not exist.'.format(file_path))
#         Proxies.proxy_list = lst

    # @staticmethod
    # def get_random_proxy():
    #     """ Returns a random proxy """
    #     return choice(Proxies.proxy_list)


class OutlookAccountCreator:
    """ Class for creating outlook.com account
    with randomly generated details"""
    URL = 'https://signup.live.com/signup'

    def __init__(self):
        self.driver = self.__open_browser()

    def create_account(self):
        while True:
            """
            Goes through website process of creating the account
            :return: dictionary with login information for the account
            """
            print('Creating new Outlook email account')
            self.driver.get(self.URL)

            """ WebDriverWait(self.driver, 1000).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'disc-border'))
            )
            self.driver.find_element(By.CLASS_NAME, 'disc-border').click()

            
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'actionButton'))
            )
            self.driver.find_element(By.ID, 'actionButton').click() """


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


            play_sound('/Users/peternyman/Clips/3wd9RcZ2fHc.mp3')
        
            """ 
                    # Solve Captcha
                    try:
                        captcha_form = self.driver.find_element(By.ID, 'HipPaneForm')
                    except:
                        # Retry if something went wrong
                        print('Failed while creating account...\nRetrying...')
                        return self.create_account()

                    # if 'Phone number' in captcha_form.get_attribute('innerHTML'):
                    #     print('Form asks for phone number...\nTerminating...')
                    #     self.driver.quit()
                    #     exit()

                    captcha_image_url = captcha_form \
                        .find_element_by_tag_name('img').get_attribute('src')
                    solution = self.__solve_captcha(captcha_image_url).replace(' ', '')
                    self.driver.find_element_by_xpath('//input[@aria-label="Enter the characters you see"]') \
                        .send_keys(solution)
                    self.driver.find_element(By.ID, 'iSignupAction').click()
            
            
            """

            
            




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


            wait_for_enter()
        


    @staticmethod
    def __generate_random_details():
        """
        Generates random details for new account
        :return: dictionary with fake details
        """
        fake_details = Faker()
        name = fake_details.name()
        username = OutlookAccountCreator.__create_username(name)
        password = OutlookAccountCreator.__generate_password()
        first, last = name.split(' ', 1)

        while True:
            dob = fake_details.date_time()
            if dob.year < 2000:
                break
            if dob.month != 2:
                break
        while True:
            country = fake_details.country_code(representation="alpha-2")
            if country != "GB":
                break
        return {
            "first_name": first,
            'last_name': last,
            'country': country,
            'username': username,
            'password': password,
            'dob': dob
        }

    @staticmethod
    def __create_username(name: str):
        """
        Creates username based on name
        :param name: string with person name
        :return: string with username based on the name
        """
        return name.replace(' ', '').lower() + str(random.randint(1000, 10000))

    @staticmethod
    def __generate_password():
        """
        generates password 10 char long, with at least one number and symbol
        :return: string with new password
        """
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        return password + random.choice('$#@!%^') + random.choice('0123456789')

    # @staticmethod
    # def __solve_captcha(captcha_url: str):
    #     """
    #     downloads captcha image and send to 2captcha to solve
    #     :param captcha_url: Captcha image url
    #     :return: string with captcha solution
    #     """
    #     img_name = f'{uuid4()}.jpg'
    #     if OutlookAccountCreator.__download_image(captcha_url, img_name):
    #         print('Solving Captcha...')
    #         solver = CaptchaSolver('2captcha', api_key=API_2_CAPTCHA)
    #         raw_data = open(img_name, 'rb').read()
    #         solution = solver.solve_captcha(raw_data)
    #         os.remove(img_name)
    #         print(f"Captcha solved (solution: {solution})...")
    #         return solution
    #     print('Failed to download captcha image...')

    # @staticmethod
    # def __download_image(image_url: str, image_name: str):
    #     """
    #     Downloads captcha image
    #     :param image_url: string with url to image
    #     :param image_name: string with image name
    #     :return: boolean, True if successful False is failed
    #     """
    #     print('Downloading Captcha image...')
    #     r = requests.get(image_url, stream=True)
    #     if r.status_code == 200:
    #         with open(image_name, 'wb') as f:
    #             r.raw.decode_content = True
    #             shutil.copyfileobj(r.raw, f)
    #             return True
    #     print('Captcha image download failed', image_url)
    #     return False

    @staticmethod
    def __open_browser():
        # TODO: add user agent
        #chrome_options = webdriver.ChromeOptions()
        
        chrome_options = Options()
        #chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")


        # Initialize the Chrome driver
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        #return webdriver.Chrome(chrome_options=chrome_options)


if __name__ == '__main__':
    # Initialize account creator class
    account_creator = OutlookAccountCreator()
    # Run account creator
    account_creator.create_account()
