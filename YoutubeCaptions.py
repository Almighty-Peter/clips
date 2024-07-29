from youtube_transcript_api import YouTubeTranscriptApi



def getYoutubeCaptions(videoId):

    try:
        transcript = YouTubeTranscriptApi.get_transcript(videoId)
        for entry in transcript:

            return f"{entry['start']} - {entry['duration']}: {entry['text']}"
    except Exception as e:
        print(f"An error occurred: {e}")
        







