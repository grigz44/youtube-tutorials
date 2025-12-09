from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

youtube = build("youtube", "v3", developerKey=API_KEY)

def get_channel_id_from_handle(handle):
    resp = youtube.channels().list(
        part="id,snippet",
        forHandle=handle  # or forHandle="@"+handle
    ).execute()

    items = resp.get("items", [])
    if not items:
        raise Exception("No channel found for handle: " + handle)
    return items[0]["id"], items[0]["snippet"]["title"]

handle = "motovillageriders"
try:
    channel_id, title = get_channel_id_from_handle(handle)
    print("Found channel:", title, "| ID:", channel_id)
except Exception as e:
    print("Error:", e)
