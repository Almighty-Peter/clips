sizeOfCaptionstoGptSEC = 22
distanceFromStarEndSEC = 30
distanceFromClipsSEC = 10000000
retentionThreshold = 160 # lower better

startClipBeforeSEC = 3
startClipAfterSEC = 1
getDataFromWeb = True

maxCharsText = 20


from YouTubeAudienceRetention import getYoutubeAudienceRetention
from YoutubeCaptions import getYoutubeCaptions
from ChatGpt import textToText
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/peternyman/Downloads/woven-victor-430706-q3-0e3eeca05bbd.json"
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

from moviepy.editor import *
from moviepy.config import change_settings


# Ensure ImageMagick path is correctly set
change_settings({"IMAGEMAGICK_BINARY": "/opt/homebrew/bin/convert"})

import cv2
import numpy as np




def main(videoId):
    audienceRetentionData = getYoutubeAudienceRetention(videoId)
    getYoutubeCaptions(videoId)
    yt = YouTube(f'https://www.youtube.com/watch?v={videoId}')
    length = yt.length  
    
    
    lowAudienceRetentionData = []
    
     
    while True:
        smallest = [0,300]  
        for i,[percent,retention] in enumerate(audienceRetentionData):
            if getDataFromWeb:
                seconds = (percent/1000)*length
            else:
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
    
    timeStamps = []
    for caption in captions:
        
        prompt = f"Identify the central theme or idea in the following text that would be the most viral, and provide the start and end times in the format: [start_time, end_time].\n\n{caption}"
        pattern = r"\b\d+\.\d+\b"
        result = textToText(prompt,system_message)
        print(result)
        timestamps = [round(float(timestamp)) for timestamp in re.findall(pattern, result)]
        print([timestamps[-2],timestamps[-1]])
        timeStamps.append(([timestamps[-2],timestamps[-1]]))
    
    print("timeStamps:",timeStamps)
    
    
    
    os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"
    
    
    download_path = "/Users/peternyman/Downloads"
    
    def download_video():
    
        url = f'https://www.youtube.com/watch?v={videoId}'
        
        ydl_opts = {
            'format': 'bestvideo[vcodec=h264]+bestaudio[acodec=aac]/best',  # Specify H.264 and AAC codecs
            'outtmpl': f'{download_path}/{videoId}.%(ext)s',  # Output template
            'merge_output_format': 'mp4',  # Ensure the final format is mp4
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    
    def audio_to_text():
        # Convert MP3 to WAV and ensure it's mono
        audio = AudioSegment.from_mp3(f"{download_path}/{videoId}.mp3")
        audio = audio.set_channels(1)  # Set to mono
        audio.export(f"{download_path}/{videoId}.wav", format="wav")

        client = speech.SpeechClient()

        with io.open(f"{download_path}/{videoId}.wav", 'rb') as audio_file:
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
                start_time_seconds = start_time.seconds + start_time.nanos * 1e-9
                transcript[start_time_seconds] = word
        
        return transcript
        
        
    def split_transcript_into_chunks(transcript, max_size):
        words = list(transcript.values())
        timestamps = list(transcript.keys())
        
        chunks = {}
        current_chunk = []
        current_start_time = timestamps[0]

        for i, word in enumerate(words):
            if sum(len(w) for w in current_chunk) + len(word) + len(current_chunk) <= max_size:
                current_chunk.append(word)
            else:
                chunks[current_start_time] = ' '.join(current_chunk)
                current_chunk = [word]
                current_start_time = timestamps[i]
        
        if current_chunk:
            chunks[current_start_time] = ' '.join(current_chunk)

        return chunks

    
    # Function to generate a random color
    def get_random_color():
        return (random.random(), random.random(), random.random())
    
    def create_plot(video_id, audience_retention_data, time_stamps):
        temp = []
        for [percent, retention] in audience_retention_data:
            seconds = (percent / 1000) * length
            temp.append([seconds, retention])
    
        x_values = [pair[0] for pair in temp]
        y_values = [pair[1] for pair in temp]
    
        plt.figure(figsize=(10, 6), dpi=200)
        plt.plot(x_values, y_values, marker='o', linestyle='-')
    
        plt.ylabel('Audience Retention')
        plt.xlabel('Seconds')
        plt.title(f'YT={video_id} S={time_stamps[0]} E={time_stamps[1]}')
    
        plt.legend([
            f'Size of captions sent to GPT SEC = {sizeOfCaptionstoGptSEC}\nDistance from start and end SEC = {distanceFromStarEndSEC}\nDistance from clips SEC = {distanceFromClipsSEC}\nRetention threshold = {retentionThreshold}\nStart clip before SEC = {startClipBeforeSEC}\nStart clip after SEC = {startClipAfterSEC}\nget data from web = {getDataFromWeb}'
        ], loc='upper right')
        plt.grid(True)
    
    
        color = get_random_color()
        plt.axvline(x=time_stamps[0], color=color, linestyle='-', linewidth=2)
        plt.axvline(x=time_stamps[1], color=color, linestyle='-', linewidth=2)
        
        plot_path = "plot.png"
        plt.savefig(plot_path)
        plt.close()
        return plot_path
    
    
    def clip(start_time, end_time, plot_image_path):
    
        output_path = f"{download_path}/{videoId}S{start_time}E{end_time}.mp4"
        
        # Define the video properties
        test=4
        frame_width = 108*test
        frame_height = 192*test
        frame_rate = 60
        duration_seconds = end_time - start_time
        
        # Calculate the total number of frames
        total_frames = frame_rate * duration_seconds
        
        # Create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define the codec
        out = cv2.VideoWriter(output_path, fourcc, frame_rate, (frame_width, frame_height))
        
        # Create a black frame
        black_frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
        
        # Write the black frames to the video file
        for _ in range(total_frames):
            out.write(black_frame)
        
        # Release the VideoWriter object
        out.release()
        
        # Load and resize the content clip
        content_clip = VideoFileClip(f"{download_path}/{videoId}.mp4").subclip(start_time, end_time)
        audio = content_clip.audio
    
        audio.write_audiofile(f"{download_path}/{videoId}.mp3")
        

        
        # Calculate new heights for content and plot to fit within the total frame height
        content_height = int(frame_height * 0.5)
        plot_height = frame_height - frame_height * 0.6
        
        # Resize the content clip to fit the new height while maintaining aspect ratio
        content_clip = content_clip.resize(height=content_height)
        
        # Convert the plot image to a video clip, resize it to fit the new height while maintaining aspect ratio
        plot_clip = ImageClip(plot_image_path).set_duration(duration_seconds)
        plot_clip = plot_clip.resize(height=plot_height)
        
        # Combine the content and plot clips
        composite_clip = CompositeVideoClip([
            content_clip.set_position(('center', 'top')),
            plot_clip.set_position(('center', 'bottom'))
        ], size=(frame_width, frame_height))
        
        



        transcript = audio_to_text()
        transcriptChunk = split_transcript_into_chunks(transcript, maxCharsText)
        
        
        
        
        
        # Create TextClips for each chunk
        text_clips = []
        
        # Sort the keys to ensure the correct order
        sorted_chunk_times = sorted(transcriptChunk.keys())
        
        for i, start_time in enumerate(sorted_chunk_times):
            text = transcriptChunk[start_time]
            # Determine the duration of the TextClip
            if i < len(sorted_chunk_times) - 1:
                end_time = sorted_chunk_times[i + 1]  # Use sorted keys to get the next time
            else:
                end_time = composite_clip.duration  # Use the duration of the composite clip for the last chunk
        
            duration = end_time - start_time
            text_clip = TextClip(text, fontsize=24, color='white').set_position('center').set_start(start_time).set_duration(duration)
            text_clips.append(text_clip)
        
        # Combine the text clips with the original composite_clip
        final_clips = [composite_clip] + text_clips
        final_composite_clip = CompositeVideoClip(final_clips, size=(frame_width, frame_height))
        
        
        
        
        
        # Add audio to the final composite clip
        audio_clip = AudioFileClip(f"{download_path}/{videoId}.mp3")
        
        if audio_clip.duration > final_composite_clip.duration:
            print("Trimming audio to match video duration.")
            audio_clip = audio_clip.subclip(0, final_composite_clip.duration)
        
        final_composite_clip = final_composite_clip.set_audio(audio_clip)
        
        # Write the final video to file
        final_composite_clip.write_videofile(output_path, fps=frame_rate, codec='libx264', audio_codec='aac', verbose=True, logger='bar')
                    
        
        
            
    download_video()
    video = VideoFileClip(download_path+"/"+videoId+".mp4")
    for i,timeStamp in enumerate(timeStamps):
        timeStamps[i] = [timeStamp[0]-startClipBeforeSEC,timeStamp[1]+startClipAfterSEC]
    
    for timeStamp in timeStamps:
        plot_image_path = create_plot(videoId, audienceRetentionData, timeStamp)
        clip(timeStamp[0], timeStamp[1], plot_image_path)
    
    os.remove(download_path+"/"+videoId+".mp4")

    
    
    
main("CaFxF2uDsw0")  
    
    
