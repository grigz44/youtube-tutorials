from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret_92563542954-soi0c97925itin88lsi79t09madvibni.apps.googleusercontent.com.json", SCOPES
    )
    creds = flow.run_local_server(port=0)
    return build("youtube", "v3", credentials=creds)

def update_privacy(video_id, status="public"):
    youtube = get_service()

    request = youtube.videos().update(
        part="status",
        body={
            "id": video_id,
            "status": {
                "privacyStatus": status
            }
        }
    )
    response = request.execute()
    print("Updated!", response["status"]["privacyStatus"])

if __name__ == "__main__":
    update_privacy("UbHic8FtDP4", "unlisted")  # or "public" / "private"
