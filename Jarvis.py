from time import sleep
from turtle import reset
import webbrowser
import pyautogui
import tkinter as tk
import spotipy as sp
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth

from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
print(">> Starting The SARA : Wait For Some Seconds.")
from Body.Listen import MicExecution
from Body.Listen import Listen
from Body.Speak import Speak
print(">> Started The SARA : Wait For Few Seconds More")
from Features.Song import Song
from Features.Stocks import stock_exec
from Features.Clap import Tester
from Features.Wakeup import WakeupDetected
from Features.Googlesearch import google_search
from Features.mail_feature import main_exe

from Main import MainTaskExecution


# class JarvisUI:

#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.resizable(True, True)
#         self.root.mainloop()

# JarvisUI()

def MainExecution():
    Speak("Hello Sir")
    Speak("I'm SARA, A Smart Artificial Responsive Assistant.")

    while True:
        # self.query = self.takecommand().lower()
        # if 'song please' in self.query or 'play some song' in self.query or 'could you play some song' in self.query:
        #     Speak('Sir what song should i play...')
        #     song = self.takecommand()
        #     webbrowser.open(f'https://open.spotify.com/search/{song}')
        #     sleep(13)
        #     pyautogui.click(x=1055, y=617)
        #     Speak('Playing' + song)
        
        # elif 'play' in self.query or 'can you play' in self.query or 'please play' in self.query:
        #     Speak("OK! here you go!!")
        #     self.query = self.query.replace("play", "")
        #     self.query = self.query.replace("could you play", "")
        #     self.query = self.query.replace("please play", "")
        #     webbrowser.open(f'https://open.spotify.com/search/{self.query}')
        #     sleep(19)
        #     pyautogui.click(x=1055, y=617)
        #     print('Enjoy!' + reset)
        #     Speak("Enjoy Sir!!")

        
        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass

        # elif "whatsapp message" in Data:
        #     pass

        # elif "turn on the tv" in Data:# Specific COmmand
        #     Speak("Ok..Turning On The Android TV")

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
            Speak(Reply)


        elif "song" in Data or "music" in Data:
            Reply = Song(Data)
            Speak("Playing your song...")
            Speak("If you got any Ad than please skip it manually")

        elif "google search" in Data or "search on google" in Data or "get google results" in Data:
            Reply = google_search(Data)
            Speak("Just a second sir...")
            Speak("Showing top 10 results collected from google search")

        elif "send email" in Data or "send mail" in Data or "a mail" in Data or "an email" in Data:
            Reply = main_exe()

        elif "predict the stock price" in Data or "predicted stock price" in Data or "future stock prices" in Data or "prediction for the stock" in Data or "stock price" in Data or "predict stock" in Data or "stock price" in Data or "stock prices" in Data:
            Reply = stock_exec()

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        MainExecution()
    else:
        pass

ClapDetect()

# def Wakeup():
#     query = WakeupDetected()
#     if "Wake up" in query:
#         print("")
#         MainExecution()
#     else:
#         pass

# Wakeup
