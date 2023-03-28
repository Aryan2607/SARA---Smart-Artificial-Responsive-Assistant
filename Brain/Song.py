# /*******************************************The code below is for normal users to play music from Spotify*********************************************/


# /*******************************************The code below is used to play from youtube*********************************************/
# import pywhatkit
# def Song(track):
#     song =(track)
#     pywhatkit.playonyt(song)

# /*******************************************The code below is for Premium user only*********************************************/

# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# client_id = 'da182c69aff04b23ae82c8c4848f3213'
# client_secret = '508ce5fd715849348f5fb7b56b4d37ed'
# client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# results = sp.search(q='track:Jhoome jo pathaan', type='track')
# track_id = results['tracks']['items'][0]['id']
# sp.start_playback(uris=[f'spotify:track:{track_id}'])

# /*******************************************The code below is for basic operation based Automation*********************************************/
# import openai
# from dotenv import load_dotenv
# import pyautogui
# import os
# import time

# def Spotify(song,chat_log= None):
#     os.system("Spotify")
#     time.sleep(5)
#     pyautogui.hotkey('ctrl', 'l')
#     pyautogui.write('Tera Zikr', interval= 0.1)
    
#     for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
#         time.sleep(2)
#         pyautogui.press(key)

# Spotify("Tera Zikr")