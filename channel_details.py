from googleapiclient.discovery import build

API_KEY = "AIzaSyBBUMpvdZ8kLq7goIKfvPYZqSIxoEALjnM"

youtube = build("youtube", "v3", developerKey=API_KEY)

request = youtube.channels().list(
    part="snippet,statistics",
    id="UC0-0a1sFFZ_eVPy-Q0rCoMA"   # Google Developers channel ID
)

response = request.execute()

print(response)
