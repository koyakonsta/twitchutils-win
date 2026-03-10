import requests as req
from bs4 import BeautifulSoup as bs
import re 
import ffmpeg
import os
import winshell

headers = {'User-Agent': 'Mozilla/5.0'}
script_dir = os.path.dirname(os.path.abspath(__file__))

for name in open('streamers.txt', 'r').readlines():
    name=name.strip()
    url=f"https://twitch.tv/{name}"
    response = bs(req.get(url, headers=headers).text, 'html.parser')
    pfp_url = response.find('meta', property='og:image').get('content')
    if pfp_url:
        ffmpeg.input(pfp_url).filter('scale',64,64).output(f"{name}.ico").overwrite_output().run()
        print(pfp_url)
    if os.path.exists(f"{name}.bat"): os.remove(f"{name}.bat")
    os.link('launchstream.bat', f"{name}.bat")
    with winshell.shortcut(os.path.join(winshell.desktop(), f"{name}.lnk")) as link:
        link.path = os.path.join(script_dir, f"{name}.bat")
        link.working_directory = script_dir
        link.icon_location = (os.path.join(script_dir, f"{name}.ico"), 0)
# input()