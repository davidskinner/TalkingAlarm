from gtts import gTTS
from subprocess import *
import time
from mutagen.mp3 import MP3


from datetime import date, datetime
today = date.today()
print("Today's date:", today)

goodmorning = "Good morning, the date is: " + datetime.now().strftime("%A-%b-%d (%I:%M%p)")
mp3File = '/Users/davidskinner/Desktop/hello.mp3'

tts = gTTS(goodmorning, 'en')
tts.save(mp3File)

audio = MP3(mp3File)
audioLength = audio.info.length
print("run length is: " + str(audioLength))

p = Popen(["vlc", '-I dummy', mp3File])
time.sleep(audioLength)
print('p = ', p.pid)
Popen.kill(p)


