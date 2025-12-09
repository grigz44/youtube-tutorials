from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.getenv("API_KEY")
PLAYLIST_ID = "PLBbxMXKrHot74OFEiZv6mQlZT7zNZrraj"  # paste from previous script

youtube = build("youtube", "v3", developerKey=API_KEY)

request = youtube.playlistItems().list(
    part="snippet,contentDetails",
    playlistId=PLAYLIST_ID,
    maxResults=25
)

response = request.execute()

for item in response.get("items", []):
    title = item["snippet"]["title"]
    video_id = item["contentDetails"]["videoId"]
    print(f"{title} - https://www.youtube.com/watch?v={video_id}")
