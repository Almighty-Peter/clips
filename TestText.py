
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/peternyman/Clips/woven-victor-430706-q3-0e3eeca05bbd.json"
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"
os.environ["IMAGEIO_FFPROBE_EXE"] = "/opt/homebrew/bin/ffprobe"


from moviepy.editor import *







maxCharsText = 18  
borderBettewnText = 100
qualityOfVideo=10



# identify -list color
# identify -list font


maxCharsText = 18  
borderBettewnText = 100
qualityOfVideo=10

"""Brasil"""
maxCharsText = 18  
borderBettewnText = 100

fontDefault="PT-Mono-Bold"
fontsizeDefault=7*qualityOfVideo 
colorDefault='green2'
bg_colorDefault='transparent'
stroke_colorDefault = "green"
stroke_widthDefault = 0.5*qualityOfVideo

fontMarked="PT-Mono-Bold"
fontsizeMarked=7*qualityOfVideo
colorMarked='white'
bg_colorMarked='yellow'
stroke_colorMarked = "blue"
stroke_widthMarked = 0.6*qualityOfVideo



"""tiktok kinda"""
maxCharsText = 18  
borderBettewnText = 100

fontDefault="STIXGeneral-BoldItalic"
fontsizeDefault=7*qualityOfVideo 
colorDefault='white'
bg_colorDefault='transparent'
stroke_colorDefault = "Pink"
stroke_widthDefault = 0.5*qualityOfVideo

fontMarked="STIXGeneral-BoldItalic"
fontsizeMarked=7*qualityOfVideo
colorMarked='black'
bg_colorMarked='Pink'
stroke_colorMarked = "white"
stroke_widthMarked = 0.5*qualityOfVideo



"""usa prety cool"""
maxCharsText = 18  
borderBettewnText = 100

fontDefault="Arial-Black"
fontsizeDefault=9*qualityOfVideo 
colorDefault='deepskyblue'
bg_colorDefault='transparent'
stroke_colorDefault = "darkblue"
stroke_widthDefault = 0.7*qualityOfVideo

fontMarked="Arial-Black"
fontsizeMarked=9*qualityOfVideo
colorMarked='red'
bg_colorMarked='lightyellow'
stroke_colorMarked = "darkred"
stroke_widthMarked = 0.7*qualityOfVideo


"""some what cool"""
maxCharsText = 18  
borderBettewnText = 100

fontDefault="Impact"
fontsizeDefault=9*qualityOfVideo 
colorDefault='cyan'
bg_colorDefault='transparent'
stroke_colorDefault = "midnightblue"
stroke_widthDefault = 0.8*qualityOfVideo

fontMarked="Impact"
fontsizeMarked=9*qualityOfVideo
colorMarked='magenta'
bg_colorMarked='palegoldenrod'
stroke_colorMarked = "purple"
stroke_widthMarked = 0.8*qualityOfVideo


"""red and white some what cool"""
maxCharsText = 18  
borderBettewnText = 100

fontDefault="Calibri-Bold"
fontsizeDefault=10*qualityOfVideo 
colorDefault='purple'
bg_colorDefault='transparent'
stroke_colorDefault = "palegoldenrod"
stroke_widthDefault = 0.5*qualityOfVideo

fontMarked="Calibri-BoldItalic"
fontsizeMarked=10*qualityOfVideo
colorMarked='palegoldenrod'
bg_colorMarked='black'
stroke_colorMarked = "DarkRed"
stroke_widthMarked = 0.5*qualityOfVideo


"""Neon Glow"""
maxCharsText = 14  
borderBettewnText = 100

fontDefault="Verdana"
fontsizeDefault=9*qualityOfVideo 
colorDefault='limegreen'
bg_colorDefault='transparent'
stroke_colorDefault = "black"
stroke_widthDefault = 0.5*qualityOfVideo

