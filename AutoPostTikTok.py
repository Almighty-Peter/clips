
""" click where to uplod file
//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div[3]/button[1]/div/div
//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div/div/div[1]

click where to add description
//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div

post button
//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[2]/div[8]/button[1]/div/div """


#
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

from pynput import keyboard

from time import sleep
import re

import json
import pyautogui

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




class TikTokUpload:
    URLLogin = 'https://www.tiktok.com/login/phone-or-email/email'
    URLUpload = 'https://www.tiktok.com/upload/?lang=en'


    def __init__(self, selenium= False):
        
        if selenium:
            self.driver = self.__open_browser()
            self.uploadSelenium()

    def uploadSelenium(self):
        userName = 'say_whattt1'
        password = 'hQH7Panh$3'
        self.driver.get(self.URLLogin)
        
        
        # Enter Username
        WebDriverWait(self.driver, 1000).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[1]/input'))
        )
        ActionChains(self.driver) \
            .send_keys_to_element(self.driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[1]/input'), userName) \
            .send_keys(Keys.ENTER).pause(3).perform()
        
        # Enter Password
        WebDriverWait(self.driver, 1000).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div/input'))
        )
        ActionChains(self.driver) \
            .send_keys_to_element(self.driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div/input'), password) \
            .send_keys(Keys.ENTER).pause(3).perform()
        
        sleep(1000)
        
        while False:
            # TODO: do it so that it can use selenium, but i found some problems
            pass


    @staticmethod
    def __open_browser():
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
    @staticmethod
    def on_press(key):
        if key == keyboard.Key.enter:
            return False  # Stop the listener

    def wait_for_enter(self):
        print("Waiting for Enter key...")
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
    
    @staticmethod
    def text_until_first_hashtag(text):
        match = re.search(r'#\w+', text)
        if match:
            return text[:match.start()]
        else:
            return text
        
    @staticmethod
    def extract_hashtags(text):
        hashtags = re.findall(r'#\w+', text)
        return hashtags

    def type(self,text):
        pyautogui.write(self.text_until_first_hashtag(text))
        hashtags = self.extract_hashtags(text)
        for hashtag in hashtags:
            pyautogui.write(hashtag)  
            sleep(1.2)
            pyautogui.press('enter')  
            sleep(0.5) 



    def saveActions(self):
        actions = []

        # 1. Click on the file manager
        self.wait_for_enter()
        coordinates = pyautogui.position()
        actions.append({"action": "file manager", "coordinates": [coordinates.x,coordinates.y]})

        # 2. Drag and Drop
        self.wait_for_enter()
        start_pos = pyautogui.position()
        self.wait_for_enter()
        end_pos = pyautogui.position()
        actions.append({"action": "drag and drop", "start": [start_pos.x,start_pos.y], "end": [end_pos.x,end_pos.y]})

        # 3. Click on text
        self.wait_for_enter()
        coordinates = pyautogui.position()
        actions.append({"action": "text", "coordinates": [coordinates.x,coordinates.y]})


        # 7. Click on post
        self.wait_for_enter()
        coordinates = pyautogui.position()
        actions.append({"action": "post", "coordinates": [coordinates.x,coordinates.y]})


        # 8. Click upload another video
        self.wait_for_enter()
        coordinates = pyautogui.position()
        actions.append({"action": "upload another video", "coordinates": [coordinates.x,coordinates.y]})


        # Save actions to JSON
        with open('/Users/peternyman/Clips/actions.json', 'w') as f:
            json.dump(actions, f, indent=4)

    def execute_actions(self):
        with open('/Users/peternyman/Clips/actions.json', 'r') as file:
            actions = json.load(file)

        for action in actions:
            if action["action"] == "file manager":
                pyautogui.click(action["coordinates"])
                sleep(1)
            elif action["action"] == "drag and drop":
                pyautogui.moveTo(action["start"])
                pyautogui.dragTo(action["end"], duration=1, button='left') 
                sleep(3)
            elif action["action"] == "text":
                pyautogui.click(action["coordinates"])
                sleep(1)
                pyautogui.hotkey('command', 'a')  # Select all text (Windows), change 'ctrl' to 'command' for macOS
                text = "Salish checks Nidal's six pack😭💗 #fyp  #viralvideo #viral #fy #blowup #activies? #nalish #nalishforever"
                sleep(0.5)
                self.type(text)  # Typing the text
                sleep(0.5)
            elif action["action"] == "post":
                pyautogui.moveTo(action["coordinates"])
                sleep(0.5)
                pyautogui.scroll(-1000)  # Scroll down to the bottom
                sleep(0.5)
                pyautogui.click(action["coordinates"])
            elif action["action"] == "upload another video":
                sleep(3)
                pyautogui.click(action["coordinates"])
                sleep(1)
                pyautogui.scroll(1000)  # Scroll back up to the top


sa = TikTokUpload()
# sa.saveActions()


sleep(4)
sa.execute_actions()










