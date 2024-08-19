
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.proxy import Proxy, ProxyType
# import sqlite3
from datetime import datetime
date = datetime.now().strftime('%Y-%m-%d')
# import requests
# from lxml import html



# connection = sqlite3.connect("local_database.db")
# cursor = connection.cursor()




# create_table_query = """
# CREATE TABLE IF NOT EXISTS channelYT (
#     channelID VARCHAR(100),
#     found VARCHAR(100),
#     otherLink VARCHAR(100),
#     country VARCHAR(100),
#     PRIMARY KEY(channelID)
# );
# """

# cursor.execute(create_table_query)
# connection.commit()


# create_table_query = """
# CREATE TABLE IF NOT EXISTS YTChannel (
#     channelID VARCHAR(100),
#     found VARCHAR(100),
#     otherLink VARCHAR(100),
#     country VARCHAR(100),
#     date CHAR(10),
#     followerChange VARCHAR(10),
#     PRIMARY KEY(channelID)
# );
# """

# cursor.execute(create_table_query)
# connection.commit()



# chrome_options = Options()
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# driver  = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
# # driverb = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)


# # def insert_channel(channelID, found, otherLink, country):
# #     check_query = "SELECT 1 FROM channelYT WHERE channelID = ?"
# #     cursor.execute(check_query, (channelID,))
    
# #     if cursor.fetchone() is None:
# #         insert_query = """
# #         INSERT INTO channelYT (channelID, found, otherLink, country)
# #         VALUES (?, ?, ?, ?)
# #         """
# #         cursor.execute(insert_query, (channelID, found, otherLink, country))
# #         connection.commit()
# #         print(f"Channel '{channelID}' added successfully.")
# #     else:
# #         print(f"Channel '{channelID}' already exists in the database.")


# # def getfromSocialBlade(found,howMany):
    
# #     driver.get(found)
# #     div = 11
# #     try:        
# #         xpath = f"/html/body/div[{div}]/div[2]/div[10]/div[3]/a"
        
# #         element = WebDriverWait(driver, 10).until(
# #         EC.presence_of_element_located((By.XPATH, xpath))
# #         )
# #         print(11)
# #     except:
# #         div = 12
# #         print(12)

# #     allLinks = []
# #     for i in range(5,howMany+5):
# #         xpath = f"/html/body/div[{div}]/div[2]/div[{i}]/div[3]/a"

# #         element = WebDriverWait(driver, 10).until(
# #         EC.presence_of_element_located((By.XPATH, xpath))
# #         )

# #         otherLink = element.get_attribute('href')
        
# #         check_query = "SELECT 1 FROM channelYT WHERE otherLink = ?"
# #         cursor.execute(check_query, (otherLink,))
        
# #         print(otherLink)
# #         if cursor.fetchone() is None:
            
# #             driverb.get(otherLink)
# #             try:
# #                 xpath_of_element = '//*[@id="YouTubeUserTopInfoBlockTop"]/div[1]/h4/a'
# #                 elementChannelID = WebDriverWait(driverb, 3).until(
# #                     EC.presence_of_element_located((By.XPATH, xpath_of_element))
# #                 )
# #             except: 
# #                 pass
# #             else:
# #                 try:
# #                     xpath_of_element = '//*[@id="youtube-user-page-country"]'
# #                     elementCountry = WebDriverWait(driverb, 3).until(
# #                         EC.presence_of_element_located((By.XPATH, xpath_of_element))
# #                     )
# #                 except: 
# #                     pass
# #                 else:
# #                     channelID = elementChannelID.get_attribute('href')
# #                     country = elementCountry.get_attribute('href')
# #                     insert_channel(channelID,found,otherLink,country)




# # howMany = 500
# # link = f"https://socialblade.com/youtube/top/trending/top-500-channels-30-day/most-subscribed"
# # getfromSocialBlade(link,howMany)
# # print(f"--------------------------------------------------------most-subscribed")

# # link = f"https://socialblade.com/youtube/top/trending/top-500-channels-30-days/most-viewed"
# # getfromSocialBlade(link,howMany)
# # print(f"--------------------------------------------------------most-viewed")
# # countrs = ["us", "ca", "gb"]
# # countrys = [ "au", "nz", "ie", "za", "jm", "tt", "bb", "bs", "bz", "gy", "zw", "gh", "ng", "ke", "bw", "sg"]
# # for country in countrys:
    
# #     howMany = 100
# #     link = f"https://socialblade.com/youtube/top/country/{country}"
# #     getfromSocialBlade(link,howMany)
# #     print(f"--------------------------------------------------------{country}")


# # categorys = ["autos", "comedy", "education", "entertainment", "film", "gaming", "howto", "made-for-kids", "music", "news", "nonprofit", "people", "animals", "tech", "shows", "sports", "travel"]
# # for category in categorys:  
# #     howMany = 100
# #     link = f"https://socialblade.com/youtube/top/category/{category}"
# #     getfromSocialBlade(link,howMany)
# #     print(f"--------------------------------------------------------{category}")




# # def ceck(id):
# #     try:
# #         response = requests.get(f'https://www.youtube.com/@{id}')
# #         response.raise_for_status()
# #         tree = html.fromstring(response.content)
# #         element = tree.xpath('//*[@id="error-page-content"]/p[1]')
# #         if element:
# #             return False
# #         else:
# #             return True
    
# #     except requests.exceptions.RequestException as e:
# #         print(e)
# #         return False





# # for j in range(1,6):
# #     driver.get(f"https://www.twitchmetrics.net/channels/growth?page={j}")
# #     if j == 1:
# #         div = 6
# #     else:
# #         div = 7
# #     for i in range(1,51):
# #         channel_element = WebDriverWait(driver, 20).until(
# #             EC.presence_of_element_located((By.XPATH, f"/html/body/div[{div}]/div[2]/div[1]/ul/li[{i}]/div/div[1]/div/div[2]/div[1]/div[2]/div[1]/a/h5"))
# #         )                                              
# #         channelID = channel_element.text
        
# #         if ceck(channelID):
# #             print(channelID)
# #             other_link = driver.find_element(By.XPATH, f"/html/body/div[{div}]/div[2]/div[1]/ul/li[{i}]/div/div[1]/div/div[2]/div[1]/div[2]/div[1]/a").get_attribute('href')
# #             country = driver.find_element(By.XPATH, f"/html/body/div[{div}]/div[2]/div[1]/ul/li[{i}]/div/div[1]/div/div[2]/div[1]/div[2]/div[3]/div[1]").text
# #             date = datetime.now().strftime('%Y-%m-%d')
# #             follower_change = driver.find_element(By.XPATH, f"/html/body/div[{div}]/div[2]/div[1]/ul/li[{i}]/div/div[2]/div/div[1]/div/samp").text
# #             found = f"https://www.twitchmetrics.net/channels/growth?page={j}"
# #             try:
# #                 insert_query = """
# #                 INSERT INTO YTChannel (channelID, found, otherLink, country, date, followerChange)
# #                 VALUES (?, ?, ?, ?, ?, ?)
# #                 """
# #                 cursor.execute(insert_query, (channelID, found, other_link, country, date, follower_change))
# #                 connection.commit()
# #             except:
# #                 print(channelID)
# #                 pass







