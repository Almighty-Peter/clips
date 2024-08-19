# create_table_query = """
# CREATE TABLE IF NOT EXISTS TKCuts (
#     video_id CHAR(11),  
#     channel TEXT,
#     startTime INT,
#     endTime INT,
#     date CHAR(10),
#     embedding BLOB,
#     TKLink TEXT,
#     brainRoot CHAR(11),
#     brainRoot_startTime INT,
#     brainRoot_endTime INT,

#     sizeOfCaptionstoGptSEC INT,
#     distanceFromStarEndSEC INT,
#     distanceFromClipsSEC INT,
#     getHowMany INT,
#     getManyInstedOfThreshold BOOLEAN,
#     retentionThreshold INT,
#     startClipBeforeSEC INT,
#     startClipAfterSEC INT,
#     qualityOfVideo INT,
#     borderBettewnText INT,
#     maxCharsText INT,    
#     fontDefult VARCHAR(50),
#     fontsizeDefult INT,
#     colorDefult VARCHAR(20),
#     bg_colorDefult VARCHAR(20),
#     stroke_colorDefult VARCHAR(20),
#     stroke_widthDefult INT,
#     fontMarked VARCHAR(50),
#     fontsizeMarked INT,
#     colorMarked VARCHAR(20),
#     bg_colorMarked VARCHAR(20),
#     stroke_colorMarked VARCHAR(20),
#     stroke_widthMarked INT, 
    

#     PRIMARY KEY(videoID, startTime, endTime)
# );
# """



# def generate_random_record():
#     record = {
#         "videoID": generate_random_youtube_id(),
#         "channel": ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(1)),
#         "startTime": random.randint(0, 3600),
#         "endTime": random.randint(3601, 7200),
#         "date": datetime.datetime.now().strftime("%Y-%m-%d"),
#         "embedding": generate_random_embedding(),
#         "TKLink": generate_random_tiktok_link(),
#         "brainRoot": generate_random_youtube_id(),
#         "brainRoot_startTime": random.randint(0, 3600),
#         "brainRoot_endTime": random.randint(3601, 7200),


#         "sizeOfCaptionstoGptSEC": sizeOfCaptionstoGptSEC,
#         "distanceFromStarEndSEC": distanceFromStarEndSEC,
#         "distanceFromClipsSEC": distanceFromClipsSEC,
#         "getHowMany": getHowMany,
#         "getManyInstedOfThreshold": getManyInstedOfThreshold,
#         "retentionThreshold": retentionThreshold,
#         "startClipBeforeSEC": startClipBeforeSEC,
#         "startClipAfterSEC": startClipAfterSEC,
#         "qualityOfVideo": qualityOfVideo,
#         "borderBettewnText": borderBettewnText,
#         "maxCharsText": maxCharsText,    
#         "fontDefult": fontDefult,
#         "fontsizeDefult": fontsizeDefult,
#         "colorDefult": colorDefult,
#         "bg_colorDefult": bg_colorDefult,
#         "stroke_colorDefult": stroke_colorDefult,
#         "stroke_widthDefult": stroke_widthDefult,
#         "fontMarked": fontMarked,
#         "fontsizeMarked": fontsizeMarked,
#         "colorMarked": colorMarked,
#         "bg_colorMarked": bg_colorMarked,
#         "stroke_colorMarked": stroke_colorMarked,
#         "stroke_widthMarked": stroke_widthMarked,
#     }
#     return record





sizeOfCaptionstoGptSEC = 22
distanceFromStarEndSEC = 30
distanceFromClipsSEC = 20

getHowMany = 1
getManyInstedOfThreshold = True
retentionThreshold = 60 # lower better

startClipBeforeSEC = 3
startClipAfterSEC = 1
qualityOfVideo=10 # a multiple of 108 and 192 as this is 1/10 of 1080 by 1920 the frame of tiktok

borderBettewnText = 100
maxCharsText = 25    

fontDefult="DejaVu Mono Sans"
fontsizeDefult=25 
colorDefult='black'
bg_colorDefult='yellow'
stroke_colorDefult = "green"
stroke_widthDefult = 2

fontMarked="DejaVu Mono Sans"
fontsizeMarked=25
colorMarked='black'
bg_colorMarked='yellow'
stroke_colorMarked = "red"
stroke_widthMarked = 4


import sqlite3
import random
import string
import time
import secrets
import numpy as np
import math
import json




