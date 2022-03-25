from gtts import gTTS


tts = gTTS("Hello, my name is Ayoub Allali",lang='en')

tts.save('audio.mp3')
