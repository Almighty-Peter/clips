

import time


import json
import numpy as np
from scipy.spatial.distance import pdist, squareform
import subprocess
import sqlite3
import pandas as pd

import csv
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import numpy as np
import random
import array
from collections import defaultdict
import os
import subprocess
import string




from pynput import keyboard

from time import sleep
import re
import pyperclip
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


    def __init__(self, userName="Null",getWeb=False):
        if getWeb:
            self.userName = userName
            self.driver = self.__open_browser()
            self.driver.get(f'https://www.tiktok.com/@{userName}')
        

    def findLastVideo(self, caption, retries=3):
        caption = caption.replace("\n\n\n\n"," ").replace("\n\n\n"," ").replace("\n\n"," ").replace("\n"," ")[:140]
        lastVid_xpath = '//*[@id="main-content-others_homepage"]/div/div[2]/div[2]/div/div[1]/div[2]/div/a'
        
        for attempt in range(retries):
            self.driver.get(f'https://www.tiktok.com/@{self.userName}')
            sleep(20)
            try:

                lastVidElement = WebDriverWait(self.driver, 100).until(
                    EC.element_to_be_clickable((By.XPATH, lastVid_xpath))
                )


                videoTitle = lastVidElement.get_attribute("title")

                print(f'Title   :"{videoTitle[:140]}')
                print(f'Caption :"{caption}"')

                if videoTitle[:140] == caption:

                    return lastVidElement.get_attribute("href")
            except Exception as e:
                print(f"Attempt {attempt+1} failed: {e}")



        

        return None

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
        pyperclip.copy(self.text_until_first_hashtag(text))
        pyautogui.hotkey('command', 'v')
        hashtags = self.extract_hashtags(text)
        for hashtag in hashtags:
            pyautogui.write(hashtag)  
            sleep(1.2)
            pyautogui.press('enter')  
            sleep(0.5) 



    def saveActions(self):
        actions = []

        # 1. Click on the file manager
        print('1. Click on the file manager')
        self.wait_for_enter()
        coordinates = pyautogui.position()
        actions.append({"action": "file manager", "coordinates": [coordinates.x,coordinates.y]})

        # 2. Drag and Drop
        print('2. Drag and Drop')
        self.wait_for_enter()
        start_pos = pyautogui.position()
        self.wait_for_enter()
        end_pos = pyautogui.position()
        actions.append({"action": "drag and drop", "start": [start_pos.x,start_pos.y], "end": [end_pos.x,end_pos.y]})

        # 3. Click on text
        print('3. Click on text')
        self.wait_for_enter()
        coordinates = pyautogui.position()
        actions.append({"action": "text", "coordinates": [coordinates.x,coordinates.y]})


        # 7. Click on post
        print('7. Click on post')
        self.wait_for_enter()
        coordinates = pyautogui.position()
        actions.append({"action": "post", "coordinates": [coordinates.x,coordinates.y]})


        # 8. Click upload another video
        print('8. Click upload another video')
        self.wait_for_enter()
        coordinates = pyautogui.position()
        actions.append({"action": "upload another video", "coordinates": [coordinates.x,coordinates.y]})


        # Save actions to JSON
        with open('/Users/peternyman/Clips/actions.json', 'w') as f:
            json.dump(actions, f, indent=4)

    def execute_actions(self,cut):
        with open('/Users/peternyman/Clips/actions.json', 'r') as file:
            actions = json.load(file)

        for action in actions:

            if action["action"] == "file manager":
                pyautogui.click(action["coordinates"])
                sleep(1)
                pyautogui.hotkey('command', 'f')  # (Windows), change 'command' to 'ctrl'
                sleep(1)
                video = f'YT={cut['VSE'][0]}S={cut['VSE'][1]}E={cut['VSE'][2]}.mp4'
                pyperclip.copy(self.text_until_first_hashtag(video))
                pyautogui.hotkey('command', 'v')
                sleep(1)
            elif action["action"] == "drag and drop":
                pyautogui.moveTo(action["start"])

                pyautogui.dragTo(action["end"], duration=1, button='left') 
            elif action["action"] == "text":
                sleep(4)
                pyautogui.click(action["coordinates"])
                sleep(3)
                pyautogui.hotkey('command', 'a')  # (Windows), change 'command' to 'ctrl'
                sleep(1)
                self.type(cut['Caption'])  # Typing the text
                sleep(0.5)
            elif action["action"] == "post":
                pyautogui.moveTo(action["coordinates"])
                sleep(0.5)
                pyautogui.scroll(-1000)  # Scroll down to the bottom
                sleep(0.5)
                pyautogui.click(action["coordinates"])
            elif action["action"] == "upload another video":
                sleep(5)
                pyautogui.click(action["coordinates"])
                sleep(1)
                pyautogui.scroll(1000)  # Scroll back up to the top
        sleep(60)
        return self.findLastVideo(cut['Caption'])

