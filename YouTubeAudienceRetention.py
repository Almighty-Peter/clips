

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re
import time



from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def getYoutubeAudienceRetention(videoId, plot=False, show=False):

    # Setup Chrome options
    chrome_options = Options()
    if show == False:
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
    result= False
    
    try:
        url = f"https://www.youtube.com/watch?v={videoId}"
    
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
        
    
        def find_element(driver, start_index, end_index, timeout=30, div=2):
            end_time = time.time() + timeout
            while time.time() < end_time:
                for i in range(start_index, end_index + 1):

                    xpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[{}]/div[1]/div[1]/div[2]'.format(i) #[2]-->[{div}]
                    try:    
                        try:     
                            WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[{}]/div[1]/div[1]/div[3]'.format(i))))
                        except:
                            pass
                        else:
                            return None
                            """here should triger the code to run many time and change div"""
                        element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, xpath)))
                        print(xpath)
                        return element
                    except:
                        continue

            return None
        
        # Base XPath with a placeholder for the index
        """IMPORTANT for videos with many parts, it takes only the first, in theory this is solvable by looking the difrence between each and then assign them to parts based on theire length, but this is for future me to do
        or maybe even just add them"""
    
        
        # Attempt to find the element
        element = find_element(driver, 20, 50)
    
        # Get the outer HTML of the element
        element_html = element.get_attribute('outerHTML')
    
        # Use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(element_html, 'html.parser')
    
    
    
        pattern = re.compile(r'd="M ([^"]+)"')
        # Search for the pattern in the HTML content
        match = pattern.search(str(soup))
        
        
        data = match.group(1)
        elements = [pair for pair in data.split() if pair != 'C']
        
        # Initialize the resulting list
        result = []
        
        # Process each element
        for element in elements:
            # Split by comma and convert to float
            x, y = map(float, element.split(','))
            # Append the pair to the result list
            result.append([x, y])
       
        if plot:
            x_values = [pair[0] for pair in result]
            y_values = [pair[1] for pair in result]
            
            # Plot the data
            plt.figure(figsize=(10, 6))
            plt.plot(x_values, y_values, marker='o', linestyle='-')
            plt.title(f'YT={videoId}')
            plt.xlabel('X Values')
            plt.ylabel('Y Values')
            plt.grid(True)
            plt.show()
    
        
    
    
    finally:
        
        if show == 0:  
            driver.quit()
            
    return result

videoId = "f-WdfjE7X8g"

