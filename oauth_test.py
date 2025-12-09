from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

flow = InstalledAppFlow.from_client_secrets_file(
    "client_secret_92563542954-soi0c97925itin88lsi79t09madvibni.apps.googleusercontent.com.json", SCOPES
)
# Some versions of google-auth-oauthlib expose `run_console()` on
# InstalledAppFlow, while others provide `run_local_server()` only.
# Try `run_console()` first for a console-based flow; fall back to
# `run_local_server(open_browser=False)` which prints a URL the user
# can open manually (useful in headless environments).
if hasattr(flow, "run_console"):
    credentials = flow.run_console()
else:
    try:
        credentials = flow.run_local_server(open_browser=False)
    except TypeError:
        # Older/newer signatures may not accept arguments; try without args.
        credentials = flow.run_local_server()
print("Access Token:", credentials.token)
print("Refresh Token:", credentials.refresh_token)
