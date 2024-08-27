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
from time import sleep

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




def __generate_random_details():
    """
    Generates random details for new account
    :return: dictionary with fake details
    """
    fake_details = Faker()
    name = fake_details.name()
    username = __create_username(name)
    password = __generate_password()
    first, last = name.split(' ', 1)

    while True:
        dob = fake_details.date_time()
        if dob.year < 2000:
            break


    country = random.choice(["US","EN","SW","CH"])

    return {
        "first_name": first,
        'last_name': last,
        'country': country,
        'username': username,
        'password': password,
        'dob': dob
    }


def __create_username(name: str):
    """
    Creates username based on name
    :param name: string with person name
    :return: string with username based on the name
    """
    return name.replace(' ', '').lower() + str(random.randint(1000, 10000))


def __generate_password():
    """
    generates password 10 char long, with at least one number and symbol
    :return: string with new password
    """
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(11))
    return password + random.choice('$#@!%^') + random.choice('0123456789')



person = __generate_random_details()
email = person['username'] 
password = person['password']
firstName = person['first_name']
lastName = person['last_name']
dob = person['dob'].strftime('%d, %b %Y')
country = person['country']


print(f"firstName: {firstName}")
print(f"lastName:  {lastName}")
print(f"")
print(f"email:     {email}@outlook.com")
print(f"password:  {password}")
print(f"")
print(f"dob:       {dob}")
print(f"country:   {country}")
