import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
from nltk.tokenize import word_tokenize


import openai
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    speak("hey there ! specify the language you want me to use:")

def takeCommandCMD():
    query = input("english,marathi,hindi,bengali,tamil,gujarati,nepali: \n")
    return query

if __name__=="__main__":
    wishme()
    while True:
        query = takeCommandCMD().lower()
        if 'bengali' in query:
            from dianabengali import bengali
            bengali(return 1)
            
        