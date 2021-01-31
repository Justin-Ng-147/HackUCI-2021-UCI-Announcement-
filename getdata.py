from ics import Calendar, Event
from datetime import datetime
import requests
from bs4 import BeautifulSoup



def get_calendar(url:str) -> Calendar:
    '''Returns a Calendar object from an url pointing to a public calendar. Raises AssertionError if status code isn't 200.
    '''
    r = requests.get(url)
    if r.status_code != 200:
        raise AssertionError   
    cal = Calendar(r.text)
    return cal

def get_todays_events(cal:Calendar) -> []:
    '''Returns a list of all events for today from a Calendar object
    '''
    list_of_events =[]
    for event in cal.timeline.today():
        list_of_events.append(event)
    return list_of_events

def format_events(events:[]) -> [str]:
    '''Returns a list of formated string where each element of the list are different events.\n
    If one of the event parameters returns none then it along with any related strings will not show up.
    '''
    return_list =[]
    for event in events:       
        return_list.append(''.join([str(event.name)+'\n',\
            (str(BeautifulSoup(event.description,'lxml').get_text()+'\n')) if BeautifulSoup(event.description,'lxml').get_text() != None else '',\
                #('Starts at: '+ datetime.fromisoformat(str(event.begin)).strftime('%Y-%m-%d %H:%M:%S')+' UTC'+'\n') if event.begin != None else '',\
                 ('Starts at: '+ (str(event.begin))+' UTC'+'\n') if event.begin != None else '',\
                    ('Duration: '+str(event.duration)+'\n') if event.duration != None else '',\
                        ('Link: '+str(event.url)+'\n') if event.url!=None else '',\
                            ('Organizer: '+str(event.organizer)+'\n') if event.organizer!=None else '']))
    return return_list


def get(url:str) -> [str]:
    return format_events(get_todays_events(get_calendar(url)))

#print(get('https://calendar.google.com/calendar/ical/pccd56qth2qfdt3alj9voutbes%40group.calendar.google.com/public/basic.ics')[0])
