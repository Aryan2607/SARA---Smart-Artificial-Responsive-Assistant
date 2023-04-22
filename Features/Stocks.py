import speech_recognition as sr
import yfinance as yf
import os
import json
import requests
import pyttsx3
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import forex_python.converter as converter
import datetime

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

# Function to get the latest exchange rate of USD to INR
def get_exchange_rate():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    if response.status_code == 200:
        data = response.json()
        if 'rates' in data and 'INR' in data['rates']:
            return data['rates']['INR']
        else:
            raise ValueError('Exchange rate data not available')
    else:
        raise ValueError('Error fetching exchange rate data')

# Get the latest exchange rate of USD to INR
exchange_rate = get_exchange_rate()

# Get today's date as the end date
end_date = datetime.datetime.now().strftime("%Y-%m-%d")

def get_company_name(symbol):
    ticker = yf.Ticker(symbol)
    if 'longName' in ticker.info:
        return ticker.info['longName']
    else:
        return ticker.info['shortName']

# Function to predict the closing price of 1 stock
def predict_stock_price(stock_name):
    # stock_ticker = yf.Ticker()
    symbol = stock_name.upper()

    # Download historical stock prices data
    stock_data = yf.download(symbol, start='2010-01-01', end=end_date)

    # Define input features and target variable
    X = stock_data[['Open', 'High', 'Low', 'Volume']]
    y = stock_data['Close']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make a prediction on the most recent day
    recent_data = stock_data.tail(1)[['Open', 'High', 'Low', 'Volume']]
    prediction = model.predict(recent_data)[0]

    # Get the last closing price of the stock
    last_close_price = stock_data['Close'].iloc[-1]

    # Convert last closing price to Indian Rupees and US Dollars using the latest exchange rate
    inr_price = last_close_price * exchange_rate
    usd_price = last_close_price

    # Get the company name from the stock ticker symbol
    company_name = get_company_name(symbol)

    # Print the results
    Speak(f"Last closing price of {company_name} (in US Dollars) is: {usd_price:.2f} Dollars")
    Speak(f"Last closing price of {company_name} (in Indian Rupees) is: {inr_price:.2f} Rupees")
    if prediction < last_close_price:
        Speak("The market is going down. Better to sell stocks.")
    else:
        Speak("The market is going up. Better to hold on to stocks")
    print('Mean squared error: ', mean_squared_error(y_test, model.predict(X_test)))
    return f"Predicted stock price (in US Dollars) is: {prediction:.2f} Dollars", f"Predicted stock price (in Indian Rupees) is: {prediction * exchange_rate:.2f} Rupees", f"Prediction result is: " + ("Market will go down. Better to sell stocks" if prediction < last_close_price else "Market will go up. Better to hold on to stocks") + "."

# Predict the price and display the result
def stock_exec():
    Speak("Please tell me the stock code to predict the price for.")
    stock_code = Listen()
    stock_name = stock_code.replace(" ", "")
    predicted_price_USD, predicted_price_INR, message = predict_stock_price(stock_name)
    Speak(predicted_price_USD)
    Speak(predicted_price_INR)
    Speak(message)
    
# stock_exec()