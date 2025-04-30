import datetime
import os.path
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_real_calendar_event(title, date, time):
    try:
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        start_datetime = datetime.datetime.combine(date, time)
        end_datetime = start_datetime + datetime.timedelta(hours=1)

        event = {
            'summary': title,
            'start': {
                'dateTime': start_datetime.isoformat(),
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'dateTime': end_datetime.isoformat(),
                'timeZone': 'Asia/Kolkata',
            },
        }

        created_event = service.events().insert(calendarId='primary', body=event).execute()
        return f"✅ Real event created: {created_event.get('htmlLink')}"

    except Exception as e:
        return f"❌ Failed to create real event: {str(e)}"
