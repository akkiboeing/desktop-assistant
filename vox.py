from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests

def speak(audio):
	print(audio)
	for line in audio.splitlines():
		os.system("say " + audio)
	
def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
         print('Okay Akshay')
         r.pause_treshold = 1
         r.adjust_for_ambient_noise(source, duration = 1)
         audio = r.listen(source)	

    try:
        command = r.recognize_google(audio).lower()
        print('You said: '+ command + '\n')

    except sr.UnknownValueError:
           speak('Your last instruction was unclear to me')
           command = myCommand();

    return command 
    
def assistant(command):
    
    if 'open reddit' in command:
        wups = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if wups:
           subreddit = wups.group(1)
           url = url + 'r/' + subreddit 
        webbrowser.open(url)
        speak('Done')

    elif 'open youtube' in command:
         wups = re.search('open youtube (.*)', command)
         url = 'https://www.youtube.com/'
         if wups:
         	search_q = wups.group(1)
         	url = url + 'results?search_query=' + search_q
         webbrowser.open(url)
         speak('Done')

    elif 'open website' in command:
         wups = re.search('open website (.+)', command)
         if wups:
            domain = wups.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            speak('Done!')
         else:
            speak('Can\'t find the website') 
            pass

    elif 'open facebook' in command:
          url = 'https://www.facebook.com/'
          webbrowser.open(url)
          speak('Done')        

    elif 'what\'s up' in command:
         speak('Helping you out') 

    elif 'open google' in command:
    	 speak('Opening google')
    	 url = 'https://www.google.com/'
    	 webbrowser.open(url)
    	 speak('Done')

    elif 'open spotify' in command:
         speak('Opening spotify')
         os.system("spotify")      

    elif 'go offline' in command:
         exit()     


speak('Welcome Mister Akshai')

while True:
	assistant(myCommand())