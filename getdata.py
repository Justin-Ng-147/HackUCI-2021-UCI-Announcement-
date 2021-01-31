from ics import Calendar, Event
import datetime
import requests
from bs4 import BeautifulSoup

time = datetime.datetime.utcnow().date()

def get_calendar(url:str) -> Calendar:
    r = requests.get(url)
    if r.status_code != 200:
        print("Error")
        raise AssertionError   
    cal = Calendar(r.text)
    return cal

def get_todays_events(cal:Calendar) -> []:
    list_of_events =[]
    for event in cal.timeline.today():
        list_of_events.append(event)
    return list_of_events

def format_events(events:[]) -> [str]:
    return_list =[]
    for event in events:       
        return_list.append(''.join([str(event.name)+'\n',\
            (str(BeautifulSoup(event.description,'lxml').get_text()+'\n')) if BeautifulSoup(event.description,'lxml').get_text() != None else '',\
                ('Starts at:'+ str(event.begin)+'\n') if event.begin != None else '',\
                    ('Duration: '+str(event.duration)+'\n') if event.duration != None else '',\
                        ('Link: '+str(event.url)+'\n') if event.url!=None else '',\
                            ('Organizer: '+str(event.organizer)+'\n') if event.organizer!=None else '']))
    return return_list

def get(url:str) - > [str]:
    return format_events(get_todays_events(get_calendar(url)))