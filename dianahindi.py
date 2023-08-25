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

from hindivoice import speak
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
    speak("अभी टाइम हो रहा है : ")
    speak(Time)
    
def samay():
    Time = datetime.datetime.now().strftime("%I:%M:%S")#HOUR = I, MIN = M,SECOND = S
    speak("अभी समय हो रहा है : ")
    speak(Time)

def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    speak("आज डेट है : ")
    speak(date)
    speak(month)
    speak(year)

def tarik():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    speak("आज की तारीख है : ")
    speak(date)
    speak(month)
    speak(year)
    
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("सुप्रभात!")
    elif hour >= 12 and hour <18:
        speak("शुभ दोपहर!")
    elif hour >= 18 and hour < 24:
        speak("शुभ और सुखद शाम!")
    else:
        speak("शुभ रात्रि!")
 
def wishme():
    speak("आपको वापस देख कर अच्छा लगा ! ")
    greeting()
    speak("मैं आपकी किस प्रकार से मदद कर सकती हू ?")
def takeCommandCMD():
    query = input("मुझसे कुछ भी पूछो जो तुम जानना चाहते हो...\n")
    return query

def takeCommandMIC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("hmmmm.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="hi-IN")
        print(query)
    
    except Exception as e:
        print(e)
        speak("क्या आप वापस दोहरा सकते हैं ?....")
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
    speak('आप google में क्या सर्च करना चाहते हैं ?')
    search = takeCommandMIC()
    wb.open('https://www.google.com/search?q='+search)
def news():
    newsapi = NewsApiClient(api_key='5e2527c963de439886c13e53d391706b')
    speak('आपको किस टॉपिक पर न्यूज़ चाहिए ?')
    topic = takeCommandMIC()
    data = newsapi.get_top_headlines(q=topic,
                                     language='en',
                                     page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
        
    speak("अभी के लिए बस इतना ही. मैं कुछ समय में और अपडेट करूंगी")
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
    wakeword = "दीया"
    while True:
        query = takeCommandMIC().lower()
        query1 = query
        query = word_tokenize(query)
        print(query)
        if wakeword in query:
            if'समय' in query:
                samay()
            elif 'टाइम' in query:
                time()
            elif 'तारीख' in query:
                tarik()
            elif 'डेट' in query:
                date()
            elif 'मेल' in query:
                email_list = {
                    'टेस्ट': 'rishabhp780@gmail.com' 
                }
                try:
                    speak("आप किसे मेल भेजना चाहते हो ?")
                    name = takeCommandMIC()
                    reciever = email_list[name]
                    speak("मेल का विषय क्या है ?")
                    subject = takeCommandMIC()
                    speak('क्या कहूँ ?')
                    content = takeCommandMIC()
                    sendEmail(reciever, subject, content)
                    speak("मैंने मेल भेज दिया है")
                except Exception as e:
                    print(e)
                    speak("मेल भेजने में बाधा आ गयी है")
            elif 'वॉट्स्ऐप' in query:
                user_name = {
                    'diana': '+91 99200 53111'
                }
                try:
                    speak("किसको भेजना है ?")
                    name = takeCommandMIC()
                    reciever = user_name[name]
                    speak("क्या संदेश है ?")
                    message = takeCommandMIC()
                    sendwhatsmsg(phone_no, message)
                    speak("मैंने संदेश भेज दिया है")
                except Exception as e:
                    print(e)
                    speak("संदेश भेजने में बाधा आ गयी है")
            elif 'विकिपीडिया' in query:
                speak('ढूंढ रही हूं....')
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences = 4)
                print(result)
                speak(result) 
            elif 'सर्च' in query:
                searchgoogle()  
            elif 'यूट्यूब' in query:
                speak("मुझे यूट्यूब पर क्या खोजना चाहिए ?")
                topic = takeCommandMIC()
                pywhatkit.playonyt(topic)
            elif 'समाचार' in query:
                news()
            elif 'न्यूज़' in query:
                news()
            elif 'read' in query:
                text2speech()
            elif 'open' in query:
                os.system('explorer C://{}'.format(query.replace('open','')))
            elif 'जोक्स' in query:
                speak(pyjokes.get_joke())
            elif 'चुटकुला' in query:
                speak(pyjokes.get_joke())
            elif 'screenshot' in query:
                screenshot()
            elif 'remember' in query:
                speak("i am pretty intellingent for that. now tell me?")
                data = takeCommandMIC()
                speak("you said me to remember that"+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()
            elif 'reminders' in query:
                remember = open('data.txt','r')
                speak("you told me to remember that"+remember.read())
                
            elif 'ऑफलाइन' in query:
                speak('आपका दिन शुभ हो। मेरे साथ बातचीत करने के लिए धन्यवाद')
                quit()
            elif 'धन्यवाद' in query:
                speak('आपका दिन शुभ हो। मेरे साथ बातचीत करने के लिए धन्यवाद')
                quit()
            else:
                gpt_output(query1)
            
    
    
