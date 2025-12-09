import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

# OAuth scope required for uploading
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret_92563542954-soi0c97925itin88lsi79t09madvibni.apps.googleusercontent.com.json", SCOPES
    )
    credentials = flow.run_local_server(port=0)
    return build("youtube", "v3", credentials=credentials)

def upload_video(file_path, title, description, tags=None, category="22"):
    youtube = get_authenticated_service()

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags or ["youtube api", "partner engineer"],
            "categoryId": category
        },
        "status": {
            "privacyStatus": "private"
        }
    }

    media = MediaFileUpload(
        file_path,
        chunksize=-1,
        resumable=True
    )

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Upload progress: {int(status.progress() * 100)}%")

    print("Upload complete!")
    print("Video ID:", response["id"])

if __name__ == "__main__":
    # Change this to your test video path
    file_path = "318654_small.mp4"

    upload_video(
        file_path=file_path,
        title="Test Upload via YouTube API",
        description="Uploaded using YouTube Data API (Partner Engineer training)",
        tags=["api", "training", "upload"]
    )
