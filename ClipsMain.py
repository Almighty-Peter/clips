sizeOfCaptionstoGptSEC = 22
distanceFromStarEndSEC = 30
distanceFromClipsSEC = 20


getManyInstedOfThreshold = True
retentionThreshold = 60 # lower better

startClipBeforeSEC = 3
startClipAfterSEC = 1
qualityOfVideo=8 # a multiple of 108 and 192 as this is 1/10 of 1080 by 1920 the frame of tiktok




from YouTubeAudienceRetention import getYoutubeAudienceRetention
from YoutubeCaptions import getYoutubeCaptions
# from AutoPostTikTok import TikTokUpload
from ChatGpt import textToText, get_embedding
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/peternyman/Clips/woven-victor-430706-q3-0e3eeca05bbd.json"
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"
os.environ["IMAGEIO_FFPROBE_EXE"] = "/opt/homebrew/bin/ffprobe"
from pytube import YouTube
from pydub import AudioSegment
from google.cloud import speech_v1p1beta1 as speech
import io
import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
import re
import matplotlib.pyplot as plt
import random
import platform
import math


from moviepy.editor import *
from moviepy.config import change_settings


# Ensure ImageMagick path is correctly set
change_settings({"IMAGEMAGICK_BINARY": "/opt/homebrew/bin/convert"})
change_settings({"IMAGEMAGICK_BINARY": "/opt/homebrew/bin/magick"})

import cv2
import array
import numpy as np
import sqlite3
from datetime import datetime


connection = sqlite3.connect('local_database.db')
cursor = connection.cursor()




create_table_query = """
CREATE TABLE IF NOT EXISTS TKCuts (
    videoId CHAR(11),  
    channel TEXT,
    start_time INT,
    end_time INT,
    event_date TEXT,
    embedding BLOB,
    caption TEXT,
    TKLink TEXT,
    brainRoot CHAR(11),
    brainRoot_startTime INT,
    brainRoot_endTime INT,

    sizeOfCaptionstoGptSEC INT,
    distanceFromStarEndSEC INT,
    distanceFromClipsSEC INT,

    getHowMany INT,
    getManyInstedOfThreshold BOOLEAN,
    retentionThreshold INT,

    startClipBeforeSEC INT,
    startClipAfterSEC INT,
    qualityOfVideo INT,

    borderBettewnText INT,
    maxCharsText INT,

    fontDefault TEXT,
    fontsizeDefault INT,
    colorDefault TEXT,
    stroke_colorDefault TEXT,
    stroke_widthDefault INT,

    fontMarked TEXT,
    fontsizeMarked INT,
    colorMarked TEXT,
    bg_colorMarked TEXT,
    stroke_colorMarked TEXT,
    stroke_widthMarked INT, 

    whatCaptalazation INT,
    

    PRIMARY KEY(videoId, start_time, end_time)
);
"""

cursor.execute(create_table_query)
connection.commit()

system = platform.system()
if system == "Darwin":  # macOS
    download_path = "/Users/peternyman/Downloads/"
elif system == "Windows":  # Windows
    download_path = "C:\\Users\\YourUsername\\Downloads\\"