fontMarked="Verdana-Bold"
fontsizeMarked=9*qualityOfVideo
colorMarked='aqua'
bg_colorMarked='darkslategray'
stroke_colorMarked = "cyan"
stroke_widthMarked = 0.6*qualityOfVideo


frame_width = 108*qualityOfVideo
frame_height = 192*qualityOfVideo
frame_rate = 60
duration_seconds = 5.4

# Calculate the total number of frames
total_frames = frame_rate * duration_seconds



clipsOutputPath = f"/Users/peternyman/Clips/Clips/YT=videoIdS=start_timeE=end_time.mp4"
print("clipsOutputPath: "+ clipsOutputPath)


transcript = {0: 'okay', 1: 'in', 2: 'Maybach', 3: 'yep', 4: 'I', 5: 'just', 5.4: 'quick'} #, 5.5: 'question', 5.6: 'about', 5.7: 'that' }#, 5.9: 'bounce', 6.4: 'feature', 6.7: 'yes'} #, 7.1: 'gimmick', 7.6: 'gimmick', 7.9: 'um', 8.5: 'do', 9.0: 'you', 9.1: 'people', 9.3: 'have', 9.6: 'naughty', 10.4: 'things', 10.6: 'with', 10.9: 'it', 11.1: 'because', 11.7: 'it', 11.8: 'has', 12.0: 'that', 12.1: 'Vibe', 12.6: 'and', 12.7: 'I', 12.9: 'posted', 13.1: 'it', 13.5: 'more', 13.6: 'than', 13.8: 'gay', 14.0: 'stuff'}
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
        
        
        # Determine duration by looking at the next word's timestamp
        if i < len(chunkSave) - 1:
            next_timestamp = chunkSave[i + 1][0]
        else:
            next_timestamp = transcript_list[0][0] if transcript_list else timestampI

        durationI = next_timestamp - timestampI
    
        word_clips = []



        for j, (timestampJ, wordJ) in enumerate(chunkSave):
            space_clip = TextClip(" ",font=fontDefault, fontsize=fontsizeDefault, color=colorDefault,bg_color=bg_colorDefault,stroke_color=stroke_colorDefault,stroke_width=stroke_widthDefault).set_start(timestampI).set_duration(durationI)    
            
            if timestampJ == timestampI:
                word_clip = TextClip(wordJ.upper(),font=fontMarked, fontsize=fontsizeMarked, color=colorMarked,bg_color=bg_colorMarked,stroke_color=stroke_colorMarked,stroke_width=stroke_widthMarked).set_start(timestampI).set_duration(durationI)
            else:
                word_clip = TextClip(wordJ,font=fontDefault, fontsize=fontsizeDefault, color=colorDefault,bg_color=bg_colorDefault,stroke_color=stroke_colorDefault,stroke_width=stroke_widthDefault).set_start(timestampI).set_duration(durationI)
            
            word_clips.append(word_clip)
            word_clips.append(space_clip)


        cumulative_width = 0
        cumulative_height = 0
        line_height = max([clip.h for clip in word_clips])
        
        positioned_clips = []

        for clip in word_clips:
            if cumulative_width + clip.w > frame_width-borderBettewnText:
                cumulative_width = 0
                cumulative_height += line_height  # Move to the next line
            positioned_clips.append(clip.set_position((cumulative_width, cumulative_height)))
            cumulative_width += clip.w

        # Calculate the final dimensions
        final_width = frame_width-borderBettewnText
        final_height = cumulative_height + line_height

        # Create the final composite video clip
        text_clip = CompositeVideoClip(positioned_clips, size=(final_width, final_height)).set_position("center")
        text_clips.append(text_clip)
    transcriptForTiktok.append(totalForTiktok)



final_composite_clip = CompositeVideoClip(text_clips, size=(frame_width, frame_height))
final_composite_clip.write_videofile(clipsOutputPath, fps=frame_rate, codec='libx264', audio_codec='aac', verbose=True, logger='bar')
