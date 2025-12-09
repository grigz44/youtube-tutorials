from googleapiclient.discovery import build

API_KEY = "AIzaSyBBUMpvdZ8kLq7goIKfvPYZqSIxoEALjnM"

youtube = build("youtube", "v3", developerKey=API_KEY)

CHANNEL_ID = "UC0-0a1sFFZ_eVPy-Q0rCoMA"  # Google Developers (example)

request = youtube.playlists().list(
    part="snippet,contentDetails",
    channelId=CHANNEL_ID,
    maxResults=25
)

response = request.execute()

for item in response.get("items", []):
    title = item["snippet"]["title"]
    playlist_id = item["id"]
    video_count = item["contentDetails"]["itemCount"]
    print(f"{title} ({playlist_id}) - {video_count} videos")

