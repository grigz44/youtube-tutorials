from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.getenv("API_KEY")

youtube = build("youtube", "v3", developerKey=API_KEY)

def check_channel(channel_id: str):
    try:
        request = youtube.channels().list(
            part="snippet,statistics",
            id=channel_id
        )
        response = request.execute()

        total = response.get("pageInfo", {}).get("totalResults", 0)
        if total == 0:
            print(f"[LOGIC ERROR] No channel found for ID: {channel_id}")
            return

        item = response["items"][0]
        title = item["snippet"]["title"]
        subs = item["statistics"]["subscriberCount"]
        print(f"[OK] Channel found: {title} (subs: {subs})")

    except HttpError as e:
        status = e.resp.status
        print(f"[HTTP ERROR] Status: {status}")
        print(e)

def main():
    print("Testing INVALID ID:")
    check_channel("INVALID_ID_12345")

    print("\nTesting YOUR channel:")
    check_channel("UC0-0a1sFFZ_eVPy-Q0rCoMA")  # your real channel

    print("\nTesting random garbage ID:")
    check_channel("ASDASDASDASDQWERTY")

if __name__ == "__main__":
    main()