# # cursor.execute("SELECT * FROM channelYT")
# # rows = cursor.fetchall()

# # for (channelID, found, otherLink, country) in rows:
# #     print()
# #     insert_query = """
# #     INSERT INTO YTChannel (channelID, found, otherLink, country, date, followerChange)
# #     VALUES (?, ?, ?, ?, ?, NULL)
# #     """

# #     cursor.execute(insert_query, (channelID[25:], found, otherLink, country[44:], date))
# #     connection.commit()

# # cursor.close()
# # connection.close()

                                             
# # driver.quit()
# # driverb.quit()


"""
whistlindiesel1000
whistlindiesel
nelkfilmz
joerogan
EnesYilmazer
"""
# ['MrBeast', '63%', '36%']
# 63% --> Fame
# 36% --> Popularity
# https://today.yougov.com/ratings/entertainment/popularity/influencers/all
# The most popular influencers (Q2 2024)
list = [['MrBeast', '63%', '36%'], ['Joanna Stevens Gaines', '51%', '32%'], ['Zach King', '41%', '29%'], ['Good Mythical Morning', '43%', '28%'], ['Ryan Higa', '42%', '28%'], ['Liz Eswein', '41%', '28%'], ['Lauren Conrad', '51%', '28%'], ['Andrew Tate', '60%', '28%'], ['Addison Rae', '47%', '27%'], ['Camila Coelho', '42%', '27%'], ['Casey Neistat', '44%', '27%'], ['Huda Kattan', '40%', '27%'], ['Uncle Roger', '42%', '26%'], ['Olivia Dunne', '43%', '26%'], ['Eddie Hall', '42%', '26%'], ['Dude Perfect', '45%', '26%'], ['Stacia Mar', '39%', '26%'], ['David Dobrik', '44%', '26%'], ['Andrew B. Bachelor', '40%', '26%'], ['Ludwig', '41%', '26%'], ['PewDiePie', '52%', '26%'], ['Jessica Vasquez', '39%', '26%'], ['Jenni Kayne', '39%', '26%'], ['Jake Paul', '62%', '26%'], ['Charli D’amelio', '46%', '26%'], ['Marie Kondo', '48%', '26%'], ['Swagg (Faze Swagg)', '40%', '26%'], ["Charli D'Amelio", '49%', '26%'], ['Emma Chamberlain', '41%', '26%'], ['MatPat', '38%', '26%'], ['Nikkie de Jager', '42%', '25%'], ['Ruben Gunderson', '37%', '25%'], ['Matt Stonie', '41%', '25%'], ['Logan Paul', '64%', '25%'], ['The Try Guys', '42%', '25%'], ['Pokimane', '46%', '25%'], ['Minimalist Baker', '39%', '25%'], ['Rebecca Zamolo', '41%', '25%'], ['Markiplier', '44%', '25%'], ['Matt King', '41%', '25%'], ['Ryan Trehan', '40%', '25%'], ['Michelle Phan', '38%', '25%'], ['Rosanna Pansino', '40%', '25%'], ['Jack Morris', '39%', '25%'], ['Troye Sivan', '44%', '25%'], ['Sam and Colby', '43%', '25%'], ['Juan Pablo “Juanpa” Zurita', '39%', '25%'], ['Khaby Lame', '38%', '25%'], ['Nick DiGiovanni', '41%', '25%'], ['Michelle Lewin', '37%', '25%'], ['Sammy Robinson', '36%', '24%'], ['Annette White', '41%', '24%'], ['NickEh30', '39%', '24%'], ['Mr Ballen', '36%', '24%'], ['Charlie McDonnell', '38%', '24%'], ['Hasanabi (Hasan Piker)', '44%', '24%'], ['Saffron Barker', '38%', '24%'], ['Jeffree Star', '49%', '24%'], ['Kayla Itsines', '38%', '24%'], ['Andrea Russet', '37%', '24%'], ['Joe Sugg', '36%', '24%'], ['Demi Bagby', '40%', '24%'], ['Lance Stewart', '38%', '24%'], ['The Points Guy', '36%', '24%'], ['Mark Rober', '38%', '24%'], ['Jay Alvarrez', '39%', '24%'], ['Adin Ross', '42%', '24%'], ['The Blonde Abroad', '38%', '24%'], ['Danny Gonzalez', '42%', '24%'], ['Ling Tang', '39%', '24%'], ['Elliot Tebele', '36%', '24%'], ['Alyssa Rose', '37%', '24%'], ['Shayla Mitchell', '38%', '23%'], ['Akin Akman', '35%', '23%'], ['Brooklyn and Bailey', '38%', '23%'], ['Nikkie De Jager', '39%', '23%'], ['Jack Johnson', '41%', '23%'], ['Liza Koshy', '41%', '23%'], ['Gregory DelliCarpini Jr', '37%', '23%'], ['tommyinnit', '37%', '23%'], ['Ian Hecox', '35%', '23%'], ['David Lopez', '39%', '23%'], ['Olajide William Olatunji (KSI)', '38%', '23%'], ['Thalia Ho', '35%', '23%'], ['Ingrid Nilsen', '39%', '23%'], ['Kandee Johnson', '36%', '23%'], ['Emma Hill', '35%', '23%'], ['Banks', '37%', '23%'], ['Dr. Mike Varshavski', '40%', '23%'], ['Alx James', '35%', '23%'], ['LilyPichu', '36%', '23%'], ['Madelynn Furlong', '39%', '23%'], ['Annemunition', '37%', '23%'], ['Talitha Girnus', '36%', '23%'], ['F2Freestylers', '38%', '23%'], ['Noah Beck', '43%', '23%'], ['James Charles', '46%', '23%'], ['Summer McKeen', '37%', '23%'], ['Kate McCulley', '37%', '23%'], ['Philip DeFranco', '43%', '23%'], ['Rickey Thompson', '37%', '23%'], ['Joshua Bradley - Zerkaa', '39%', '23%'], ['Roman Atwood', '39%', '23%'], ['Julie Sarinana', '37%', '23%'], ['Hannah Bronfman', '36%', '23%'], ['Meghan Rienks', '37%', '23%'], ['Molly Yeh', '37%', '23%'], ['Simply Nailogical', '38%', '23%'], ['Tara Milk Tea', '35%', '23%'], ['KingRichard', '40%', '23%'], ['Andrew Evans', '40%', '23%'], ['Elisabeth Akinwale', '37%', '23%'], ['Hannah Hart', '40%', '23%'], ['Louise Pentland', '37%', '23%'], ['Tanya Burr', '42%', '23%'], ['Ines de la Fressange', '35%', '23%'], ['Monsieur Dream', '35%', '23%'], ['Jay Caesar', '38%', '23%'], ['Ray William Johnson', '38%', '23%'], ['Sidemen', '36%', '23%'], ['Lele Pons', '39%', '23%'], ['Cole LaBrant', '38%', '23%'], ['Iskra Lawrence', '39%', '22%'], ['Tyler Oakley', '42%', '22%'], ['Gabrielle Alexis', '38%', '22%'], ['Kennedy Cymone', '35%', '22%'], ['Ida Frosk', '37%', '22%'], ['Jason Stein', '40%', '22%'], ['Luka Sabbat', '37%', '22%'], ['Simeon Panda', '33%', '22%'], ['Gloria Morales', '35%', '22%'], ['Andrea Russett', '35%', '22%'], ['Toby Turner', '38%', '22%'], ['Tarik', '39%', '22%'], ['Myth', '38%', '22%'], ['Danielle Bernstein', '38%', '22%'], ['Alinity', '40%', '22%'], ['Jerry Purpdrank', '33%', '22%'], ['Lily Maymac', '42%', '22%'], ['Mrs. Hinch', '36%', '22%'], ['Jack Douglass', '37%', '22%'], ['Justine Ezarik', '35%', '22%'], ['Ryan Trahan', '36%', '22%'], ['Valkyrae', '35%', '22%'], ['JasonTheWeen', '36%', '22%'], ['Pei Ketron', '36%', '22%'], ['Yogscast', '35%', '22%'], ['Joe Weller', '37%', '22%'], ['Kevin Fredericks', '34%', '22%'], ['Bugha', '36%', '22%'], ['Lilly Singh', '41%', '22%'], ['Larray', '38%', '22%'], ['Naomi Giannopoulos', '39%', '22%'], ['Emily Mariko', '38%', '22%'], ['Meg DeAngelis', '39%', '22%'], ['Samantha Ravndahl', '36%', '22%'], ['John Stephen Grice', '37%', '22%'], ['GloZell Lynette Simon', '37%', '22%'], ['Zoe Sugg (Zoella)', '37%', '22%'], ['IShowSpeed', '38%', '22%'], ['Nelk Boys', '38%', '22%'], ['Cooking with Mima', '36%', '22%'], ['Benjamin Lowy', '36%', '22%'], ['Brittany Furlan', '38%', '22%'], ['Adorian Deck', '35%', '22%'], ['Emily Skye', '37%', '22%'], ['Mark Angel Comedy', '33%', '22%'], ['Hind Deer', '35%', '22%'], ['Loren Gray', '38%', '22%'], ['Jen Selter', '37%', '22%'], ['Nicole Cogan', '35%', '22%'], ['Wayne Goss', '34%', '22%'], ['Dustin Giallanza', '35%', '22%'], ['Tana Mongeau', '40%', '22%'], ['Baddie Winkle', '36%', '22%'], ['Shroud', '36%', '22%'], ['Alfie Deyes (Pointless Blog)', '36%', '21%'], ['Hannah Stocking', '34%', '21%'], ['JiDion', '39%', '21%'], ['Vic Blends', '40%', '21%'], ['Natalie Myers', '39%', '21%'], ['Adam Dahlberg', '37%', '21%'], ['Murad Osmann', '35%', '21%'], ['Lauren Bullen', '35%', '21%'], ['Tyler "Ninja" Blevins', '38%', '21%'], ['CR Tan', '38%', '21%'], ['Mandi Gubler', '35%', '21%'], ['Marcus Butler', '35%', '21%'], ['Nailea Devora', '32%', '21%'], ['Isabella Thordsen', '37%', '21%'], ['Trainwreckstv', '37%', '21%'], ['NickMercs', '36%', '21%'], ['Valeria Lukyanova', '36%', '21%'], ['Jimmy Chin', '38%', '21%'], ['Chiara Ferragni', '37%', '21%'], ['Jenn Im', '34%', '21%'], ['Timthetatman', '40%', '21%'], ['Clix', '36%', '21%'], ['Bretman Rock', '37%', '21%'], ['Megan Gilmore', '35%', '21%'], ['Fozi Mozi', '34%', '21%'], ['Matthew Karsten', '35%', '21%'], ['Sommer Ray', '38%', '21%'], ['Carrington Durham', '34%', '21%'], ['Miranda Sings', '45%', '21%'], ['The Bucket List Family', '36%', '21%'], ['Gabriel Cabrera', '37%', '21%'], ['Laura Large', '35%', '21%'], ['Dennis the Prescott', '36%', '21%'], ['Edith W Young', '33%', '21%'], ['Kim Loaiza', '36%', '21%'], ['Lizzy Capri', '36%', '21%'], ['Dan Howell', '33%', '21%'], ['Alex Botez', '32%', '21%'], ['Cameron Dallas', '38%', '21%'], ['Evan Fong', '35%', '21%'], ['Jessie Chanes', '35%', '21%'], ['Tai Lopez', '34%', '21%'], ['Mikecrackq', '32%', '21%'], ['Summit1G', '35%', '21%'], ['Tom Cassell', '35%', '21%'], ['Rudy Mancuso', '34%', '21%'], ['Druski', '35%', '21%'], ['Negin Mirsalehi', '34%', '21%'], ['Chris Burkard', '34%', '21%'], ['Nash Grier', '37%', '21%'], ['Sykkuno', '34%', '21%'], ['Massy Arias', '38%', '21%'], ['Kaleb Anthony', '34%', '21%'], ['CalebCity', '37%', '21%'], ['Ling K Tang', '36%', '21%'], ['Lirik', '39%', '21%'], ['Manny Gutierrez', '39%', '21%'], ['Tfue', '35%', '21%'], ['Joe Wicks (The Body Coach)', '35%', '21%'], ['Will Taylor', '32%', '21%'], ['Julia Hengel', '35%', '20%'], ['Ashley Stark Kenner', '36%', '20%'], ["Dixie D'Amelio", '38%', '20%'], ['Russ Crandall', '36%', '20%'], ['Cassey Ho', '34%', '20%'], ['Matthew Espinosa', '40%', '20%'], ['Shaaanxo', '34%', '20%'], ['Fat Girls Traveling', '34%', '20%'], ['Grace Bonney', '33%', '20%'], ['Beta Squad', '34%', '20%'], ['Thomas Sanders', '41%', '20%'], ['KaiCenat', '38%', '20%'], ['Ty Haney', '38%', '20%'], ['Collins Key', '35%', '20%'], ['Ashrod', '36%', '20%'], ['Andrea Botez', '37%', '20%'], ['Aimee Song', '31%', '20%'], ['Eric Stoen', '36%', '20%'], ['Lil Tay', '41%', '20%'], ['Molly Tavoletti', '33%', '20%'], ['Oliver Proudlock', '33%', '20%'], ['DrDisRespect', '37%', '20%'], ['Brunch Boys', '33%', '20%'], ['Ironmouse', '36%', '20%'], ['Nina Williams', '34%', '20%'], ['Deji Olatunji', '35%', '20%'], ['QuarterJade', '34%', '20%'], ['iiTzTimmy', '33%', '20%'], ['Julia Sariñana', '34%', '20%'], ['Daniel Middleton', '34%', '20%'], ['Jim Chapman', '34%', '20%'], ['Craig Thompson - Mini Ladd', '34%', '20%'], ['Ela Vegan', '32%', '20%'], ['Amouranth', '34%', '20%'], ['StableRonaldo', '34%', '20%'], ['The Planet D', '34%', '20%'], ['Nicolette Mason', '36%', '20%'], ["L'atelier de Roxane", '35%', '20%'], ['Kemo Marriott', '34%', '20%'], ['Donjay', '35%', '20%'], ['QTCinderella', '37%', '20%'], ['Saudah Saleem', '36%', '20%'], ['DeStorm Power', '35%', '20%'], ['Joey Graceffa', '36%', '20%'], ['Shane Daweson', '43%', '20%'], ['Colin Furze', '32%', '20%'], ['Ilhan Eroglu', '34%', '20%'], ['Mariano Di Vaio', '35%', '20%'], ['Amymarie Gaertner', '33%', '20%'], ['Karl Jacobs', '38%', '20%'], ['Lacy', '35%', '19%'], ['Jack Harries', '37%', '19%'], ['Lindsey Silverman Love', '32%', '19%'], ['Casa Chicks', '33%', '19%'], ['Caspar Lee', '34%', '19%'], ['Rafi Fine', '33%', '19%'], ['David Chang', '36%', '19%'], ['Amanda Cerny', '33%', '19%'], ['Joana Ceddia', '31%', '19%'], ['Giovanna Engelbert', '33%', '19%'], ['Kordale Lewis', '34%', '19%'], ['Majawyh', '32%', '19%'], ['Lil Miquela', '35%', '19%'], ['Callum Leighton Airey', '36%', '19%'], ['Alexa Chung', '36%', '19%'], ['Arishfa Khan', '33%', '19%'], ['Safiya Nygaard', '33%', '19%'], ['Gabi Gregg', '36%', '19%'], ['YourRage', '35%', '19%'], ['Domelipa', '32%', '19%'], ['Ella Woodward (Deliciously Ella)', '32%', '19%'], ['Phil Lester', '35%', '19%'], ['Curtis Lepore', '34%', '19%'], ['Paul Nicklen', '36%', '19%'], ['Jeff Rose', '37%', '19%'], ['Brad Lau', '34%', '19%'], ['Michael Yamashita', '33%', '19%'], ['Galey Alix', '34%', '19%'], ['CC Clarke Beauty', '35%', '19%'], ['xQc', '37%', '19%'], ['Sydney Leroux Dwyer', '29%', '19%'], ['Whindersson Nunes', '34%', '18%'], ['ZooMaa', '32%', '18%'], ['Anwar Jibawi', '33%', '18%'], ['Brent Rivera', '37%', '18%'], ['Laura Noltemeyer', '33%', '18%'], ['Kelsey Calemine', '36%', '18%'], ['Studio McGee', '35%', '18%'], ['Garance Dore', '32%', '18%'], ['CourageJD', '31%', '18%'], ['TenZ', '30%', '18%'], ['Perrie Edwards', '33%', '18%'], ['Stacy Kranitz', '37%', '18%'], ['DrLupo', '37%', '18%'], ['Dakotaz', '35%', '18%'], ['Yumna Jawad', '32%', '18%'], ['Jannid Olsson Deler', '33%', '18%'], ['Joseph Garrett', '34%', '17%'], ['German Garmendia', '34%', '17%'], ['Gus Johnson', '31%', '17%'], ['Sjana Elise Earp', '30%', '17%'], ['Faze Rug', '33%', '17%'], ['Louis Cole', '35%', '16%'], ['Ajey Nagar', '30%', '16%'], ['Gueorgui Pinkhassov', '30%', '16%'], ['Ada Oguntodu', '31%', '16%']]

