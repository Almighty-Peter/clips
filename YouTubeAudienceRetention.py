

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re
import time
from pytube import YouTube
import sqlite3
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


connection = sqlite3.connect('local_database.db')
cursor = connection.cursor()

def match_extract(patern, response):
    videos = []
    matches_video = re.findall(patern, response)
    for video in matches_video:
        if (video in videos):
            pass
        else:
            videos.append(video)
    return videos

def video_exists(video_id):
    cursor.execute("SELECT 1 FROM YTVideos WHERE video_id = ?", (video_id,))
    return cursor.fetchone() is not None

def find_element(driver, start_index, end_index, div, timeout=20):
    end_time = time.time() + timeout
    foundMore = False
    while time.time() < end_time:
        for i in range(start_index, end_index + 1):
            xpath = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[{i}]/div[1]/div[1]/div[{div}]'
            try:    
                try:     
                    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[{i}]/div[1]/div[1]/div[{div+1}]')))
                except:
                    pass
                else:
                    foundMore = True
                element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, xpath)))
                print("Found Data")
                return element, foundMore
            except:
                continue

    return None

def getYoutubeAudienceRetention(videoId, plot=False, show=False):

    # Setup Chrome options
    chrome_options = Options()
    if show == False:
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")


    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
    
    try:
        url = f"https://www.youtube.com/watch?v={videoId}"

        
        div = 2
        totalData = []

        found = False
        foundMore = True
        attempt = 0
        allowedAttempts = 5
        while found == False and attempt < allowedAttempts:
            # Open the YouTube link
            driver.get(url)
        
            # Use the provided XPath to locate the element and modify it
            xpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div'
        
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            # Modify the element using JavaScript
            new_class_value = 'html5-video-player ytp-transparent ytp-exp-bottom-control-flexbox ytp-modern-caption ytp-exp-ppp-update ytp-bigboards ytp-hide-info-bar ytp-fine-scrubbing-exp ytp-fit-cover-video ytp-autonav-endscreen-cancelled-state ytp-heat-map-v2 ytp-heat-map ytp-iv-drawer-enabled ytp-branding-shown ad-created paused-mode ytp-progress-bar-hover'
            driver.execute_script("arguments[0].setAttribute('class', arguments[1]);", element, new_class_value)
            print("Element modified successfully.")
            


            try:
                element, foundMore = find_element(driver, 20, 50, div)
            except:
                print(f"data not Extracted. (TRYING AGAIN Attempt:{attempt}/{allowedAttempts})")
            else:


                element_html = element.get_attribute('outerHTML')

                soup = BeautifulSoup(element_html, 'html.parser')

                pattern = re.compile(r'd="M ([^"]+)"')

                match = pattern.search(str(soup))


                
                attempt += 1
                if match:
                    data = match.group(1)
                    totalData.append(data)
                    if foundMore:
                        
                        print(div)
                        print("foundMore")
                        attempt = 0
                        div = div+1
                    else:
                        found = True
                else:
                    print(f"data not Extracted. (TRYING AGAIN Attempt:{attempt}/{allowedAttempts})")
                    print(element)

        totalResult = []


        for data in totalData:
            print(len(data))
            elements = [pair for pair in data.split() if pair != 'C']
            
            result = []
            
            # Process each element
            for element in elements:
                # Split by comma and convert to float
                nill, y = map(float, element.split(','))
                # Append the pair to the result list
                result.append(y)

            totalResult.extend(result)

        if plot:
            yt = YouTube(f'https://www.youtube.com/watch?v={videoId}')
            length = yt.length  
            x_values = [(length * ((i+1)/len(totalResult))) for i in range(len(totalResult))]
            y_values = [pair for pair in totalResult]
            

            # Plot the data
            plt.figure(figsize=(10, 6))
            plt.plot(x_values, y_values, marker='o', linestyle='-')
            plt.title(f'YT={videoId}')
            plt.xlabel('X Values')
            plt.ylabel('Y Values')
            plt.grid(True)
            plt.savefig("plot.png")

            plt.close()
        

    
        
    
    
    finally:

        element = driver.find_element(By.XPATH, '//*[@id="text"]/a')
        href_value = element.get_attribute('href')
        page_source = driver.page_source
        yt_codes = match_extract(r'watch\?v=(.{11})', page_source)
        date = datetime.now().strftime('%Y-%m-%d')


        search_query = f"https://www.youtube.com/watch?v={videoId}"
        data = "NULL"

        for position_found,video_id in enumerate(yt_codes):
            if not video_exists(video_id):
                try:
                    yt = YouTube("https://www.youtube.com/watch?v="+video_id)
                    title = yt.title
                    channel = yt.author
                    views = yt.views

                    if views == None:
                        views = "NULL"

                    print(f"channel : {channel} \n\ntitle : {title}\n\n----------------------\n\n")
                    insert_query = """
                    INSERT INTO YTVideos (
                        video_id, channel, title, position_found, views, date, search_query, data
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """
                    cursor.execute(insert_query, (video_id, channel, title, position_found, views, date, search_query, data))
                    connection.commit()
                except:
                    pass
            else:
                print(f"Video ID {video_id} already exists in the database.")
            
        driver.quit()
            
    return href_value[25:], totalResult



