# twitchutils
Make streamer desktop shortcuts, check if they're online, watch twitch streams on vlc

## Requirements
- Python ~3.13
- ffmpeg, streamlink and vlc installed and in PATH
- pip install -r requirements.txt

## Usage
- **checklive.py**: check which streamers are online and send out notifications
  - If launched directly reads _streamers.txt_
  - "Open with" any number of streamer shortcuts to check those individual streamers
- **populate.py**:
  - Reads streamers.txt, fetches pfps and creates shortcuts to hardlinks which launch _launchstream.bat_ as the streamer name [streamer].bat
  - By default, the shortcuts are placed on the desktop
- **Streamer shortcuts**
  - Double-click on a shortcut to watch the twitch stream on vlc. If an instance is already running it will rename the window title.
