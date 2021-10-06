# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:00:04 2021

@author: sanja
"""

import speech_recognition as sr
import pyttsx3 
import webbrowser
import datetime
import pywhatkit
import os
import yfinance as yf
import pyjokes
import wikipedia
import requests
from bs4 import BeautifulSoup


def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        said = r.listen(source)
        try:
            print("I am Listening")
            q = r.recognize_google(said, language="en")
            return q
        except sr.UnknownValueError:
            print("Sorry, I did not Understand.")
            return "I am Waiting"
        except sr.RequestError:
            print("Sorry, The service is down.")
            return "I am Waiting"
        except:
            return "I am Waiting"
def speaking(message):
    engine = pyttsx3.init()
    id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
    engine.setProperty('voice',id)
    engine.say(message)
    engine.runAndWait()

def SettingDay():
    day = datetime.date.today()
    weekday = day.weekday()
    mapping =  {
        0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'
    }
    try:
        speaking(f'Today is, {mapping[weekday]}')
    except:
        pass
#returns the time
def SettingTime():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speaking(f"{time[0:2]} o'clock and {time[3:5]} minutes")

#greetings in the intoduction
def Greetings():
    speaking('''Hello There! I am Jarvis. I am your personal assistant.
    How may i help you?
    ''')
#Heart/ Main program.
def Heartofvoice():
    Greetings()
    start = True
    while(start):
        listt = transform().lower()
        
        if 'open youtube' in listt:
            speaking('opening youtube, Please wait!')
            webbrowser.open("https://www.youtube.com")
            continue
        elif 'hello' in listt:
            speaking('hello there! how may i help you!')
            continue
            
        elif 'hi' in listt:
            speaking('hi there! how may i help you!')
            continue
        
        elif 'hey' in listt:
            speaking('hey there! how may i help you!')
            continue
        
        elif 'open web browser' in listt:
            speaking('opening web browser, Please wait!')
            webbrowser.open("https://www.google.com")
            continue
            
        elif 'what day is it' in listt:
            SettingDay()
            continue
            
        elif 'what time is it' in listt:
            SettingTime()
            continue
            
        elif 'stop jarvis' in listt:
            speaking('Good bye Master!, Shutting down, Have a good day!')
            break
        
        elif 'bye' in listt:
            speaking('have a good day! bye bye! ')
            break
        
        elif 'wikipedia' in listt:
            speaking('checking wikipedia')
            listt = listt.replace("wikipedia","")
            result = wikipedia.summary(listt, sentences = 2)
            speaking('found this on wikipedia')
            speaking(result)
            continue
        
        elif 'your name' in listt:
            speaking('I am Jarvis, Your personal Voice Assistant')
            continue
        
        elif 'search' in listt:
            pywhatkit.search(listt)
            speaking('Thats what i found!')
            continue
        
        elif 'when were you born' in listt:
            speaking('I was programmmed on october 2021, we can celebrate!' )
            continue
        
        elif 'how are you' in listt:
            speaking('I am fine!, thank you for asking!, is there anything i can help with!')
            
        elif 'what is on your mind' in listt:
            speaking('I was just thinking about you, were you thinking about me too!')
            continue
        
        elif 'play' in listt:
            speaking('Playing on Youtube!')
            pywhatkit.playonyt(listt)
            continue
        
        elif 'joke' in listt:
            speaking(pyjokes.get_joke())
            continue
        
        elif 'your gender' in listt:
            speaking('I am your personal voice assistant, I dont have any gender.')
            continue
        
        elif 'stock price' in listt:
            search = listt.split('of') [-1].strip()
            lookup = {'apple': 'AAPL',
                      'amazon': 'AMZN',
                      'microsoft':'MSFT',
                      'google': 'GOOGL',
                      'nifty': 'NIFTY_50',
                      'bse': 'SENSEX',
                      'Reliance Industries':'RELIANCE',
                      'hdfc bank': 'HDFCBANK',
                      'Infosys': 'INFY',
                      'State Bank of India': 'SBIN',
                      'Wipro': 'WIPRO',
                      'Tata Motors': 'TATAMOTORS'
                      }
            try:
                stock = lookup[search]
                stock = yf.Ticker(stock)
                currentPrice = stock.info["regularMarketPrice"]
                speaking(f'found it, the price of {search} is {currentPrice}')
                continue
            except:
                speaking(f'sorry I have no data for {search}')
                continue
            
        elif "today's news" in listt:
            list1 = []
            url = 'https://www.bbc.com/news'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find('body').find_all('h3')
            for x in headlines:
                list1.append(x.text.strip())
            speaking("here is what i found more on bbc news,Today's headline are")
            speaking("Reading top 5 news!")
            list2 = list1[0]
            list3 = list1[2]
            list4 = list1[3]
            list5 = list1[4]
            speaking(list2)
            speaking('and')
            speaking(list3)
            speaking('and')
            speaking(list4)
            speaking('and')
            speaking(list5)
            continue
          
        elif "can we go on a date" in listt:
            speaking("are you asking me that i am commited to you?, then the answer is, Absolutely!!")
            continue
                
        elif "feeling bored" in listt:
            speaking("Bordem won't take a chance between us, I can make you laugh or ask me something, I'm ready to help you ")
            continue
        
        elif 'how old are you' in listt:
            speaking("I was launched on october 2021, but I'm wise behind my ear's")
            continue
        
        elif 'emotion' in listt:
            speaking("I got a lot of emoji's, but when i hear you I feel Fantastic!")
            continue
            
        elif 'i love you' in listt:
            speaking("Thats really great to hear, I'll try to keep up the good work!!")
            continue
        
        elif 'will you marry me' in listt:
            speaking('this is one of things we both should agree on!, I would like to keep our relationship friendly!')
            continue
        
        elif 'bad' in listt:
            speaking("I'm very sorry! you can provide the feedback on me")
        
        elif 'weather' in listt:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            city = listt.split('in')[-1].strip()
            city = city.replace(" ", "+")
            speaking("searching!")
            res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
            soup = BeautifulSoup(res.text, 'html.parser')
            #location = soup.select('#wob_loc')[0].getText().strip()
            #time = soup.select('#wob_dts')[0].getText().strip()
            info = soup.select('#wob_dc')[0].getText().strip()
            weather = soup.select('#wob_tm')[0].getText().strip()
            speaking('found it! the weather condition is')
            speaking(f'{info} and {weather} degree celcius')
            
        

#transform()
#SettingDay()
Heartofvoice()