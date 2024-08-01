import yt_dlp
# URL of the YouTube video
videoIds = ["3wd9RcZ2fHc"]

# Output directory
download_path = "/Users/peternyman/Clips/BrainRoot/"

def download_video(videoId):

    url = f'https://www.youtube.com/watch?v={videoId}'
    
    ydl_opts = {
        'format': 'bestvideo[vcodec=h264]+bestaudio[acodec=aac]/best',  # Specify H.264 and AAC codecs
        'outtmpl': f'{download_path}{videoId}.%(ext)s',  # Output template
        'merge_output_format': 'mp4',  # Ensure the final format is mp4
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])



for videoId in videoIds:
    download_video(videoId)
