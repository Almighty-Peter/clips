# import yt_dlp
# # URL of the YouTube video
# # videoIds = ["orVonJwofD8", "7XhhOVGF8sg", "-yPjP85CbQE", "G4zsPjmfhs0", "o-YM8mCG7Co", "biF1uCiCPBs", "kPRA0W1kECg", "ORyn0Zm3oeM", "X_OXRy9qjP4", "9QdunUVPfn4", "fxZDK5an7ig
# # videoIds = ["vlJsiZFh1OQ", "ZlJd47w7Pbk", "eOt1HLXNRFE"]
# # G_iFEPg2aDA == 3FL5HvdHTR4 > fxZDK5an7ig > Nei2pTuF-tY
# # 10m fxZDK5an7ig
# # 15m G_iFEPg2aDA
# # 19m 3FL5HvdHTR4 
# # 3m  Nei2pTuF-tY
# # Output directory
# download_path = "/Users/peternyman/Clips/BrainRoot/"

# def download_video(videoId):

#     url = f'https://www.youtube.com/watch?v={videoId}'
    
#     ydl_opts = {
#         'format': 'bestvideo+bestaudio',  # Specify H.264 and AAC codecs
#         'outtmpl': f'{download_path}{videoId}.%(ext)s',  # Output template
#         'merge_output_format': 'mp4',  # Ensure the final format is mp4
#     }
    
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])



# for videoId in videoIds:
#     download_video(videoId)

from moviepy.editor import VideoFileClip, vfx
import os


video_path = '/Users/peternyman/Clips/BrainRoot/aw_zjI9ouLU.mp4'


clip = VideoFileClip(video_path)


faster_clip = clip.fx(vfx.speedx, 2) 


temp_path = 'temp_video.mp4'
faster_clip.write_videofile(temp_path, codec='libx264')


clip.close()
faster_clip.close()


os.remove(video_path)


os.rename(temp_path, video_path)

print("The video has been successfully sped up and replaced.")