# test = """
# 1
# MrBeast
# MrBeast
# 63%
# 36%
# 2
# Joanna Stevens Gaines
# Joanna Stevens Gaines
# 51%
# 32%
# 3
# Zach King
# Zach King
# 41%
# 29%
# 4
# Good Mythical Morning
# Good Mythical Morning
# 43%
# 28%
# 5
# Ryan Higa
# Ryan Higa
# 42%
# 28%
# 6
# Liz Eswein
# Liz Eswein
# 41%
# 28%
# 7
# Lauren Conrad
# Lauren Conrad
# 51%
# 28%
# 8
# Andrew Tate
# Andrew Tate
# 60%
# 28%
# 9
# Addison Rae
# Addison Rae
# 47%
# 27%
# 10
# Camila Coelho
# Camila Coelho
# 42%
# 27%
# 11
# Casey Neistat
# Casey Neistat
# 44%
# 27%
# 12
# Huda Kattan
# Huda Kattan
# 40%
# 27%
# 13
# Uncle Roger
# Uncle Roger
# 42%
# 26%
# 14
# Olivia Dunne
# Olivia Dunne
# 43%
# 26%
# 15
# Eddie Hall
# Eddie Hall
# 42%
# 26%
# 16
# Dude Perfect
# Dude Perfect
# 45%
# 26%
# 17
# Stacia Mar
# Stacia Mar
# 39%
# 26%
# 18
# David Dobrik
# David Dobrik
# 44%
# 26%
# 19
# Andrew B. Bachelor
# Andrew B. Bachelor
# 40%
# 26%
# 20
# Ludwig
# Ludwig
# 41%
# 26%
# 21
# PewDiePie
# PewDiePie
# 52%
# 26%
# 22
# Jessica Vasquez
# Jessica Vasquez
# 39%
# 26%
# 23
# Jenni Kayne
# Jenni Kayne
# 39%
# 26%
# 24
# Jake Paul
# Jake Paul
# 62%
# 26%
# 25
# Charli D’amelio
# Charli D’amelio
# 46%
# 26%
# 26
# Marie Kondo
# Marie Kondo
# 48%
# 26%
# 27
# Swagg (Faze Swagg)
# Swagg (Faze Swagg)
# 40%
# 26%
# 28
# Charli D'Amelio
# Charli D'Amelio
# 49%
# 26%
# 29
# Emma Chamberlain
# Emma Chamberlain
# 41%
# 26%
# 30
# MatPat
# MatPat
# 38%
# 26%
# 31
# Nikkie de Jager
# Nikkie de Jager
# 42%
# 25%
# 32
# Ruben Gunderson
# Ruben Gunderson
# 37%
# 25%
# 33
# Matt Stonie
# Matt Stonie
# 41%
# 25%
# 34
# Logan Paul
# Logan Paul
# 64%
# 25%
# 35
# The Try Guys
# The Try Guys
# 42%
# 25%
# 36
# Pokimane
# Pokimane
# 46%
# 25%
# 37
# Minimalist Baker
# Minimalist Baker
# 39%
# 25%
# 38
# Rebecca Zamolo
# Rebecca Zamolo
# 41%
# 25%
# 39
# Markiplier
# Markiplier
# 44%
# 25%
# 40
# Matt King
# Matt King
# 41%
# 25%
# 41
# Ryan Trehan
# Ryan Trehan
# 40%
# 25%
# 42
# Michelle Phan
# Michelle Phan
# 38%
# 25%
# 43
# Rosanna Pansino
# Rosanna Pansino
# 40%
# 25%
# 44
# Jack Morris
# Jack Morris
# 39%
# 25%
# 45
# Troye Sivan
# Troye Sivan
# 44%
# 25%
# 46
# Sam and Colby
# Sam and Colby
# 43%
# 25%
# 47
# Juan Pablo “Juanpa” Zurita
# Juan Pablo “Juanpa” Zurita
# 39%
# 25%
# 48
# Khaby Lame
# Khaby Lame
# 38%
# 25%
# 49
# Nick DiGiovanni
# Nick DiGiovanni
# 41%
# 25%
# 50
# Michelle Lewin
# Michelle Lewin
# 37%
# 25%
# 51
# Sammy Robinson
# Sammy Robinson
# 36%
# 24%
# 52
# Annette White
# Annette White
# 41%
# 24%
# 53
# NickEh30
# NickEh30
# 39%
# 24%
# 54
# Mr Ballen
# Mr Ballen
# 36%
# 24%
# 55
# Charlie McDonnell
# Charlie McDonnell
# 38%
# 24%
# 56
# Hasanabi (Hasan Piker)
# Hasanabi (Hasan Piker)
# 44%
# 24%
# 57
# Saffron Barker
# Saffron Barker
# 38%
# 24%
# 58
# Jeffree Star
# Jeffree Star
# 49%
# 24%
# 59
# Kayla Itsines
# Kayla Itsines
# 38%
# 24%
# 60
# Andrea Russet
# Andrea Russet
# 37%
# 24%
# 61
# Joe Sugg
# Joe Sugg
# 36%
# 24%
# 62
# Demi Bagby
# Demi Bagby
# 40%
# 24%
# 63
# Lance Stewart
# Lance Stewart
# 38%
# 24%
# 64
# The Points Guy
# The Points Guy
# 36%
# 24%
# 65
# Mark Rober
# Mark Rober
# 38%
# 24%
# 66
# Jay Alvarrez
# Jay Alvarrez
# 39%
# 24%
# 67
# Adin Ross
# Adin Ross
# 42%
# 24%
# 68
# The Blonde Abroad
# The Blonde Abroad
# 38%
# 24%
# 69
# Danny Gonzalez
# Danny Gonzalez
# 42%
# 24%
# 70
# Ling Tang
# Ling Tang
# 39%
# 24%
# 71
# Elliot Tebele
# Elliot Tebele
# 36%
# 24%
# 72
# Alyssa Rose
# Alyssa Rose
# 37%
# 24%
# 73
# Shayla Mitchell
# Shayla Mitchell
# 38%
# 23%
# 74
# Akin Akman
# Akin Akman
# 35%
# 23%
# 75
# Brooklyn and Bailey
# Brooklyn and Bailey
# 38%
# 23%
# 76
# Nikkie De Jager
# Nikkie De Jager
# 39%
# 23%
# 77
# Jack Johnson
# Jack Johnson
# 41%
# 23%
# 78
# Liza Koshy
# Liza Koshy
# 41%
# 23%
# 79
# Gregory DelliCarpini Jr
# Gregory DelliCarpini Jr
# 37%
# 23%
# 80
# tommyinnit
# tommyinnit
# 37%
# 23%
# 81
# Ian Hecox
# Ian Hecox
# 35%
# 23%
# 82
# David Lopez
# David Lopez
# 39%
# 23%
# 83
# Olajide William Olatunji (KSI)
# Olajide William Olatunji (KSI)
# 38%
# 23%
# 84
# Thalia Ho
# Thalia Ho
# 35%
# 23%
# 85
# Ingrid Nilsen
# Ingrid Nilsen
# 39%
# 23%
# 86
# Kandee Johnson
# Kandee Johnson
# 36%
# 23%
# 87
# Emma Hill
# Emma Hill
# 35%
# 23%
# 88
# Banks
# Banks
# 37%
# 23%
# 89
# Dr. Mike Varshavski
# Dr. Mike Varshavski
# 40%
# 23%
# 90
# Alx James
# Alx James
# 35%
# 23%
# 91
# LilyPichu
# LilyPichu
# 36%
# 23%
# 92
# Madelynn Furlong
# Madelynn Furlong
# 39%
# 23%
# 93
# Annemunition
# Annemunition
# 37%
# 23%
# 94
# Talitha Girnus
# Talitha Girnus
# 36%
# 23%
# 95
# F2Freestylers
# F2Freestylers
# 38%
# 23%
# 96
# Noah Beck
# Noah Beck
# 43%
# 23%
# 97
# James Charles
# James Charles
# 46%
# 23%
# 98
# Summer McKeen
# Summer McKeen
# 37%
# 23%
# 99
# Kate McCulley
# Kate McCulley
# 37%
# 23%
# 100
# Philip DeFranco
# Philip DeFranco
# 43%
# 23%
# 101
# Rickey Thompson
# Rickey Thompson
# 37%
# 23%
# 102
# Joshua Bradley - Zerkaa
# Joshua Bradley - Zerkaa
# 39%
# 23%
# 103
# Roman Atwood
# Roman Atwood
# 39%
# 23%
# 104
# Julie Sarinana
# Julie Sarinana
# 37%
# 23%
# 105
# Hannah Bronfman
# Hannah Bronfman
# 36%
# 23%
# 106
# Meghan Rienks
# Meghan Rienks
# 37%
# 23%
# 107
# Molly Yeh
# Molly Yeh
# 37%
# 23%
# 108
# Simply Nailogical
# Simply Nailogical
# 38%
# 23%
# 109
# Tara Milk Tea
# Tara Milk Tea
# 35%
# 23%
# 110
# KingRichard
# KingRichard
# 40%
# 23%
# 111
# Andrew Evans
# Andrew Evans
# 40%
# 23%
# 112
# Elisabeth Akinwale
# Elisabeth Akinwale
# 37%
# 23%
# 113
# Hannah Hart
# Hannah Hart
# 40%
# 23%
# 114
# Louise Pentland
# Louise Pentland
# 37%
# 23%
# 115
# Tanya Burr
# Tanya Burr
# 42%
# 23%
# 116
# Ines de la Fressange
# Ines de la Fressange
# 35%
# 23%
# 117
# Monsieur Dream
# Monsieur Dream
# 35%
# 23%
# 118
# Jay Caesar
# Jay Caesar
# 38%
# 23%
# 119
# Ray William Johnson
# Ray William Johnson
# 38%
# 23%
# 120
# Sidemen
# Sidemen
# 36%
# 23%
# 121
# Lele Pons
# Lele Pons
# 39%
# 23%
# 122
# Cole LaBrant
# Cole LaBrant
# 38%
# 23%
# 123
# Iskra Lawrence
# Iskra Lawrence
# 39%
# 22%
# 124
# Tyler Oakley
# Tyler Oakley
# 42%
# 22%
# 125
# Gabrielle Alexis
# Gabrielle Alexis
# 38%
# 22%
# 126
# Kennedy Cymone
# Kennedy Cymone
# 35%
# 22%
# 127
# Ida Frosk
# Ida Frosk
# 37%
# 22%
# 128
# Jason Stein
# Jason Stein
# 40%
# 22%
# 129
# Luka Sabbat
# Luka Sabbat
# 37%
# 22%
# 130
# Simeon Panda
# Simeon Panda
# 33%
# 22%
# 131
# Gloria Morales
# Gloria Morales
# 35%
# 22%
# 132
# Andrea Russett
# Andrea Russett
# 35%
# 22%
# 133
# Toby Turner
# Toby Turner
# 38%
# 22%
# 134
# Tarik
# Tarik
# 39%
# 22%
# 135
# Myth
# Myth
# 38%
# 22%
# 136
# Danielle Bernstein
# Danielle Bernstein
# 38%
# 22%
# 137
# Alinity
# Alinity
# 40%
# 22%
# 138
# Jerry Purpdrank
# Jerry Purpdrank
# 33%
# 22%
# 139
# Lily Maymac
# Lily Maymac
# 42%
# 22%
# 140
# Mrs. Hinch
# Mrs. Hinch
# 36%
# 22%
# 141
# Jack Douglass
# Jack Douglass
# 37%
# 22%
# 142
# Justine Ezarik
# Justine Ezarik
# 35%
# 22%
# 143
# Ryan Trahan
# Ryan Trahan
# 36%
# 22%
# 144
# Valkyrae
# Valkyrae
# 35%
# 22%
# 145
# JasonTheWeen
# JasonTheWeen
# 36%
# 22%
# 146
# Pei Ketron
# Pei Ketron
# 36%
# 22%
# 147
# Yogscast
# Yogscast
# 35%
# 22%
# 148
# Joe Weller
# Joe Weller
# 37%
# 22%
# 149
# Kevin Fredericks
# Kevin Fredericks
# 34%
# 22%
# 150
# Bugha
# Bugha
# 36%
# 22%
# 151
# Lilly Singh
# Lilly Singh
# 41%
# 22%
# 152
# Larray
# Larray
# 38%
# 22%
# 153
# Naomi Giannopoulos
# Naomi Giannopoulos
# 39%
# 22%
# 154
# Emily Mariko
# Emily Mariko
# 38%
# 22%
# 155
# Meg DeAngelis
# Meg DeAngelis
# 39%
# 22%
# 156
# Samantha Ravndahl
# Samantha Ravndahl
# 36%
# 22%
# 157
# John Stephen Grice
# John Stephen Grice
# 37%
# 22%
# 158
# GloZell Lynette Simon
# GloZell Lynette Simon
# 37%
# 22%
# 159
# Zoe Sugg (Zoella)
# Zoe Sugg (Zoella)
# 37%
# 22%
# 160
# IShowSpeed
# IShowSpeed
# 38%
# 22%
# 161
# Nelk Boys
# Nelk Boys
# 38%
# 22%
# 162
# Cooking with Mima
# Cooking with Mima
# 36%
# 22%
# 163
# Benjamin Lowy
# Benjamin Lowy
# 36%
# 22%
# 164
# Brittany Furlan
# Brittany Furlan
# 38%
# 22%
# 165
# Adorian Deck
# Adorian Deck
# 35%
# 22%
# 166
# Emily Skye
# Emily Skye
# 37%
# 22%
# 167
# Mark Angel Comedy
# Mark Angel Comedy
# 33%
# 22%
# 168
# Hind Deer
# Hind Deer
# 35%
# 22%
# 169
# Loren Gray
# Loren Gray
# 38%
# 22%
# 170
# Jen Selter
# Jen Selter
# 37%
# 22%
# 171
# Nicole Cogan
# Nicole Cogan
# 35%
# 22%
# 172
# Wayne Goss
# Wayne Goss
# 34%
# 22%
# 173
# Dustin Giallanza
# Dustin Giallanza
# 35%
# 22%
# 174
# Tana Mongeau
# Tana Mongeau
# 40%
# 22%
# 175
# Baddie Winkle
# Baddie Winkle
# 36%
# 22%
# 176
# Shroud
# Shroud
# 36%
# 22%
# 177
# Alfie Deyes (Pointless Blog)
# Alfie Deyes (Pointless Blog)
# 36%
# 21%
# 178
# Hannah Stocking
# Hannah Stocking
# 34%
# 21%
# 179
# JiDion
# JiDion
# 39%
# 21%
# 180
# Vic Blends
# Vic Blends
# 40%
# 21%
# 181
# Natalie Myers
# Natalie Myers
# 39%
# 21%
# 182
# Adam Dahlberg
# Adam Dahlberg
# 37%
# 21%
# 183
# Murad Osmann
# Murad Osmann
# 35%
# 21%
# 184
# Lauren Bullen
# Lauren Bullen
# 35%
# 21%
# 185
# Tyler "Ninja" Blevins
# Tyler "Ninja" Blevins
# 38%
# 21%
# 186
# CR Tan
# CR Tan
# 38%
# 21%
# 187
# Mandi Gubler
# Mandi Gubler
# 35%
# 21%
# 188
# Marcus Butler
# Marcus Butler
# 35%
# 21%
# 189
# Nailea Devora
# Nailea Devora
# 32%
# 21%
# 190
# Isabella Thordsen
# Isabella Thordsen
# 37%
# 21%
# 191
# Trainwreckstv
# Trainwreckstv
# 37%
# 21%
# 192
# NickMercs
# NickMercs
# 36%
# 21%
# 193
# Valeria Lukyanova
# Valeria Lukyanova
# 36%
# 21%
# 194
# Jimmy Chin
# Jimmy Chin
# 38%
# 21%
# 195
# Chiara Ferragni
# Chiara Ferragni
# 37%
# 21%
# 196
# Jenn Im
# Jenn Im
# 34%
# 21%
# 197
# Timthetatman
# Timthetatman
# 40%
# 21%
# 198
# Clix
# Clix
# 36%
# 21%
# 199
# Bretman Rock
# Bretman Rock
# 37%
# 21%
# 200
# Megan Gilmore
# Megan Gilmore
# 35%
# 21%
# 201
# Fozi Mozi
# Fozi Mozi
# 34%
# 21%
# 202
# Matthew Karsten
# Matthew Karsten
# 35%
# 21%
# 203
# Sommer Ray
# Sommer Ray
# 38%
# 21%
# 204
# Carrington Durham
# Carrington Durham
# 34%
# 21%
# 205
# Miranda Sings
# Miranda Sings
# 45%
# 21%
# 206
# The Bucket List Family
# The Bucket List Family
# 36%
# 21%
# 207
# Gabriel Cabrera
# Gabriel Cabrera
# 37%
# 21%
# 208
# Laura Large
# Laura Large
# 35%
# 21%
# 209
# Dennis the Prescott
# Dennis the Prescott
# 36%
# 21%
# 210
# Edith W Young
# Edith W Young
# 33%
# 21%
# 211
# Kim Loaiza
# Kim Loaiza
# 36%
# 21%
# 212
# Lizzy Capri
# Lizzy Capri
# 36%
# 21%
# 213
# Dan Howell
# Dan Howell
# 33%
# 21%
# 214
# Alex Botez
# Alex Botez
# 32%
# 21%
# 215
# Cameron Dallas
# Cameron Dallas
# 38%
# 21%
# 216
# Evan Fong
# Evan Fong
# 35%
# 21%
# 217
# Jessie Chanes
# Jessie Chanes
# 35%
# 21%
# 218
# Tai Lopez
# Tai Lopez
# 34%
# 21%
# 219
# Mikecrackq
# Mikecrackq
# 32%
# 21%
# 220
# Summit1G
# Summit1G
# 35%
# 21%
# 221
# Tom Cassell
# Tom Cassell
# 35%
# 21%
# 222
# Rudy Mancuso
# Rudy Mancuso
# 34%
# 21%
# 223
# Druski
# Druski
# 35%
# 21%
# 224
# Negin Mirsalehi
# Negin Mirsalehi
# 34%
# 21%
# 225
# Chris Burkard
# Chris Burkard
# 34%
# 21%
# 226
# Nash Grier
# Nash Grier
# 37%
# 21%
# 227
# Sykkuno
# Sykkuno
# 34%
# 21%
# 228
# Massy Arias
# Massy Arias
# 38%
# 21%
# 229
# Kaleb Anthony
# Kaleb Anthony
# 34%
# 21%
# 230
# CalebCity
# CalebCity
# 37%
# 21%
# 231
# Ling K Tang
# Ling K Tang
# 36%
# 21%
# 232
# Lirik
# Lirik
# 39%
# 21%
# 233
# Manny Gutierrez
# Manny Gutierrez
# 39%
# 21%
# 234
# Tfue
# Tfue
# 35%
# 21%
# 235
# Joe Wicks (The Body Coach)
# Joe Wicks (The Body Coach)
# 35%
# 21%
# 236
# Will Taylor
# Will Taylor
# 32%
# 21%
# 237
# Julia Hengel
# Julia Hengel
# 35%
# 20%
# 238
# Ashley Stark Kenner
# Ashley Stark Kenner
# 36%
# 20%
# 239
# Dixie D'Amelio
# Dixie D'Amelio
# 38%
# 20%
# 240
# Russ Crandall
# Russ Crandall
# 36%
# 20%
# 241
# Cassey Ho
# Cassey Ho
# 34%
# 20%
# 242
# Matthew Espinosa
# Matthew Espinosa
# 40%
# 20%
# 243
# Shaaanxo
# Shaaanxo
# 34%
# 20%
# 244
# Fat Girls Traveling
# Fat Girls Traveling
# 34%
# 20%
# 245
# Grace Bonney
# Grace Bonney
# 33%
# 20%
# 246
# Beta Squad
# Beta Squad
# 34%
# 20%
# 247
# Thomas Sanders
# Thomas Sanders
# 41%
# 20%
# 248
# KaiCenat
# KaiCenat
# 38%
# 20%
# 249
# Ty Haney
# Ty Haney
# 38%
# 20%
# 250
# Collins Key
# Collins Key
# 35%
# 20%
# 251
# Ashrod
# Ashrod
# 36%
# 20%
# 252
# Andrea Botez
# Andrea Botez
# 37%
# 20%
# 253
# Aimee Song
# Aimee Song
# 31%
# 20%
# 254
# Eric Stoen
# Eric Stoen
# 36%
# 20%
# 255
# Lil Tay
# Lil Tay
# 41%
# 20%
# 256
# Molly Tavoletti
# Molly Tavoletti
# 33%
# 20%
# 257
# Oliver Proudlock
# Oliver Proudlock
# 33%
# 20%
# 258
# DrDisRespect
# DrDisRespect
# 37%
# 20%
# 259
# Brunch Boys
# Brunch Boys
# 33%
# 20%
# 260
# Ironmouse
# Ironmouse
# 36%
# 20%
# 261
# Nina Williams
# Nina Williams
# 34%
# 20%
# 262
# Deji Olatunji
# Deji Olatunji
# 35%
# 20%
# 263
# QuarterJade
# QuarterJade
# 34%
# 20%
# 264
# iiTzTimmy
# iiTzTimmy
# 33%
# 20%
# 265
# Julia Sariñana
# Julia Sariñana
# 34%
# 20%
# 266
# Daniel Middleton
# Daniel Middleton
# 34%
# 20%
# 267
# Jim Chapman
# Jim Chapman
# 34%
# 20%
# 268
# Craig Thompson - Mini Ladd
# Craig Thompson - Mini Ladd
# 34%
# 20%
# 269
# Ela Vegan
# Ela Vegan
# 32%
# 20%
# 270
# Amouranth
# Amouranth
# 34%
# 20%
# 271
# StableRonaldo
# StableRonaldo
# 34%
# 20%
# 272
# The Planet D
# The Planet D
# 34%
# 20%
# 273
# Nicolette Mason
# Nicolette Mason
# 36%
# 20%
# 274
# L'atelier de Roxane
# L'atelier de Roxane
# 35%
# 20%
# 275
# Kemo Marriott
# Kemo Marriott
# 34%
# 20%
# 276
# Donjay
# Donjay
# 35%
# 20%
# 277
# QTCinderella
# QTCinderella
# 37%
# 20%
# 278
# Saudah Saleem
# Saudah Saleem
# 36%
# 20%
# 279
# DeStorm Power
# DeStorm Power
# 35%
# 20%
# 280
# Joey Graceffa
# Joey Graceffa
# 36%
# 20%
# 281
# Shane Daweson
# Shane Daweson
# 43%
# 20%
# 282
# Colin Furze
# Colin Furze
# 32%
# 20%
# 283
# Ilhan Eroglu
# Ilhan Eroglu
# 34%
# 20%
# 284
# Mariano Di Vaio
# Mariano Di Vaio
# 35%
# 20%
# 285
# Amymarie Gaertner
# Amymarie Gaertner
# 33%
# 20%
# 286
# Karl Jacobs
# Karl Jacobs
# 38%
# 20%
# 287
# Lacy
# Lacy
# 35%
# 19%
# 288
# Jack Harries
# Jack Harries
# 37%
# 19%
# 289
# Lindsey Silverman Love
# Lindsey Silverman Love
# 32%
# 19%
# 290
# Casa Chicks
# Casa Chicks
# 33%
# 19%
# 291
# Caspar Lee
# Caspar Lee
# 34%
# 19%
# 292
# Rafi Fine
# Rafi Fine
# 33%
# 19%
# 293
# David Chang
# David Chang
# 36%
# 19%
# 294
# Amanda Cerny
# Amanda Cerny
# 33%
# 19%
# 295
# Joana Ceddia
# Joana Ceddia
# 31%
# 19%
# 296
# Giovanna Engelbert
# Giovanna Engelbert
# 33%
# 19%
# 297
# Kordale Lewis
# Kordale Lewis
# 34%
# 19%
# 298
# Majawyh
# Majawyh
# 32%
# 19%
# 299
# Lil Miquela
# Lil Miquela
# 35%
# 19%
# 300
# Callum Leighton Airey
# Callum Leighton Airey
# 36%
# 19%
# 301
# Alexa Chung
# Alexa Chung
# 36%
# 19%
# 302
# Arishfa Khan
# Arishfa Khan
# 33%
# 19%
# 303
# Safiya Nygaard
# Safiya Nygaard
# 33%
# 19%
# 304
# Gabi Gregg
# Gabi Gregg
# 36%
# 19%
# 305
# YourRage
# YourRage
# 35%
# 19%
# 306
# Domelipa
# Domelipa
# 32%
# 19%
# 307
# Ella Woodward (Deliciously Ella)
# Ella Woodward (Deliciously Ella)
# 32%
# 19%
# 308
# Phil Lester
# Phil Lester
# 35%
# 19%
# 309
# Curtis Lepore
# Curtis Lepore
# 34%
# 19%
# 310
# Paul Nicklen
# Paul Nicklen
# 36%
# 19%
# 311
# Jeff Rose
# Jeff Rose
# 37%
# 19%
# 312
# Brad Lau
# Brad Lau
# 34%
# 19%
# 313
# Michael Yamashita
# Michael Yamashita
# 33%
# 19%
# 314
# Galey Alix
# Galey Alix
# 34%
# 19%
# 315
# CC Clarke Beauty
# CC Clarke Beauty
# 35%
# 19%
# 316
# xQc
# xQc
# 37%
# 19%
# 317
# Sydney Leroux Dwyer
# Sydney Leroux Dwyer
# 29%
# 19%
# 318
# Whindersson Nunes
# Whindersson Nunes
# 34%
# 18%
# 319
# ZooMaa
# ZooMaa
# 32%
# 18%
# 320
# Anwar Jibawi
# Anwar Jibawi
# 33%
# 18%
# 321
# Brent Rivera
# Brent Rivera
# 37%
# 18%
# 322
# Laura Noltemeyer
# Laura Noltemeyer
# 33%
# 18%
# 323
# Kelsey Calemine
# Kelsey Calemine
# 36%
# 18%
# 324
# Studio McGee
# Studio McGee
# 35%
# 18%
# 325
# Garance Dore
# Garance Dore
# 32%
# 18%
# 326
# CourageJD
# CourageJD
# 31%
# 18%
# 327
# TenZ
# TenZ
# 30%
# 18%
# 328
# Perrie Edwards
# Perrie Edwards
# 33%
# 18%
# 329
# Stacy Kranitz
# Stacy Kranitz
# 37%
# 18%
# 330
# DrLupo
# DrLupo
# 37%
# 18%
# 331
# Dakotaz
# Dakotaz
# 35%
# 18%
# 332
# Yumna Jawad
# Yumna Jawad
# 32%
# 18%
# 333
# Jannid Olsson Deler
# Jannid Olsson Deler
# 33%
# 18%
# 334
# Joseph Garrett
# Joseph Garrett
# 34%
# 17%
# 335
# German Garmendia
# German Garmendia
# 34%
# 17%
# 336
# Gus Johnson
# Gus Johnson
# 31%
# 17%
# 337
# Sjana Elise Earp
# Sjana Elise Earp
# 30%
# 17%
# 338
# Faze Rug
# Faze Rug
# 33%
# 17%
# 339
# Louis Cole
# Louis Cole
# 35%
# 16%
# 340
# Ajey Nagar
# Ajey Nagar
# 30%
# 16%
# 341
# Gueorgui Pinkhassov
# Gueorgui Pinkhassov
# 30%
# 16%
# 342
# Ada Oguntodu
# Ada Oguntodu
# 31%
# 16%
# 343
# Josh Ostrovsky
# Josh Ostrovsky
# 33%
# 16%
# """
# wait = 2
# save = ""
# all = []
# all2 = []
# for i in test: 
#     if i == "\n":
#         wait -= 1
#         all.append(save.replace("\n",""))

#         save = ""
#     if i == "\n" and wait == 0:
#         all2.append(all)
#         all = []
#         wait = 5 
#     if 4 >= wait >= 2:
#         save += i


# list2 = []
# for i in all2:
#     list1 = []
#     for j in i:
#         if j == "":
#             pass
#         else:
#             list1.append(j)
#     list2.append(list1)
# print(list2)
    
