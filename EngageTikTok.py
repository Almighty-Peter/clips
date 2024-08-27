




import json

import numpy as np
import random





from pynput import keyboard

from time import sleep

import json
import pyautogui





class TikTokEngage:

    def rand(self,a,b):
        return random.random()+random.randint(a,b)

    def on_press(self, key):
        if key == keyboard.Key.enter:
            return False

    def wait_for_enter(self):
        print("Waiting for Enter key...")
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
        

    def type(self,text):
        pyautogui.write(text)  
        sleep(1.2)
        pyautogui.press('enter')  
        sleep(0.5) 



    def saveActions(self):
        actions = []


        print('1. Click on the down')
        self.wait_for_enter()
        coordinates = pyautogui.position()
        actions.append({"action": "down", "coordinates": [coordinates.x,coordinates.y]})


        print('2. Click on the upp')
        self.wait_for_enter()
        coordinates = pyautogui.position()
        actions.append({"action": "upp", "coordinates": [coordinates.x,coordinates.y]})


        print('3. Click on comment')
        self.wait_for_enter()
        coordinates = pyautogui.position()
        actions.append({"action": "comment", "coordinates": [coordinates.x,coordinates.y]})

        print('4. Click on the middel')
        self.wait_for_enter()
        coordinates = pyautogui.position()
        actions.append({"action": "middel", "coordinates": [coordinates.x,coordinates.y]})

        print('5. Click on follow')
        self.wait_for_enter()
        coordinates = pyautogui.position()
        actions.append({"action": "follow", "coordinates": [coordinates.x,coordinates.y]})


        # Save actions to JSON
        with open('/Users/peternyman/Clips/interacting.json', 'w') as f:
            json.dump(actions, f, indent=4)

    def execute_actions(self):
        with open('/Users/peternyman/Clips/interacting.json', 'r') as file:
            actions = json.load(file)

        for action in actions:


            if action["action"] == "down":
                pyautogui.moveTo(action["coordinates"])
                pyautogui.click(action["coordinates"])


            elif action["action"] == "upp":
                if random.random() > 0.95:
                    pyautogui.moveTo(action["coordinates"])
                    pyautogui.click(action["coordinates"])


            elif action["action"] == "comment":
                if random.random() > 0.5:
                    pyautogui.moveTo(action["coordinates"])
                    pyautogui.click(action["coordinates"])
                    sample_comments = [
                        "Great point!",
                        "I totally agree with you.",
                        "This is so true!",
                        "Couldn't have said it better myself.",
                        "Interesting perspective.",
                        "Thanks for sharing!",
                        "This is a great insight.",
                        "Love this!",
                        "Totally on point.",
                        "Well said!",
                        "This is exactly what I was thinking.",
                        "So true!",
                        "Absolutely agree.",
                        "This really resonated with me.",
                        "Great post!",
                        "I'm with you on this.",
                        "Couldn't agree more.",
                        "This is spot on!",
                        "This makes so much sense.",
                        "Very insightful.",
                    ]
                    self.type(random.choice(sample_comments))

            elif action["action"] == "middel":
                if random.random() > 0.2:
                    pyautogui.moveTo(action["coordinates"])
                    pyautogui.doubleClick(action["coordinates"])

            elif action["action"] == "follow":
                if random.random() > 0.8:
                    pyautogui.moveTo(action["coordinates"])
                    pyautogui.click(action["coordinates"])


            sleep(self.rand(0,7))
            pyautogui.moveTo(self.rand(0,1000))

sleep(3)
asd = TikTokEngage()
while True:
    asd.execute_actions()


