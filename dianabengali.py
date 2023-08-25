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

from bengalivoice import speak
import openai
openai.api_key = "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"





sender = 'diana.for.rishabh@gmail.com'
epwd = 'hyzunleyybwkgouq'
phone_no = '+91 89202 08655'
#to = 'rishabhp780@gmail.com'

#engine = pyttsx3.init()

#def speak(text):
 #   engine.say(text)
  #  engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")#HOUR = I, MIN = M,SECOND = S
    speak("আমাকে পরীক্ষা করতে দিন, সময় হয়েছে : ")
    speak(Time)
    
def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    speak("আজকের তারিখ হলো : ")
    speak(date)
    speak(month)
    speak(year)
    
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("সুপ্রভাত!")
    elif hour >= 12 and hour <18:
        speak("শুভ অপরাহ্ন!")
    elif hour >= 18 and hour < 24:
        speak("শুভ সন্ধ্যা!")
    else:
        speak("শুভ রাত্রি!")
 
def wishme():
    speak("তোমাকে ফিরে পেয়ে ভালো লাগলো ! ")
    greeting()
    speak("আপনাকে কিভাবে সাহায্য করতে পারি?")
def takeCommandCMD():
    query = input("আপনি যা জানতে চান আমাকে জিজ্ঞাসা করুন...\n")
    return query

def takeCommandMIC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("hmmmm.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="bn-IN")
        print(query)
    
    except Exception as e:
        print(e)
        speak("আপনি অনুগ্রহ করে এটি পুনরাবৃত্তি করতে পারেন?....")
        return "none"
    return query

def sendEmail(reciever, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, epwd)
    email = EmailMessage()
    email['From'] = sender
    email['to'] = reciever
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()
    
def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no +'&text='+Message)
    sleep(10)
    pyautogui.press('enter')
def searchgoogle():
    speak('আপনি google এ কি সার্চ করতে চান ?')
    search = takeCommandMIC()
    wb.open('https://www.google.com/search?q='+search)
def news():
    newsapi = NewsApiClient(api_key='5e2527c963de439886c13e53d391706b')
    speak('আপনি কি বিষয় সম্পর্কে খবর প্রয়োজন ?')
    topic = takeCommandMIC()
    data = newsapi.get_top_headlines(q=topic,
                                     language='en',
                                     page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
        
    speak("আপাতত এই পর্যন্ত. আমি কিছু সময়ের মধ্যে আরও আপডেট করব")
def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)
def screenshot():
    name_img = (tt.time())
    name_img = f'C:\\Users\\Asus\\OneDrive\\Desktop\\assistant\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()
start_sequence = "\nAI:"
restart_sequence = "\nHuman:"

prompt = "the following is a conversation with an AI assistant."
def gpt_output(prompt):
    response = openai.Completion.create(
    model = "text-davinci-003",
    prompt = prompt,
    temperature=0.9,
    max_tokens = 3000,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0.6,
    stop = ["Human:", "AI:"]
    )  
    data = response.choices[0].text
    print(data)
    speak(data)
       
    
    
#https://api.openweathermap.org/data/2.5/weather?q={New Delhi}&units=imperial&appid={d63aee3e9700c501e1ea0663cc3d601b}

if __name__ == "__main__":
    wishme()
    wakeword = "রিচা"
    while True:
        query = takeCommandMIC().lower()
        query1 = query
        query = word_tokenize(query)
        print(query)
        if wakeword in query:
            if'সময়' in query:
                time()
            elif 'তারিখ' in query:
                date()
            elif 'মেইল' in query:
                email_list = {
                    'পরীক্ষা': 'rishabhp780@gmail.com' 
                }
                try:
                    speak("যাকে আপনি মেইল ​​পাঠাতে চান ?")
                    name = takeCommandMIC()
                    reciever = email_list[name]
                    speak("মেইলের বিষয় কি ?")
                    subject = takeCommandMIC()
                    speak('আমার কী বলা উচিত ?')
                    content = takeCommandMIC()
                    sendEmail(reciever, subject, content)
                    speak("আমি মেইল ​​পাঠিয়েছি")
                except Exception as e:
                    print(e)
                    speak("ইমেইল পাঠাতে অক্ষম")
            elif 'হোয়াটসঅ্যাপ' in query:
                user_name = {
                    'Diana': '+91 99200 53111'
                }
                try:
                    speak("to whom you want to send the mail ?")
                    name = takeCommandMIC()
                    reciever = user_name[name]
                    speak("what's the message ?")
                    message = takeCommandMIC()
                    sendwhatsmsg(phone_no, message)
                    speak("i have sent the message")
                except Exception as e:
                    print(e)
                    speak("unable to send the message")
            elif 'wikipedia' in query:
                speak('searching on wikipedia....')
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences = 4)
                print(result)
                speak(result) 
            elif 'অনুসন্ধান' in query:
                searchgoogle()  
            elif 'ইউটিউব' in query:
                speak("আমি ইউটিউবে কি অনুসন্ধান করা উচিত ?")
                topic = takeCommandMIC()
                pywhatkit.playonyt(topic)
            elif 'খবর' in query:
                news()
            elif 'পড়া' in query:
                text2speech()
            elif 'খোলা' in query:
                os.system('explorer C://{}'.format(query.replace('open','')))
            elif 'কৌতুক' in query:
                speak(pyjokes.get_joke())
            elif 'স্ক্রিনশট' in query:
                screenshot()
            elif 'মনে রাখবেন' in query:
                speak("আমি এর জন্য বেশ বুদ্ধিমান। এখন আমাকে বল?")
                data = takeCommandMIC()
                speak("তুমি আমাকে এটা মনে রাখতে বলেছিলে"+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()
            elif 'অনুস্মারক' in query:
                remember = open('data.txt','r')
                speak("তুমি আমাকে এটা মনে রাখতে বলেছিলে"+remember.read())
                
            elif 'অফলাইন' in query:
                speak('আপনার দিনটি শুভ হোক. আমার সাথে যোগাযোগ করার জন্য ধন্যবাদ')
                quit()
            else:
                gpt_output(query1)
            