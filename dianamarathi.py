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

from marathivoice import speak
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
    speak("मला वेळ तपासू द्या. वेळ आहे : ")
    speak(Time)
    
def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    speak("आजची तारीख आहे : ")
    speak(date)
    speak(month)
    speak(year)
    
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("शुभ प्रभात !")
    elif hour >= 12 and hour <18:
        speak("शुभ दुपार!")
    elif hour >= 18 and hour < 24:
        speak("शुभ संध्या !")
    else:
        speak("शुभ रात्री !")
 
def wishme():
    speak("तुम्हाला परत आल्याने आनंद झाला ! ")
    greeting()
    speak("मी तुम्हाला कशी मदत करू शकते ?")
def takeCommandCMD():
    query = input("तुम्हाला जे काही जाणून घ्यायचे आहे ते मला विचारा...\n")
    return query

def takeCommandMIC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("hmmmm.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="mr-IN")
        print(query)
    
    except Exception as e:
        print(e)
        speak("तुम्ही कृपया त्याची पुनरावृत्ती करू शकता?....")
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
    speak('तुम्हाला गुगलवर काय शोधायचे आहे ?')
    search = takeCommandMIC()
    wb.open('https://www.google.com/search?q='+search)
def news():
    newsapi = NewsApiClient(api_key='5e2527c963de439886c13e53d391706b')
    speak('तुम्हाला कोणत्या विषयाची बातमी हवी आहे ?')
    topic = takeCommandMIC()
    data = newsapi.get_top_headlines(q=topic,
                                     language='en',
                                     page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
        
    speak("आतासाठी तेच आहे. मी काही वेळाने अधिक अपडेट करेन")
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
    wakeword = "दिया"
    while True:
        query = takeCommandMIC().lower()
        query1 = query
        query = word_tokenize(query)
        print(query)
        if wakeword in query:
            if'वेळ' in query:
                time()
            elif 'तारीख' in query:
                date()
            elif 'मेल' in query:
                email_list = {
                    'टेस्ट': 'rishabhp780@gmail.com' 
                }
                try:
                    speak("ज्याला तुम्हाला मेल पाठवायचा आहे ?")
                    name = takeCommandMIC()
                    reciever = email_list[name]
                    speak("मेलचा विषय काय आहे ?")
                    subject = takeCommandMIC()
                    speak('मी काय बोलावे ?')
                    content = takeCommandMIC()
                    sendEmail(reciever, subject, content)
                    speak("मी मेल पाठवला आहे")
                except Exception as e:
                    print(e)
                    speak("ईमेल पाठवू शकत नाही")
            elif 'whatsapp' in query:
                user_name = {
                    'Diana': '+91 99200 53111'
                }
                try:
                    speak("ज्याला तुम्हाला मेल पाठवायचा आहे ?")
                    name = takeCommandMIC()
                    reciever = user_name[name]
                    speak("संदेश काय आहे ?")
                    message = takeCommandMIC()
                    sendwhatsmsg(phone_no, message)
                    speak("मी संदेश पाठवला आहे")
                except Exception as e:
                    print(e)
                    speak("संदेश पाठवण्यात अक्षम")
            elif 'विकिपीडिया' in query:
                speak('विकिपीडियावर शोधत आहे....')
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences = 4)
                print(result)
                speak(result) 
            elif 'शोध' in query:
                searchgoogle()
            elif 'सर्च' in query:
                searchgoogle()  
            elif 'युट्युब' in query:
                speak("मी youtube वर काय शोधले पाहिजे ?")
                topic = takeCommandMIC()
                pywhatkit.playonyt(topic)
            elif 'बातम्या' in query:
                news()
            elif 'समाचार' in query:
                news()
            elif 'वाचा' in query:
                text2speech()
            elif 'उघडा' in query:
                os.system('explorer C://{}'.format(query.replace('open','')))
            elif 'विनोद' in query:
                speak(pyjokes.get_joke())
            elif 'जोक्स' in query:
                speak(pyjokes.get_joke())
            elif 'स्क्रीनशॉट' in query:
                screenshot()
            elif 'लक्षात ठेवा' in query:
                speak("त्यासाठी मी खूप हुशार आहे. आता मला सांग ?")
                data = takeCommandMIC()
                speak("तू मला ते लक्षात ठेवण्यास सांगितलेस"+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()
            elif 'स्मरणपत्रे' in query:
                remember = open('data.txt','r')
                speak("तू मला ते लक्षात ठेवायला सांगितलेस"+remember.read())
                
            elif 'ऑफलाइन' in query:
                speak('तुमचा दिवस चांगला जावो माझ्याशी संवाद साधल्याबद्दल धन्यवाद')
                quit()
            elif 'धन्यवाद' in query:
                speak('तुमचा दिवस चांगला जावो माझ्याशी संवाद साधल्याबद्दल धन्यवाद')
                quit()
            else:
                gpt_output(query1)
            