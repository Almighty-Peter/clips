import requests
import re
from pytube import YouTube
import sqlite3
import json
from datetime import datetime
date = datetime.now().strftime('%Y-%m-%d')


connection = sqlite3.connect('local_database.db')
cursor = connection.cursor()


create_table_query = """
CREATE TABLE IF NOT EXISTS YTVideos (
    video_id CHAR(11),  
    channel TEXT,
    title TEXT,
    position_found INT,
    views INT,
    date char(10),
    search_query TEXT,
    data TEXT,


    PRIMARY KEY(video_id)
);
"""

cursor.execute(create_table_query)
connection.commit()


def match_extract(patern, response):
    videos = []
    matches_video = re.findall(patern, response)
    for video in matches_video:
        if (video in videos):
            pass
        else:
            videos.append(video)
    return videos


def links_yt(query):
    query = query.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    
    response = requests.get(url)
    matches_video = match_extract(r'watch\?v=(.{11})', response.text)
    # matches_short = match_extract(r'shorts/(.{11})', response.text)
    
    return matches_video #,matches_short

def video_exists(video_id):
    cursor.execute("SELECT 1 FROM YTVideos WHERE video_id = ?", (video_id,))
    return cursor.fetchone() is not None


list = [['MrBeast', '63%', '36%'], ['Joanna Stevens Gaines', '51%', '32%'], ['Zach King', '41%', '29%'], ['Good Mythical Morning', '43%', '28%'], ['Ryan Higa', '42%', '28%'], ['Liz Eswein', '41%', '28%'], ['Lauren Conrad', '51%', '28%'], ['Andrew Tate', '60%', '28%'], ['Addison Rae', '47%', '27%'], ['Camila Coelho', '42%', '27%'], ['Casey Neistat', '44%', '27%'], ['Huda Kattan', '40%', '27%'], ['Uncle Roger', '42%', '26%'], ['Olivia Dunne', '43%', '26%'], ['Eddie Hall', '42%', '26%'], ['Dude Perfect', '45%', '26%'], ['Stacia Mar', '39%', '26%'], ['David Dobrik', '44%', '26%'], ['Andrew B. Bachelor', '40%', '26%'], ['Ludwig', '41%', '26%'], ['PewDiePie', '52%', '26%'], ['Jessica Vasquez', '39%', '26%'], ['Jenni Kayne', '39%', '26%'], ['Jake Paul', '62%', '26%'], ['Charli D’amelio', '46%', '26%'], ['Marie Kondo', '48%', '26%'], ['Swagg (Faze Swagg)', '40%', '26%'], ["Charli D'Amelio", '49%', '26%'], ['Emma Chamberlain', '41%', '26%'], ['MatPat', '38%', '26%'], ['Nikkie de Jager', '42%', '25%'], ['Ruben Gunderson', '37%', '25%'], ['Matt Stonie', '41%', '25%'], ['Logan Paul', '64%', '25%'], ['The Try Guys', '42%', '25%'], ['Pokimane', '46%', '25%'], ['Minimalist Baker', '39%', '25%'], ['Rebecca Zamolo', '41%', '25%'], ['Markiplier', '44%', '25%'], ['Matt King', '41%', '25%'], ['Ryan Trehan', '40%', '25%'], ['Michelle Phan', '38%', '25%'], ['Rosanna Pansino', '40%', '25%'], ['Jack Morris', '39%', '25%'], ['Troye Sivan', '44%', '25%'], ['Sam and Colby', '43%', '25%'], ['Juan Pablo “Juanpa” Zurita', '39%', '25%'], ['Khaby Lame', '38%', '25%'], ['Nick DiGiovanni', '41%', '25%'], ['Michelle Lewin', '37%', '25%'], ['Sammy Robinson', '36%', '24%'], ['Annette White', '41%', '24%'], ['NickEh30', '39%', '24%'], ['Mr Ballen', '36%', '24%'], ['Charlie McDonnell', '38%', '24%'], ['Hasanabi (Hasan Piker)', '44%', '24%'], ['Saffron Barker', '38%', '24%'], ['Jeffree Star', '49%', '24%'], ['Kayla Itsines', '38%', '24%'], ['Andrea Russet', '37%', '24%'], ['Joe Sugg', '36%', '24%'], ['Demi Bagby', '40%', '24%'], ['Lance Stewart', '38%', '24%'], ['The Points Guy', '36%', '24%'], ['Mark Rober', '38%', '24%'], ['Jay Alvarrez', '39%', '24%'], ['Adin Ross', '42%', '24%'], ['The Blonde Abroad', '38%', '24%'], ['Danny Gonzalez', '42%', '24%'], ['Ling Tang', '39%', '24%'], ['Elliot Tebele', '36%', '24%'], ['Alyssa Rose', '37%', '24%'], ['Shayla Mitchell', '38%', '23%'], ['Akin Akman', '35%', '23%'], ['Brooklyn and Bailey', '38%', '23%'], ['Nikkie De Jager', '39%', '23%'], ['Jack Johnson', '41%', '23%'], ['Liza Koshy', '41%', '23%'], ['Gregory DelliCarpini Jr', '37%', '23%'], ['tommyinnit', '37%', '23%'], ['Ian Hecox', '35%', '23%'], ['David Lopez', '39%', '23%'], ['Olajide William Olatunji (KSI)', '38%', '23%'], ['Thalia Ho', '35%', '23%'], ['Ingrid Nilsen', '39%', '23%'], ['Kandee Johnson', '36%', '23%'], ['Emma Hill', '35%', '23%'], ['Banks', '37%', '23%'], ['Dr. Mike Varshavski', '40%', '23%'], ['Alx James', '35%', '23%'], ['LilyPichu', '36%', '23%'], ['Madelynn Furlong', '39%', '23%'], ['Annemunition', '37%', '23%'], ['Talitha Girnus', '36%', '23%'], ['F2Freestylers', '38%', '23%'], ['Noah Beck', '43%', '23%'], ['James Charles', '46%', '23%'], ['Summer McKeen', '37%', '23%'], ['Kate McCulley', '37%', '23%'], ['Philip DeFranco', '43%', '23%'], ['Rickey Thompson', '37%', '23%'], ['Joshua Bradley - Zerkaa', '39%', '23%'], ['Roman Atwood', '39%', '23%'], ['Julie Sarinana', '37%', '23%'], ['Hannah Bronfman', '36%', '23%'], ['Meghan Rienks', '37%', '23%'], ['Molly Yeh', '37%', '23%'], ['Simply Nailogical', '38%', '23%'], ['Tara Milk Tea', '35%', '23%'], ['KingRichard', '40%', '23%'], ['Andrew Evans', '40%', '23%'], ['Elisabeth Akinwale', '37%', '23%'], ['Hannah Hart', '40%', '23%'], ['Louise Pentland', '37%', '23%'], ['Tanya Burr', '42%', '23%'], ['Ines de la Fressange', '35%', '23%'], ['Monsieur Dream', '35%', '23%'], ['Jay Caesar', '38%', '23%'], ['Ray William Johnson', '38%', '23%'], ['Sidemen', '36%', '23%'], ['Lele Pons', '39%', '23%'], ['Cole LaBrant', '38%', '23%'], ['Iskra Lawrence', '39%', '22%'], ['Tyler Oakley', '42%', '22%'], ['Gabrielle Alexis', '38%', '22%'], ['Kennedy Cymone', '35%', '22%'], ['Ida Frosk', '37%', '22%'], ['Jason Stein', '40%', '22%'], ['Luka Sabbat', '37%', '22%'], ['Simeon Panda', '33%', '22%'], ['Gloria Morales', '35%', '22%'], ['Andrea Russett', '35%', '22%'], ['Toby Turner', '38%', '22%'], ['Tarik', '39%', '22%'], ['Myth', '38%', '22%'], ['Danielle Bernstein', '38%', '22%'], ['Alinity', '40%', '22%'], ['Jerry Purpdrank', '33%', '22%'], ['Lily Maymac', '42%', '22%'], ['Mrs. Hinch', '36%', '22%'], ['Jack Douglass', '37%', '22%'], ['Justine Ezarik', '35%', '22%'], ['Ryan Trahan', '36%', '22%'], ['Valkyrae', '35%', '22%'], ['JasonTheWeen', '36%', '22%'], ['Pei Ketron', '36%', '22%'], ['Yogscast', '35%', '22%'], ['Joe Weller', '37%', '22%'], ['Kevin Fredericks', '34%', '22%'], ['Bugha', '36%', '22%'], ['Lilly Singh', '41%', '22%'], ['Larray', '38%', '22%'], ['Naomi Giannopoulos', '39%', '22%'], ['Emily Mariko', '38%', '22%'], ['Meg DeAngelis', '39%', '22%'], ['Samantha Ravndahl', '36%', '22%'], ['John Stephen Grice', '37%', '22%'], ['GloZell Lynette Simon', '37%', '22%'], ['Zoe Sugg (Zoella)', '37%', '22%'], ['IShowSpeed', '38%', '22%'], ['Nelk Boys', '38%', '22%'], ['Cooking with Mima', '36%', '22%'], ['Benjamin Lowy', '36%', '22%'], ['Brittany Furlan', '38%', '22%'], ['Adorian Deck', '35%', '22%'], ['Emily Skye', '37%', '22%'], ['Mark Angel Comedy', '33%', '22%'], ['Hind Deer', '35%', '22%'], ['Loren Gray', '38%', '22%'], ['Jen Selter', '37%', '22%'], ['Nicole Cogan', '35%', '22%'], ['Wayne Goss', '34%', '22%'], ['Dustin Giallanza', '35%', '22%'], ['Tana Mongeau', '40%', '22%'], ['Baddie Winkle', '36%', '22%'], ['Shroud', '36%', '22%'], ['Alfie Deyes (Pointless Blog)', '36%', '21%'], ['Hannah Stocking', '34%', '21%'], ['JiDion', '39%', '21%'], ['Vic Blends', '40%', '21%'], ['Natalie Myers', '39%', '21%'], ['Adam Dahlberg', '37%', '21%'], ['Murad Osmann', '35%', '21%'], ['Lauren Bullen', '35%', '21%'], ['Tyler "Ninja" Blevins', '38%', '21%'], ['CR Tan', '38%', '21%'], ['Mandi Gubler', '35%', '21%'], ['Marcus Butler', '35%', '21%'], ['Nailea Devora', '32%', '21%'], ['Isabella Thordsen', '37%', '21%'], ['Trainwreckstv', '37%', '21%'], ['NickMercs', '36%', '21%'], ['Valeria Lukyanova', '36%', '21%'], ['Jimmy Chin', '38%', '21%'], ['Chiara Ferragni', '37%', '21%'], ['Jenn Im', '34%', '21%'], ['Timthetatman', '40%', '21%'], ['Clix', '36%', '21%'], ['Bretman Rock', '37%', '21%'], ['Megan Gilmore', '35%', '21%'], ['Fozi Mozi', '34%', '21%'], ['Matthew Karsten', '35%', '21%'], ['Sommer Ray', '38%', '21%'], ['Carrington Durham', '34%', '21%'], ['Miranda Sings', '45%', '21%'], ['The Bucket List Family', '36%', '21%'], ['Gabriel Cabrera', '37%', '21%'], ['Laura Large', '35%', '21%'], ['Dennis the Prescott', '36%', '21%'], ['Edith W Young', '33%', '21%'], ['Kim Loaiza', '36%', '21%'], ['Lizzy Capri', '36%', '21%'], ['Dan Howell', '33%', '21%'], ['Alex Botez', '32%', '21%'], ['Cameron Dallas', '38%', '21%'], ['Evan Fong', '35%', '21%'], ['Jessie Chanes', '35%', '21%'], ['Tai Lopez', '34%', '21%'], ['Mikecrackq', '32%', '21%'], ['Summit1G', '35%', '21%'], ['Tom Cassell', '35%', '21%'], ['Rudy Mancuso', '34%', '21%'], ['Druski', '35%', '21%'], ['Negin Mirsalehi', '34%', '21%'], ['Chris Burkard', '34%', '21%'], ['Nash Grier', '37%', '21%'], ['Sykkuno', '34%', '21%'], ['Massy Arias', '38%', '21%'], ['Kaleb Anthony', '34%', '21%'], ['CalebCity', '37%', '21%'], ['Ling K Tang', '36%', '21%'], ['Lirik', '39%', '21%'], ['Manny Gutierrez', '39%', '21%'], ['Tfue', '35%', '21%'], ['Joe Wicks (The Body Coach)', '35%', '21%'], ['Will Taylor', '32%', '21%'], ['Julia Hengel', '35%', '20%'], ['Ashley Stark Kenner', '36%', '20%'], ["Dixie D'Amelio", '38%', '20%'], ['Russ Crandall', '36%', '20%'], ['Cassey Ho', '34%', '20%'], ['Matthew Espinosa', '40%', '20%'], ['Shaaanxo', '34%', '20%'], ['Fat Girls Traveling', '34%', '20%'], ['Grace Bonney', '33%', '20%'], ['Beta Squad', '34%', '20%'], ['Thomas Sanders', '41%', '20%'], ['KaiCenat', '38%', '20%'], ['Ty Haney', '38%', '20%'], ['Collins Key', '35%', '20%'], ['Ashrod', '36%', '20%'], ['Andrea Botez', '37%', '20%'], ['Aimee Song', '31%', '20%'], ['Eric Stoen', '36%', '20%'], ['Lil Tay', '41%', '20%'], ['Molly Tavoletti', '33%', '20%'], ['Oliver Proudlock', '33%', '20%'], ['DrDisRespect', '37%', '20%'], ['Brunch Boys', '33%', '20%'], ['Ironmouse', '36%', '20%'], ['Nina Williams', '34%', '20%'], ['Deji Olatunji', '35%', '20%'], ['QuarterJade', '34%', '20%'], ['iiTzTimmy', '33%', '20%'], ['Julia Sariñana', '34%', '20%'], ['Daniel Middleton', '34%', '20%'], ['Jim Chapman', '34%', '20%'], ['Craig Thompson - Mini Ladd', '34%', '20%'], ['Ela Vegan', '32%', '20%'], ['Amouranth', '34%', '20%'], ['StableRonaldo', '34%', '20%'], ['The Planet D', '34%', '20%'], ['Nicolette Mason', '36%', '20%'], ["L'atelier de Roxane", '35%', '20%'], ['Kemo Marriott', '34%', '20%'], ['Donjay', '35%', '20%'], ['QTCinderella', '37%', '20%'], ['Saudah Saleem', '36%', '20%'], ['DeStorm Power', '35%', '20%'], ['Joey Graceffa', '36%', '20%'], ['Shane Daweson', '43%', '20%'], ['Colin Furze', '32%', '20%'], ['Ilhan Eroglu', '34%', '20%'], ['Mariano Di Vaio', '35%', '20%'], ['Amymarie Gaertner', '33%', '20%'], ['Karl Jacobs', '38%', '20%'], ['Lacy', '35%', '19%'], ['Jack Harries', '37%', '19%'], ['Lindsey Silverman Love', '32%', '19%'], ['Casa Chicks', '33%', '19%'], ['Caspar Lee', '34%', '19%'], ['Rafi Fine', '33%', '19%'], ['David Chang', '36%', '19%'], ['Amanda Cerny', '33%', '19%'], ['Joana Ceddia', '31%', '19%'], ['Giovanna Engelbert', '33%', '19%'], ['Kordale Lewis', '34%', '19%'], ['Majawyh', '32%', '19%'], ['Lil Miquela', '35%', '19%'], ['Callum Leighton Airey', '36%', '19%'], ['Alexa Chung', '36%', '19%'], ['Arishfa Khan', '33%', '19%'], ['Safiya Nygaard', '33%', '19%'], ['Gabi Gregg', '36%', '19%'], ['YourRage', '35%', '19%'], ['Domelipa', '32%', '19%'], ['Ella Woodward (Deliciously Ella)', '32%', '19%'], ['Phil Lester', '35%', '19%'], ['Curtis Lepore', '34%', '19%'], ['Paul Nicklen', '36%', '19%'], ['Jeff Rose', '37%', '19%'], ['Brad Lau', '34%', '19%'], ['Michael Yamashita', '33%', '19%'], ['Galey Alix', '34%', '19%'], ['CC Clarke Beauty', '35%', '19%'], ['xQc', '37%', '19%'], ['Sydney Leroux Dwyer', '29%', '19%'], ['Whindersson Nunes', '34%', '18%'], ['ZooMaa', '32%', '18%'], ['Anwar Jibawi', '33%', '18%'], ['Brent Rivera', '37%', '18%'], ['Laura Noltemeyer', '33%', '18%'], ['Kelsey Calemine', '36%', '18%'], ['Studio McGee', '35%', '18%'], ['Garance Dore', '32%', '18%'], ['CourageJD', '31%', '18%'], ['TenZ', '30%', '18%'], ['Perrie Edwards', '33%', '18%'], ['Stacy Kranitz', '37%', '18%'], ['DrLupo', '37%', '18%'], ['Dakotaz', '35%', '18%'], ['Yumna Jawad', '32%', '18%'], ['Jannid Olsson Deler', '33%', '18%'], ['Joseph Garrett', '34%', '17%'], ['German Garmendia', '34%', '17%'], ['Gus Johnson', '31%', '17%'], ['Sjana Elise Earp', '30%', '17%'], ['Faze Rug', '33%', '17%'], ['Louis Cole', '35%', '16%'], ['Ajey Nagar', '30%', '16%'], ['Gueorgui Pinkhassov', '30%', '16%'], ['Ada Oguntodu', '31%', '16%']]
for person in list:

    search_query = person[0]

    data = {
        "found": "https://today.yougov.com/ratings/entertainment/popularity/influencers/all",
        "person": person[0],
        "date": "The most popular influencers (Q2 2024)",
        "fame": person[1],
        "popularity": person[2]
    }
    data = json.dumps(data)

    yt_codes = links_yt(person[0])
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
        

cursor.close()
connection.close()
