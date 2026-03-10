import time
import requests as req
from bs4 import BeautifulSoup as bs
import json
from plyer import notification
import threading
import sys
import os 
from pathlib import Path

headers = {'User-Agent': 'Mozilla/5.0'}

def send_alert(streamer, online):
    notification.notify(
        title="koyakonsta's Twitch utils",
        message=f"{streamer} is {'Live' if online else 'Offline'}",
        app_name=f"graggle_{streamer}{online}", # Unique app_name helps trigger stacking
        app_icon=f"{streamer}.ico",
        timeout=10
    )


def getstatus(name):
    url=f"https://twitch.tv/{name}"
    response = bs(req.get(url, headers=headers).text, 'html.parser')
    streamer = json.loads(getattr(response.find('script', type='application/ld+json'), 'string', '{}'))
    isLive = streamer.get('@graph', [{}])[0].get('publication', {}).get('isLiveBroadcast', False)
    return isLive



if len(sys.argv) > 1:
    for entry in sys.argv[1:]:
        name = Path(entry).stem
        send_alert(name, getstatus(name))
        # time.sleep(2)
else:
    for name in open('streamers.txt', 'r').readlines(): 
        name=name.strip()
        threading.Thread(target=send_alert, args=(name, getstatus(name))).start()
    input('Enter to exit')