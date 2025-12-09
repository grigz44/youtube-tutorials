from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.getenv("API_KEY")
VIDEO_ID = "XyCk5v7zOBo"  # Use from previous script

youtube = build("youtube", "v3", developerKey=API_KEY)

request = youtube.commentThreads().list(
    part="snippet",
    videoId=VIDEO_ID,
    maxResults=20,
    textFormat="plainText"
)

response = request.execute()

for item in response.get("items", []):
    top_comment = item["snippet"]["topLevelComment"]["snippet"]
    author = top_comment["authorDisplayName"]
    text = top_comment["textDisplay"]
    print(f"{author}: {text}")
