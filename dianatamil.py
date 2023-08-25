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

from tamilvoice import speak
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
    speak("நேரத்தை சரிபார்க்கிறேன். தற்பொழுது நேரம் : ")
    speak(Time)
    
def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    speak("இன்றைய தேதி : ")
    speak(date)
    speak(month)
    speak(year)
    
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("காலை வணக்கம்!")
    elif hour >= 12 and hour <18:
        speak("மதிய வணக்கம்!")
    elif hour >= 18 and hour < 24:
        speak("மாலை வணக்கம்!")
    else:
        speak("இனிய இரவு!")
 
def wishme():
    speak("நீங்கள் திரும்பி வந்ததில் மகிழ்ச்சி ! ")
    greeting()
    speak("நான் உங்களுக்கு எப்படி உதவ முடியும்?")
def takeCommandCMD():
    query = input("நீங்கள் தெரிந்து கொள்ள விரும்பும் எதையும் என்னிடம் கேளுங்கள்...\n")
    return query

def takeCommandMIC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("hmmmm.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="ta-IN")
        print(query)
    
    except Exception as e:
        print(e)
        speak("தயவுசெய்து அதை மீண்டும் செய்ய முடியுமா?....")
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
    speak('நீங்கள் Google இல் என்ன தேட விரும்புகிறீர்கள் ?')
    search = takeCommandMIC()
    wb.open('https://www.google.com/search?q='+search)
def news():
    newsapi = NewsApiClient(api_key='5e2527c963de439886c13e53d391706b')
    speak('உங்களுக்கு எந்த தலைப்பில் செய்தி தேவை ?')
    topic = takeCommandMIC()
    data = newsapi.get_top_headlines(q=topic,
                                     language='en',
                                     page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
        
    speak("இப்போதைக்கு அவ்வளவுதான். சிறிது நேரத்தில் மேலும் புதுப்பிப்பேன்")
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
    wakeword = "அண்ணா"
    
    while True:
        query = takeCommandMIC().lower()
        query1 = query
        query = word_tokenize(query)
        print(query)
        if wakeword in query:
            if'நேரம்' in query:
                time()
            elif 'தேதி' in query:
                date()
            elif 'அஞ்சல்' in query:
                email_list = {
                    'சோதனை': 'rishabhp780@gmail.com' 
                }
                try:
                    speak("யாருக்கு நீங்கள் அஞ்சல் அனுப்ப விரும்புகிறீர்கள் ?")
                    name = takeCommandMIC()
                    reciever = email_list[name]
                    speak("மின்னஞ்சலின் பொருள் என்ன ?")
                    subject = takeCommandMIC()
                    speak('நான் என்ன சொல்ல வேண்டும் ?')
                    content = takeCommandMIC()
                    sendEmail(reciever, subject, content)
                    speak("நான் அஞ்சல் அனுப்பியுள்ளேன்")
                except Exception as e:
                    print(e)
                    speak("மின்னஞ்சல் அனுப்ப முடியவில்லை")
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
            elif 'தேடல்' in query:
                searchgoogle()  
            elif 'யூடியூப்' in query:
                speak("நான் யூடியூப்பில் என்ன தேட வேண்டும் ?")
                topic = takeCommandMIC()
                pywhatkit.playonyt(topic)
            elif 'news' in query:
                news()
            elif 'படி' in query:
                text2speech()
            elif 'திறந்த' in query:
                os.system('explorer C://{}'.format(query.replace('open','')))
            elif 'நகைச்சுவை' in query:
                speak(pyjokes.get_joke())
            elif 'ஸ்கிரீன்ஷாட்' in query:
                screenshot()
            elif 'நினைவில் கொள்க' in query:
                speak("அதற்கு நான் மிகவும் புத்திசாலி. இப்போ சொல்லு?")
                data = takeCommandMIC()
                speak("அதை நினைவில் கொள்ள வேண்டும் என்று சொன்னீர்கள்"+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()
            elif 'நினைவூட்டல்கள்' in query:
                remember = open('data.txt','r')
                speak("நினைவில் கொள்ளச் சொன்னீர்கள்t"+remember.read())
                
            elif 'ஆஃப்லைனில்' in query:
                speak('ஒரு நல்ல நாள். என்னுடன் தொடர்பு கொண்டதற்கு நன்றி')
                quit()
            if 'நன்றி' in query:
                speak('ஒரு நல்ல நாள். என்னுடன் தொடர்பு கொண்டதற்கு நன்றி')
                quit()
            else:
                gpt_output(query1)
            