from time import sleep
from turtle import reset
import webbrowser
import pyautogui
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from Brain.Song import *
import tkinter as tk
from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Started The Jarvis : Wait For Few Seconds More")
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


        # elif "play" in Data or "song" in Data or "music" in Data:
        #     Reply = Song(Data)

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