# save = TikTokUpload()
# save.saveActions()





connection = sqlite3.connect('local_database.db')
cursor = connection.cursor()



def check_row_exists(video_id, start_time, end_time):
    
    # Update the query to check that 'link' is not NULL
    query = """
    SELECT EXISTS(
        SELECT 1 FROM TKcuts
        WHERE videoId = ? AND start_time = ? AND end_time = ? AND TKLink IS NOT "NULL"
    )
    """
    
    cursor.execute(query, (video_id, start_time, end_time))
    exists = cursor.fetchone()[0]

    return exists


cursor.execute("SELECT videoId, start_time, end_time, embedding, caption FROM TKcuts")
tkcuts_rows = cursor.fetchall()
tkCuts = []


for row in tkcuts_rows:
    embedding_blob = row[3]
    embedding_array = array.array('d') 
    embedding_array.frombytes(embedding_blob)
    embedding = embedding_array.tolist()
    tkCuts.append({
        'VSE': [row[0], row[1], row[2]], 
        'Embedding': embedding,
        'Caption': row[4]
    })

tkCuts = pd.DataFrame(tkCuts)
tkCuts.columns = ['VSE', 'Embedding', 'Caption']


channel = "GlowTimeWithGrace"
alias = "GlowTimeWithGrace"
tikTokUpload = TikTokUpload(userName=channel,getWeb=True)
input("continue:")
sleep(4)



tkChannels = []
cursor.execute("SELECT name, embedding FROM TkChannel")
tkchannels_rows = cursor.fetchall()

for row in tkchannels_rows:
    embedding_blob = row[1]
    embedding_array = array.array('d') 
    embedding_array.frombytes(embedding_blob)
    embedding = embedding_array.tolist()
    tkChannels.append({
        'Name': row[0], 
        'Embedding': embedding
    })

tkChannels = pd.DataFrame(tkChannels)
tkChannels.columns = ['Name', 'Embedding']

howMany = {name: 0 for name in tkChannels['Name']}  

for i, cut in tkCuts.iterrows():
    max_similarity = -1
    closest_channel = None  


    cut_embedding_reshaped = np.array(cut['Embedding']).reshape(1, -1)

    for j, channel in tkChannels.iterrows():
        channel_embedding_reshaped = np.array(channel['Embedding']).reshape(1, -1)
        similarity = cosine_similarity(cut_embedding_reshaped, channel_embedding_reshaped)[0][0]


        if similarity > max_similarity:
            max_similarity = similarity
            closest_channel = channel['Name'] 



    print(closest_channel)
    if closest_channel == alias:
        
        if check_row_exists(cut['VSE'][0], cut['VSE'][1], cut['VSE'][2]) == False:

            TKLink = tikTokUpload.execute_actions(cut)
            if TKLink != None:
                print(TKLink)
                sql = """
                UPDATE TKcuts
                SET TKLink = ?
                WHERE videoId = ? AND start_time = ? AND end_time = ?;
                """
                cursor.execute(sql, (TKLink, cut['VSE'][0], cut['VSE'][1], cut['VSE'][2]))
                connection.commit()
        else:
            print("already upploaded")

connection.close()
