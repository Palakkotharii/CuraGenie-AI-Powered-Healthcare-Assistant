def create_calendar_event(title, date, time):
    try:
        # Simulate creating event (actual Google Calendar API needs OAuth setup, skip for now)
        return f"Event '{title}' scheduled on {date} at {time} successfully!"
    except Exception as e:
        return f"Failed to create event: {str(e)}"
