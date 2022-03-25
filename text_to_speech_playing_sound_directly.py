from gtts import gTTS
import os
import playsound

tts = gTTS("Hello, my name is Ayoub Allali",lang='en')

tts.save('audio.mp3')

playsound.playsound('audio.mp3')

os.remove('audio.mp3')
