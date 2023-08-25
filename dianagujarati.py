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

from gujarativoice import speak
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
    speak("મને સમય તપાસવા દો. સમય છે : ")
    speak(Time)
    
def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    speak("આજની તારીખ છે : ")
    speak(date)
    speak(month)
    speak(year)
    
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("તમને ખૂબ જ શુભ સવાર !")
    elif hour >= 12 and hour <18:
        speak("શુભ બપોર !")
    elif hour >= 18 and hour < 24:
        speak("શુભ સાંજ!")
    else:
        speak("શુભ રાત્રી !")
 
def wishme():
    speak("તમને પાછા મળીને આનંદ થયો ! ")
    greeting()
    speak("હું આપની શું મદદ કરી શકું?")
def takeCommandCMD():
    query = input("તમે જે કંઈપણ જાણવા માગો છો તે મને પૂછો...\n")
    return query

def takeCommandMIC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("hmmmm.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="gu-IN")
        print(query)
    
    except Exception as e:
        print(e)
        speak("શું તમે તેને પુનરાવર્તન કરી શકો છો ?....")
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
    speak('તમે ગૂગલમાં શું સર્ચ કરવા માંગો છો ?')
    search = takeCommandMIC()
    wb.open('https://www.google.com/search?q='+search)
def news():
    newsapi = NewsApiClient(api_key='5e2527c963de439886c13e53d391706b')
    speak('તમારે કયા વિષયના સમાચાર જોઈએ છે ?')
    topic = takeCommandMIC()
    data = newsapi.get_top_headlines(q=topic,
                                     language='en',
                                     page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
        
    speak("હમણાં માટે તે છે. હું થોડા સમયમાં વધુ અપડેટ કરીશ")
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
    wakeword = "દયા"
    while True:
        query = takeCommandMIC().lower()
        query1 = query
        query = word_tokenize(query)
        print(query)
        if wakeword in query:
            if'સમય' in query:
                time()
            elif 'તારીખ' in query:
                date()
            elif 'મેઇલ' in query:
                email_list = {
                    'test': 'rishabhp780@gmail.com' 
                }
                try:
                    speak("તમે જેમને મેઇલ મોકલવા માંગો છો ?")
                    name = takeCommandMIC()
                    reciever = email_list[name]
                    speak("મેઇલનો વિષય શું છે ?")
                    subject = takeCommandMIC()
                    speak('મારે શું લખવું જોઈએ ?')
                    content = takeCommandMIC()
                    sendEmail(reciever, subject, content)
                    speak("મે મેઈલ મોકલી દીધો છે")
                except Exception as e:
                    print(e)
                    speak("મેઇલ મોકલ્યો નથી")
            elif 'whatsapp' in query:
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
            elif 'શોધ' in query:
                searchgoogle()  
            elif 'યુટ્યુબ' in query:
                speak("મારે યુટ્યુબ પર શું સર્ચ કરવું જોઈએ ?")
                topic = takeCommandMIC()
                pywhatkit.playonyt(topic)
            elif 'સમાચાર' in query:
                news()
            elif 'read' in query:
                text2speech()
            elif 'open' in query:
                os.system('explorer C://{}'.format(query.replace('open','')))
            elif 'મજાક' in query:
                speak(pyjokes.get_joke())
            elif 'સ્ક્રીનશોટ' in query:
                screenshot()
            elif 'યાદ રાખો' in query:
                speak("હું તેના માટે ખૂબ હોશિયાર છું. હવે મને કહો?")
                data = takeCommandMIC()
                speak("તમે મને તે યાદ રાખવા કહ્યું હતું"+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()
            elif 'રીમાઇન્ડર્સ' in query:
                remember = open('data.txt','r')
                speak("તમે મને તે યાદ રાખવા કહ્યું હતું"+remember.read())
                
            elif 'ઑફલાઇન' in query:
                speak('તમારો દિવસ શુભ રહે. મારી સાથે વાર્તાલાપ કરવા બદલ આભાર')
                quit()
            elif 'આભાર' in query:
                speak('તમારો દિવસ શુભ રહે. મારી સાથે વાર્તાલાપ કરવા બદલ આભાર')
                quit()
            else:
                gpt_output(query1)
            import pyttsx3