def main(videoId, yt):



    channel, audienceRetentionData = getYoutubeAudienceRetention(videoId)
    print(channel)
    getYoutubeCaptions(videoId)
    length = yt.length  
    getHowMany = math.floor(length/120)

    if getHowMany > 9:
        getHowMany = 9

    
    lowAudienceRetentionData = []
    
     
    while True:
        smallest = [0,1000]  
        for i, retention in enumerate(audienceRetentionData):
            seconds = length * ((i+1)/len(audienceRetentionData))
            print(seconds)

            if seconds > distanceFromStarEndSEC and seconds < length-distanceFromStarEndSEC:
                if smallest[1] > retention:
                    # checks if there are any close 
                    addData = True
                    for data in lowAudienceRetentionData:
                        if abs(data - seconds) < distanceFromClipsSEC:
                            addData = False
                            break
                    if addData:
                        smallest = [seconds,retention]
        
        if getManyInstedOfThreshold:
            if smallest[1] == 1000:
                break
            elif len(lowAudienceRetentionData) >= getHowMany:
                break
            else:
                lowAudienceRetentionData.append(smallest[0])
                print(f'retention:{smallest[1]}')
        else:
            if smallest[1] < retentionThreshold:
                lowAudienceRetentionData.append(smallest[0])
                print(f'retention:{smallest[1]}')
            else:
                break
                
        
    
    
    lowAudienceRetentionCaptions = []
    transcript = YouTubeTranscriptApi.get_transcript(videoId)
    
    for timeStamps in lowAudienceRetentionData:
        lowAudienceRetentionCaptions.append([])
        for entry in transcript:
                if abs(entry['start'] - timeStamps) < sizeOfCaptionstoGptSEC:
                    print(entry['start'])
                    lowAudienceRetentionCaptions[len(lowAudienceRetentionCaptions)-1].append([entry['start'],entry['text']])
     
    captions = []
    for data in lowAudienceRetentionCaptions:
        currentMemory = ""
        for start, text in data:
            currentMemory += f'Start Time: {start}, Caption: {text}\n'
        captions.append(currentMemory)
    
        
        
    system_message = """You will receive a text with start times and captions. Your task is to identify the central theme or idea of the text that would be the most viral and provide the start and end times in the format: [start_time, end_time]. Use the provided data format and times to ensure consistency.
    
    For example, given the following data:
    
    Start Time: 23.121, Caption: jet. But here's the thing, I don't care about all that. Scroll down the page, and
    Start Time: 27.426, Caption: you'll find that there are true gourmet meals on board, and if I'm going to spend $30,000 on
    Start Time: 30.49, Caption: a plane ticket just to get the food, I'm going to get my money's worth.   But I think
    Start Time: 34.722, Caption: that's achievable because I see that you can order whatever you want, whenever you
    Start Time: 37.624, Caption: want. And because this is what they call a long-haul flight, check out how insane
    Start Time: 41.217, Caption: this sample menu is. This menu is almost as long as the Cheesecake Factory menu.
    Start Time: 44.847, Caption: Before we take flight, I'll remind you that we are catching up to Gordon, and I
    Start Time: 48.548, Caption: know that half of you watching aren't subscribed, so go hit that button below to
    Start Time: 51.632, Caption: help us catch Gordon. Enough talking, it's time to fly. To begin our journey, Emirates
    Start Time: 56.734, Caption: sent a car to pick me up and bring me to the airport. It even had these fancy lights
    
    The most viral central theme or idea might be about the gourmet meals on board and the luxurious experience, starting from 27.426 to 41.217. Thus, the output should be:
    
    [27.426, 41.217]
    
    Please proceed with the provided data."""
    

    # TODO: check if what chatgpt says actualy happens
    timeStamps = []
    for caption in captions:
        
        prompt = f"Identify the central theme or idea in the following text that would be the most viral, and provide the start and end times in the format: [start_time, end_time].\n\n{caption}"
        pattern = r"\b\d+\.\d+\b"
        result = textToText(prompt,system_message)
        print(f"--------------------------------------------------------system_message--------------------------------------------------------\n\n{system_message}\n\n--------------------------------------------------------prompt--------------------------------------------------------\n\n{prompt}\n\n--------------------------------------------------------result--------------------------------------------------------\n\n{result}\n\n----------------------------------------------------------------------------------------------------------------")
        timestamps = [round(float(timestamp)) for timestamp in re.findall(pattern, result)]
        print([timestamps[-2],timestamps[-1]])
        # here must fix so that if it dosent append any it should automaticly be the first and the last --> An error occurred: list index out of range 
        timeStamps.append(([timestamps[-2],timestamps[-1]]))
    
    print("timeStamps:",timeStamps)
    
    
    def download_video():
    
        url = f'https://www.youtube.com/watch?v={videoId}'
        
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # More flexible format selection
            'outtmpl': f'{download_path}{videoId}.%(ext)s',
            'merge_output_format': 'mp4',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])


    
    def audio_to_text():
        # Convert MP3 to WAV and ensure it's mono
        audio = AudioSegment.from_mp3(f"{download_path}{videoId}.mp3")
        audio = audio.set_channels(1)  # Set to mono
        audio.export(f"{download_path}{videoId}.wav", format="wav")

        client = speech.SpeechClient()

        with io.open(f"{download_path}{videoId}.wav", 'rb') as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,  # Match the sample rate of the WAV file
            language_code='en-US',
            enable_word_time_offsets=True
        )

        response = client.recognize(config=config, audio=audio)

        transcript = {}

        for result in response.results:
            alternative = result.alternatives[0]
            for word_info in alternative.words:
                word = word_info.word
                start_time = word_info.start_time
                # start_time_seconds = start_time.seconds + start_time.nanos * 1e-9
                start_time_seconds = start_time.total_seconds()
                transcript[start_time_seconds] = word
        
        return transcript
        

    # Function to generate a random color
    # def get_random_color():
    #     return (random.random(), random.random(), random.random())
    
    # def create_plot(video_id, audience_retention_data, time_stamps):
    #     temp = []
    #     for [percent, retention] in audience_retention_data:
    #         seconds = (percent / 1000) * length
    #         temp.append([seconds, retention])
    
    #     x_values = [pair[0] for pair in temp]
    #     y_values = [pair[1] for pair in temp]
    
    #     plt.figure(figsize=(10, 6), dpi=200)
    #     plt.plot(x_values, y_values, marker='o', linestyle='-')
    
    #     plt.ylabel('Audience Retention')
    #     plt.xlabel('Seconds')
    #     plt.title(f'YT={video_id} S={time_stamps[0]} E={time_stamps[1]}')
    
    #     plt.legend([
    #         f'Size of captions sent to GPT SEC = {sizeOfCaptionstoGptSEC}\nDistance from start and end SEC = {distanceFromStarEndSEC}\nDistance from clips SEC = {distanceFromClipsSEC}\nRetention threshold = {retentionThreshold}\nStart clip before SEC = {startClipBeforeSEC}\nStart clip after SEC = {startClipAfterSEC}\nget data from web = {getDataFromWeb}'
    #     ], loc='upper right')
    #     plt.grid(True)
    
    
    #     color = get_random_color()
    #     plt.axvline(x=time_stamps[0], color=color, linestyle='-', linewidth=2)
    #     plt.axvline(x=time_stamps[1], color=color, linestyle='-', linewidth=2)
        
    #     plot_path = "plot.png"
    #     plt.savefig(plot_path)
    #     plt.close()
    #     return plot_path
    
    
    def clip(start_time, end_time):

        rand = random.randint(0,6)
        if rand == 0:
            """Brasil"""
            maxCharsText = 18  
            borderBettewnText = 100

            fontDefault="PT-Mono-Bold"
            fontsizeDefault=7*qualityOfVideo 
            colorDefault='green2'
            stroke_colorDefault = "green"
            stroke_widthDefault = 0.5*qualityOfVideo

            fontMarked="PT-Mono-Bold"
            fontsizeMarked=7*qualityOfVideo
            colorMarked='white'
            bg_colorMarked='yellow'
            stroke_colorMarked = "blue"
            stroke_widthMarked = 0.6*qualityOfVideo


        elif rand == 1:
            """tiktok kinda"""
            maxCharsText = 18  
            borderBettewnText = 100

            fontDefault="STIXGeneral-BoldItalic"
            fontsizeDefault=7*qualityOfVideo 
            colorDefault='white'
            stroke_colorDefault = "Pink"
            stroke_widthDefault = 0.5*qualityOfVideo

            fontMarked="STIXGeneral-BoldItalic"
            fontsizeMarked=7*qualityOfVideo
            colorMarked='black'
            bg_colorMarked='Pink'
            stroke_colorMarked = "white"
            stroke_widthMarked = 0.5*qualityOfVideo


        elif rand == 2:
            """usa prety cool"""
            maxCharsText = 18  
            borderBettewnText = 100

            fontDefault="Arial-Black"
            fontsizeDefault=9*qualityOfVideo 
            colorDefault='deepskyblue'
            stroke_colorDefault = "darkblue"
            stroke_widthDefault = 0.7*qualityOfVideo

            fontMarked="Arial-Black"
            fontsizeMarked=9*qualityOfVideo
            colorMarked='red'
            bg_colorMarked='lightyellow'
            stroke_colorMarked = "darkred"
            stroke_widthMarked = 0.7*qualityOfVideo

        elif rand == 3:
            """some what cool"""
            maxCharsText = 18  
            borderBettewnText = 100

            fontDefault="Impact"
            fontsizeDefault=9*qualityOfVideo 
            colorDefault='cyan'
            stroke_colorDefault = "midnightblue"
            stroke_widthDefault = 0.8*qualityOfVideo

            fontMarked="Impact"
            fontsizeMarked=9*qualityOfVideo
            colorMarked='magenta'
            bg_colorMarked='palegoldenrod'
            stroke_colorMarked = "purple"
            stroke_widthMarked = 0.8*qualityOfVideo

        elif rand == 4:
            """red and white some what cool"""
            maxCharsText = 18  
            borderBettewnText = 100

            fontDefault="Calibri-Bold"
            fontsizeDefault=10*qualityOfVideo 
            colorDefault='purple'

            stroke_colorDefault = "palegoldenrod"
            stroke_widthDefault = 0.5*qualityOfVideo

            fontMarked="Calibri-BoldItalic"
            fontsizeMarked=10*qualityOfVideo
            colorMarked='palegoldenrod'
            bg_colorMarked='black'
            stroke_colorMarked = "DarkRed"
            stroke_widthMarked = 0.5*qualityOfVideo

        elif rand == 5:
            """Neon Glow"""
            maxCharsText = 14  
            borderBettewnText = 100

            fontDefault="Verdana"
            fontsizeDefault=9*qualityOfVideo 
            colorDefault='limegreen'
            stroke_colorDefault = "black"
            stroke_widthDefault = 0.5*qualityOfVideo

            fontMarked="Verdana-Bold"
            fontsizeMarked=9*qualityOfVideo
            colorMarked='aqua'
            bg_colorMarked='darkslategray'
            stroke_colorMarked = "cyan"
            stroke_widthMarked = 0.6*qualityOfVideo

        elif rand == 6:
            """Neon Glow"""
            maxCharsText = 14  
            borderBettewnText = 100

            fontDefault="Verdana"
            fontsizeDefault=9*qualityOfVideo 
            colorDefault='LightPink'
            stroke_colorDefault = "HotPink"
            stroke_widthDefault = 0.5*qualityOfVideo

            fontMarked="Verdana-Bold"
            fontsizeMarked=9*qualityOfVideo
            colorMarked='aqua'
            bg_colorMarked='darkslategray'
            stroke_colorMarked = "cyan"
            stroke_widthMarked = 0.6*qualityOfVideo
        
        frame_width = 108*qualityOfVideo
        frame_height = 192*qualityOfVideo
        frame_rate = 40
        duration_seconds = end_time - start_time

        
        clipsOutputPath = f"/Users/peternyman/Clips/Clips/YT={videoId}S={start_time}E={end_time}.mp4"
        print("clipsOutputPath: "+ clipsOutputPath)

        content_clip = VideoFileClip(f"{download_path}{videoId}.mp4").subclip(start_time, end_time)
        audio = content_clip.audio
    
        audio.write_audiofile(f"{download_path}{videoId}.mp3")
        
        content_height = int(frame_height * 0.6)
        plot_height = frame_height - content_height

        brainRoot = random.choice([file for file in os.listdir('/Users/peternyman/Clips/BrainRoot') if file.endswith('mp4')])
        brainRootCode = brainRoot[:11]
        print("brainRootCode:",brainRootCode)
        brainRoot = f'/Users/peternyman/Clips/BrainRoot/{brainRoot}'
        print(brainRoot)
        
       
        
        brainRootDuration = math.floor(VideoFileClip(brainRoot).duration)
        
        brainRoot_startTime = random.randrange(0,brainRootDuration-duration_seconds)

        if brainRoot_startTime < 0:
            print(f"ERROR --> you must emedietly delete: {brainRoot}")
        

        plot_clip = VideoFileClip(brainRoot).subclip(brainRoot_startTime, duration_seconds + brainRoot_startTime).resize(height=plot_height)


        content_clip = content_clip.resize(height=content_height)

        composite_clip = CompositeVideoClip([
            content_clip.set_position(('center', 'top')),
            plot_clip.set_position(('center', 'bottom'))
        ], size=(frame_width, frame_height))


        transcript = audio_to_text()
        whatCaptalazation = random.randint(0,2)
        
        text_clips = []
        transcriptForTiktok = []

        while len(transcript) != 0:
            chunkSave = []
            chunk = ""
            transcript_list = sorted(transcript.items())
            for i, (timestamp, word) in enumerate(transcript_list):
                if len(word) + len(chunk) <= maxCharsText + 1:
                    chunk += word + " "
                    del transcript[timestamp]
                    chunkSave.append([timestamp, word])

                else:
                    
                    break
            
            totalForTiktok = ""
            print(f"---------------{chunkSave}----------------")
            star_time = chunkSave[0][0]
            for i, (timestampI, wordI) in enumerate(chunkSave):
                transcript_list.pop(0)
                totalForTiktok += wordI + " "
                
                
                if i < len(chunkSave) - 1:
                    next_timestamp = chunkSave[i + 1][0]
                else:
                    next_timestamp = transcript_list[0][0] if transcript_list else timestampI

                durationI = next_timestamp - timestampI
            
                word_clips = []


                for j, (timestampJ, wordJ) in enumerate(chunkSave):


                    if whatCaptalazation == 1:
                        wordI = wordI.upper()
                    elif whatCaptalazation == 2:
                        wordI = wordI.upper()
                        wordJ = wordJ.upper()
                    space_clip = TextClip(" ",font=fontDefault, fontsize=fontsizeDefault, color=colorDefault,stroke_color=stroke_colorDefault,stroke_width=stroke_widthDefault).set_start(timestampI).set_duration(durationI)    
                    
                    if timestampJ == timestampI:
                        word_clip = TextClip(wordI,font=fontMarked, fontsize=fontsizeMarked, color=colorMarked,bg_color=bg_colorMarked,stroke_color=stroke_colorMarked,stroke_width=stroke_widthMarked).set_start(timestampI).set_duration(durationI)
                    else:
                        word_clip = TextClip(wordJ,font=fontDefault, fontsize=fontsizeDefault, color=colorDefault,stroke_color=stroke_colorDefault,stroke_width=stroke_widthDefault).set_start(timestampI).set_duration(durationI)
                    
                    word_clips.append(word_clip)
                    word_clips.append(space_clip)

                


                cumulative_width = 0
                cumulative_height = 0
                line_height = max([clip.h for clip in word_clips])
                
                positioned_clips = []

                for clip in word_clips:
                    if cumulative_width + clip.w > frame_width-borderBettewnText:
                        cumulative_width = 0
                        cumulative_height += line_height  
                    positioned_clips.append(clip.set_position((cumulative_width, cumulative_height)))
                    cumulative_width += clip.w


                final_width = frame_width-borderBettewnText
                final_height = cumulative_height + line_height


                text_clip = CompositeVideoClip(positioned_clips, size=(final_width, final_height)).set_position("center")
                text_clips.append(text_clip)
            transcriptForTiktok.append(totalForTiktok)
    
        

        final_clips = [composite_clip] + text_clips
        final_composite_clip = CompositeVideoClip(final_clips, size=(frame_width, frame_height))

        
        final_composite_clip = final_composite_clip.set_audio(audio)
        
        final_composite_clip.write_videofile(clipsOutputPath, fps=frame_rate, codec='libx264', audio_codec='aac', verbose=True, logger='bar')
        os.remove(f"{download_path}{videoId}.mp3")
        os.remove(f"{download_path}{videoId}.wav")


        captions = ""
        transcript_list = sorted(transcript.items())
        for chunk in transcriptForTiktok:
            captions += chunk + "\n"
        captions


        
        # - {yt.title}: Title of the video
        prompt = f"""Given the following information:
- {yt.author}: Name of the YouTube channel
- {captions}: Transcript of the video

Create an optimized caption for the video following these guidelines:

1. Align the caption with the video's essence, capturing its core message or theme.

2. Break the caption into short, digestible lines using line breaks for better readability.

3. Use strategic capitalization for emphasis on key words or phrases.

4. Make the caption relatable to the target audience, considering their experiences and emotions.

5. If possible incorporate a brilliant question that encourages viewers to share their opinions and experiences in the comments.

6. Include a strong call-to-action (CTA) that prompts engagement (like, comment, share, or follow).

7. Add 8 relevant hashtags at the end to increase discoverability and reach a broader audience.

Output Format:
```
[Brilliant question]

[Call-to-action]

[10 relevant hashtags]
```
"""

        system_message = """You are an expert social media content creator specializing in crafting engaging and optimized captions for video content. Your task is to create the best possible caption for a given video based on provided information. Your captions should be attention-grabbing, relatable, and designed to maximize engagement and reach."""
        tkCaption = textToText(prompt,system_message)
        print(f"--------------------------------------------------------system_message--------------------------------------------------------\n\n{system_message}\n\n--------------------------------------------------------prompt--------------------------------------------------------\n\n{prompt}\n\n--------------------------------------------------------result--------------------------------------------------------\n\n{tkCaption}\n\n----------------------------------------------------------------------------------------------------------------")
        caption = tkCaption.replace("```", "")



        
        embedding = get_embedding(captions)
        TKLink = "NULL"
        brainRoot = brainRootCode
        brainRoot_endTime = brainRoot_startTime+duration_seconds
        event_date = datetime.now().strftime('%Y-%m-%d')
        embedding_bytes = array.array('d', embedding).tobytes()

        # print(f"videoId:{videoId}, channel{channel}, start_time{start_time}, end_time{end_time}, event_date{event_date}, embedding{embedding}, caption{caption}, TKLink{TKLink}, brainRoot{brainRoot}, brainRoot_startTime{brainRoot_startTime}, brainRoot_endTime{brainRoot_endTime}, sizeOfCaptionstoGptSEC{sizeOfCaptionstoGptSEC}, distanceFromStarEndSEC{distanceFromStarEndSEC}, distanceFromClipsSEC{distanceFromClipsSEC}, getHowMany{getHowMany}, getManyInstedOfThreshold{getManyInstedOfThreshold}, retentionThreshold{retentionThreshold}, startClipBeforeSEC{startClipBeforeSEC}, startClipAfterSEC{startClipAfterSEC}, qualityOfVideo{qualityOfVideo}, borderBettewnText{borderBettewnText}, maxCharsText{maxCharsText}, fontDefault{fontDefault}, fontsizeDefault{fontsizeDefault}, colorDefault{colorDefault}, stroke_colorDefault{stroke_colorDefault}, stroke_widthDefault{stroke_widthDefault}, fontMarked{fontMarked}, fontsizeMarked{fontsizeMarked}, colorMarked{colorMarked}, bg_colorMarked{bg_colorMarked}, stroke_colorMarked{stroke_colorMarked}, stroke_widthMarked{stroke_widthMarked}, whatCaptalazation{whatCaptalazation}")
        cursor.execute('DELETE FROM TKCuts WHERE videoId = ? AND start_time = ? AND end_time = ?', (videoId,start_time,end_time))
        insert_query = """
        INSERT INTO TKCuts (
            videoId, channel, start_time, end_time, event_date, embedding, caption, TKLink, brainRoot, brainRoot_startTime, brainRoot_endTime, sizeOfCaptionstoGptSEC, distanceFromStarEndSEC, distanceFromClipsSEC, getHowMany, getManyInstedOfThreshold, retentionThreshold, startClipBeforeSEC, startClipAfterSEC, qualityOfVideo, borderBettewnText, maxCharsText, fontDefault, fontsizeDefault, colorDefault, stroke_colorDefault, stroke_widthDefault, fontMarked, fontsizeMarked, colorMarked, bg_colorMarked, stroke_colorMarked, stroke_widthMarked, whatCaptalazation
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        cursor.execute(insert_query, (
            videoId, channel, start_time, end_time, event_date, embedding_bytes, caption, TKLink, brainRoot, brainRoot_startTime, brainRoot_endTime, sizeOfCaptionstoGptSEC, distanceFromStarEndSEC, distanceFromClipsSEC, getHowMany, getManyInstedOfThreshold, retentionThreshold, startClipBeforeSEC, startClipAfterSEC, qualityOfVideo, borderBettewnText, maxCharsText, fontDefault, fontsizeDefault, colorDefault, stroke_colorDefault, stroke_widthDefault, fontMarked, fontsizeMarked, colorMarked, bg_colorMarked, stroke_colorMarked, stroke_widthMarked, whatCaptalazation
        ))
        connection.commit()





        
            
    download_video()
    for i,timeStamp in enumerate(timeStamps):

        timeStamps[i] = [timeStamp[0]-startClipBeforeSEC,timeStamp[1]+startClipAfterSEC]
    
    for timeStamp in timeStamps:
        # plot_image_path = create_plot(videoId, audienceRetentionData, timeStamp)
        clip(timeStamp[0], timeStamp[1])
    
    os.remove(download_path+videoId+".mp4")

    
cursor.execute("SELECT * FROM YTVideos ORDER BY RANDOM()")
rows = cursor.fetchall()
for (video_id1, channel1, title1, position_found1, views1, date1, search_query1, data1) in rows:
    if views1 > 100000:
        print("next")
        try:
            print(video_id1)
            yt = YouTube(f'https://www.youtube.com/watch?v={video_id1}')
            if 10800 > yt.length > 120:

                main(video_id1, yt)  
        except Exception as e:
            print(f"An error occurred: {e}")
    
    
    #  RrjEtmeby64 KY_en3cGYVs mtWDLLtxoHY