connection = sqlite3.connect('your_database.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE TKCuts")
connection.commit()


           

create_table_query = """
CREATE TABLE IF NOT EXISTS TKCuts (
    videoID CHAR(11),  
    channel INT,

    timeOfPost FLOAT,
    embedding INT,

    randomAtribute1 INT,
    randomAtribute2 INT,
    randomAtribute3 INT,


    timeAtPeak FLOAT,
    virality FLOAT,

    data TEXT,

    PRIMARY KEY(videoID)
);
"""

cursor.execute(create_table_query)
connection.commit()


def generate_random_youtube_id():
    return ''.join(secrets.choice(string.ascii_letters + string.digits + '-_') for _ in range(11))


def radnom_channel_power(t):  

    return random.randint(0,t)

def generate_random_record(channel,t):
    record = {
        "videoID": generate_random_youtube_id(),
        "channel": channel,

        "timeOfPost": t,

        "embedding": random.randint(0,30),

        "randomAtribute1": random.randint(0,9),
        "randomAtribute2": random.randint(0,9),
        "randomAtribute3": random.randint(0,9),
            #the highest possible number of views per second
                                        #number to fall at sec  #could take up to 
        "timeAtPeak": np.random.normal(random.randint(0,5),random.randint(1,5)), 
           #the time of a videos relavancy
        "virality": np.random.normal(random.randint(0,32),random.randint(1,5)),
        
        "data": "{}"
    }
    return record


allowedVideos = 40
for i in range(allowedVideos):
    channel=radnom_channel_power(10)
    record = generate_random_record(channel,0)
    insert_query = """
    INSERT INTO TKCuts (
        videoID, channel, timeOfPost, embedding, randomAtribute1, randomAtribute2, randomAtribute3, timeAtPeak, virality, data
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    cursor.execute(insert_query, tuple(record.values()))
    connection.commit()



whatIsGood = 0
# start_time = time.time()
total_views = {}
wait = 0.5
mostViews = ["",0,0]
bestChannel = []
views = []

for t in range(100000):

    cursor.execute("SELECT * FROM TKCuts")
    rows = cursor.fetchall()

    for (videoID, channel, timeOfPost, embedding, randomAtribute1, randomAtribute2, randomAtribute3, timeAtPeak, virality, data) in rows:


        if timeAtPeak <= 0:
            timeAtPeak = 0.000001

        if virality <= 0:
            virality = 0.000001

        views_this_second = np.exp(-(((t-(timeOfPost))*10 - timeAtPeak) ** 2) / (2 * virality ** 2)) * channel
            

        if videoID not in total_views:
            total_views[videoID] = 0


        total_views[videoID] += math.floor(views_this_second)
        # if videoID == rows[0][0]:
            # print(f"videoID:{videoID}, channel:{channel}, timeAtPeak:{round(timeAtPeak,2)}, virality:{round(virality,2)}",  t,"		", math.floor(views_this_second), "		", total_views[videoID])
        

    
        
        data = json.loads(data)
        data[str(t)] = total_views[videoID]
        data = json.dumps(data)
        cursor.execute("UPDATE TKCuts SET data = ? WHERE videoID = ?", (data, videoID))
        connection.commit()








    cursor.execute("SELECT * FROM TKCuts")
    rows = cursor.fetchall()

    
    
    for (videoID, channel, timeOfPost, embedding, randomAtribute1, randomAtribute2, randomAtribute3, timeAtPeak, virality, data) in rows:
        
        data = json.loads(data)
        last_key = list(data.keys())[-1]
        last_value = data[last_key]


        if len(list(data.keys())) > 2:
            otherlast_key = list(data.keys())[-2]
            otherlast_value = data[otherlast_key]
            if last_value-otherlast_value == 0 :
                continueP = False
                for key in list(data.keys()):
                    if data[key] > 0:
                        continueP = True
                        break
                
                if continueP or len(list(data.keys())) > 5: 
                    views.append([channel,last_value])
                    cursor.execute("DELETE FROM TKCuts WHERE videoID = ?", (videoID,))

    if len(views) != 0:
        print(f"avg:{sum([x[0] for x in views])/len(views)}")
        print(f"---------max:{max([x[0] for x in views])}")
        print(f"------------------time:{t}")


    if len(rows) == 0:
        howManyVidsPChan = []
        for view in views:
            howManyVidsPChan.append([view[0],math.floor(view[1]/sum([x[1] for x in views])*35)])

        views = []

        for VidsPChannel in howManyVidsPChan:
            for _ in range(VidsPChannel[1]):

                channel = VidsPChannel[0]
                record = generate_random_record(channel,t)
                insert_query = """
                INSERT INTO TKCuts (
                    videoID, channel, timeOfPost, embedding, randomAtribute1, randomAtribute2, randomAtribute3, timeAtPeak, virality, data
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
                cursor.execute(insert_query, tuple(record.values()))
                connection.commit()

        while len(rows) < 40:
            cursor.execute("SELECT * FROM TKCuts")
            rows = cursor.fetchall()
            channel = radnom_channel_power(t)
            record = generate_random_record(channel,t)
            insert_query = """
            INSERT INTO TKCuts (
                videoID, channel, timeOfPost, embedding, randomAtribute1, randomAtribute2, randomAtribute3, timeAtPeak, virality, data
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_query, tuple(record.values()))
            connection.commit()
    



            


                



cursor.close()
connection.close()
