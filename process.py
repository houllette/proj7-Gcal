import arrow

def list_events(service, selected_calendars, user_defined_begin_date, user_defined_end_date):
    """
    Given a google 'service' object and list of selected calendars, return a list of
    events from the selected calendars within the submitted date range.
    Each event is represented by a dict.
    """
    page_token = None
    result = [ ]
    for cal_id in selected_calendars:
        while True:
          events_list = service.events().list(calendarId=cal_id, pageToken=page_token, timeMin=user_defined_begin_date, timeMax=user_defined_end_date).execute()
          for event in events_list["items"]:
            if "summary" in event:
                if 'transparency' not in event:
                    if 'description' in event:
                        desc = event['description']
                    else:
                        desc = '(no description)'

                    if 'date' in event['start']:
                        start_date = "ALL DAY"
                    else:
                        start_date = event['start']['dateTime']

                    if 'date' in event['end']:
                        end_date = "ALL DAY"
                    else:
                        end_date = event['end']['dateTime']

                    result.append({
                    'summary': event['summary'],
                    'desc': desc,
                    'start_date': start_date,
                    'end_date': end_date
                    })
          page_token = events_list.get("nextPageToken")
          if not page_token:
            break
    return result

def conflicting_events(events, user_defined_begin_time, user_defined_end_time):
    '''
    Given a list of events, checks against user inputted time frame
    and returns list of events that fall between the requested time frame
    '''
    conflict = [ ]
    for event in events:
        if event['start_date'] == "ALL DAY" or event['end_date'] == "ALL DAY":
            conflict.append(event)
        else:
            event_start = arrow.get(event['start_date'].split('T')[1][0:8], 'HH:mm:ss')
            event_end = arrow.get(event['end_date'].split('T')[1][0:8], 'HH:mm:ss')
            request_start = arrow.get(user_defined_begin_time.split('T')[1][0:8], 'HH:mm:ss')
            request_end = arrow.get(user_defined_end_time.split('T')[1][0:8], 'HH:mm:ss')
            #starts within pre-existing event
            if event_start < request_start and request_start < event_end:
                conflict.append(event)
            #ends within pre-existing event
            elif event_start < request_end and request_end < event_end:
                conflict.append(event)
            #pre-existing event happens within request
            elif request_start < event_start and event_end < request_end:
                conflict.append(event)
    return conflict