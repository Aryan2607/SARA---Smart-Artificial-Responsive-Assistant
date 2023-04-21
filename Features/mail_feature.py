import smtplib
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3
import re
import json

r = sr.Recognizer()
engine = pyttsx3.Engine()

def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id)
    engine.setProperty('rate',170)
    print("")
    print(f"SARA : {Text}.")
    print("")
    engine.say(Text)
    engine.runAndWait()

def Listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # Listening Mode.....
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")

    except:
        return ""
    
    query = str(query).lower()
    print(query)
    return query

def load_email_dict():
    try:
        with open("DataBase\\email_dict.json", "r") as f:
            email_dict = json.load(f)
    except FileNotFoundError:
        email_dict = {}

    return email_dict

def save_email_dict(email_dict):
    with open("DataBase\\email_dict.json", "w") as f:
        json.dump(email_dict, f)

email_dict = load_email_dict()
# print("Loaded email_dict:", email_dict)

sender_email = "your_email_address"
sender_password = "your_email_password"

def send_mail(receiver, subject, body):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email, sender_password)

    email = EmailMessage()
    email["From"] = sender_email
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(body)
    server.send_message(email)

def main_exe():
    email_dict
    Speak("To whom would you like me to send the mail?")
    receiver = Listen()

    while not receiver:
        Speak("Sorry, I didn't catch that. Please say it again.")
        receiver = Listen()

    # check if nickname is called and get the corresponding email from the dictionary
    if receiver in email_dict:
        receiver = email_dict[receiver]
    else:
        # Remove spaces from the email address
        receiver = receiver.replace(" ", "")
        receiver = receiver.split("@")[0] + "@gmail.com"
        Speak(f"What nickname would you like to give to {receiver}?")
        nickname = Listen()
        while not nickname:
            Speak("Sorry, I didn't catch that. Please say it again.")
            nickname = Listen()
        email_dict[nickname] = receiver
        save_email_dict(email_dict)

    # check if email is valid
    while not re.match(r"[^@]+@[^@]+\.[^@]+", receiver):
        Speak("Sorry, that is not a valid email address. Please try again.")
        receiver = Listen()

    Speak("Please tell me the subject of the email.")
    subject = Listen()
    while not subject:
        Speak("Sorry, I didn't catch that. Please say it again.")
        subject = Listen()
    Speak("Please tell me the message you would like me to include in the email.")
    body = Listen()
    while not body:
        Speak("Sorry, I didn't catch that. Please say it again.")
        body = Listen()
    send_mail(receiver, subject, body)
    Speak("The email has been sent!")

# call the main_exe function
main_exe()
