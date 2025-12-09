from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.getenv("API_KEY")

def get_uploads_playlist_id(youtube, channel_id):
    channel_response = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    ).execute()

    items = channel_response.get("items", [])
    if not items:
        raise Exception("Channel not found or no contentDetails available.")

    uploads_playlist_id = items[0]["contentDetails"]["relatedPlaylists"]["uploads"]
    return uploads_playlist_id

def get_all_videos_from_playlist(youtube, playlist_id):
    videos = []
    next_page_token = None

    while True:
        pl_request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )

        pl_response = pl_request.execute()

        for item in pl_response.get("items", []):
            title = item["snippet"]["title"]
            video_id = item["contentDetails"]["videoId"]
            url = f"https://www.youtube.com/watch?v={video_id}"
            videos.append((title, url))

        next_page_token = pl_response.get("nextPageToken")
        if not next_page_token:
            break

    return videos

def main():
    youtube = build("youtube", "v3", developerKey=API_KEY)

    # Example: Google Developers channel
    channel_id = "UC0-0a1sFFZ_eVPy-Q0rCoMA"

    uploads_playlist_id = get_uploads_playlist_id(youtube, channel_id)
    print("Uploads playlist:", uploads_playlist_id)

    videos = get_all_videos_from_playlist(youtube, uploads_playlist_id)

    print(f"Total videos found: {len(videos)}")
    with open("channel_videos.txt", "w", encoding="utf-8") as f:
        for title, url in videos:
            f.write(f"{title} | {url}\n")

    print("Saved to channel_videos.txt")

if __name__ == "__main__":
    main()


