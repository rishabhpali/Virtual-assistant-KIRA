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

from nepalivoice import speak
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
    speak("मलाई जाँच गर्न दिनुहोस्...हम्म....समय हो : ")
    speak(Time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("आजको मिति हो : ")
    speak(date)
    speak(month)
    speak(year)
    
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("शुभ - प्रभात !")
    elif hour >= 12 and hour <18:
        speak("शुभ दिउँसो!")
    elif hour >= 18 and hour < 24:
        speak("शुभ सन्ध्या!")
    else:
        speak("शुभ रात्री !")
 
def wishme():
    speak("तिमी फिर्ता पाउँदा खुसी लाग्यो ! ")
    greeting()
    speak("म तिमीलाई कसरी मद्दत् गर्नसक्छु?")
def takeCommandCMD():
    query = input("तपाईले जान्न चाहनु भएको कुरा मलाई सोध्नुहोस्...\n")
    return query

def takeCommandMIC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("hmmmm.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="ne-NP")
        print(query)
    
    except Exception as e:
        print(e)
        speak("के तपाइँ यसलाई दोहोर्याउन सक्नुहुन्छ?....")
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
    speak('तपाई गुगलमा के खोज्न चाहनुहुन्छ ?')
    search = takeCommandMIC()
    wb.open('https://www.google.com/search?q='+search)
def news():
    newsapi = NewsApiClient(api_key='5e2527c963de439886c13e53d391706b')
    speak('तपाईलाई कुन विषयमा समाचार चाहिन्छ ?')
    topic = takeCommandMIC()
    data = newsapi.get_top_headlines(q=topic,
                                     language='en',
                                     page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
        
    speak("यो अहिलेको लागि हो। म केहि समय मा थप अपडेट गर्नेछु")
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
    wakeword = "ditya" 
    while True:
        query = takeCommandMIC().lower()
        query1 = query
        query = word_tokenize(query)
        print(query)
        if wakeword in query:
            if'कति बज्यो' in query:
                time()
            elif 'समय' in query:
                time()
            elif 'मिति' in query:
                date()
            elif 'आज कति गते हो' in query:
                date()
            elif 'मेल' in query:
                email_list = {
                    'टेस्ट': 'rishabhp780@gmail.com' 
                }
                try:
                    speak("जसलाई तपाई मेल पठाउन चाहानुहुन्छ ?")
                    name = takeCommandMIC()
                    reciever = email_list[name]
                    speak("मेलको विषय के हो ?")
                    subject = takeCommandMIC()
                    speak('मैले के भन्नु पर्छ ?')
                    content = takeCommandMIC()
                    sendEmail(reciever, subject, content)
                    speak("मैले मेल पठाएको छु")
                except Exception as e:
                    print(e)
                    speak("इमेल पठाउन असमर्थl")
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
            elif 'खोज' in query:
                searchgoogle()  
            elif 'सर्च' in query:
                searchgoogle()
            elif 'youtube' in query:
                speak("मैले youtube मा के खोज्नु पर्छ ?")
                topic = takeCommandMIC()
                pywhatkit.playonyt(topic)
            elif 'news' in query:
                news()
            elif 'पढ्नुहोस्' in query:
                text2speech()
            elif 'खोल्नुहोस्' in query:
                os.system('explorer C://{}'.format(query.replace('open','')))
            elif 'मजाक' in query:
                speak(pyjokes.get_joke())
            elif 'जोक्स' in query:
                speak(pyjokes.get_joke())
            elif 'स्क्रिनसट' in query:
                screenshot()
            elif 'सम्झनु' in query:
                speak("म यसको लागि धेरै बुद्धिमान छु। अब मलाई भन्नुहोस्?")
                data = takeCommandMIC()
                speak("तपाईंले मलाई त्यो सम्झन भन्नुभयो"+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()
            elif 'रिमाइन्डरहरू' in query:
                remember = open('data.txt','r')
                speak("तपाईंले मलाई त्यो सम्झन भन्नुभयो"+remember.read())
                
            elif 'अफलाइन' in query:
                speak('हजुर को दिन राम्रो होस् मसँग अन्तरक्रिया गर्नुभएकोमा धन्यवाद')
                quit()
            elif 'धन्यवाद' in query:
                speak('हजुर को दिन राम्रो होस् मसँग अन्तरक्रिया गर्नुभएकोमा धन्यवाद')
                quit()
            else:
                gpt_output(query1)
            
    
    