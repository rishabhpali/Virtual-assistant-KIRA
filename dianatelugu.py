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

from teluguvoice import speak
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
    speak("నన్ను చూడనివ్వు. ఇప్పుడు సమయం : ")
    speak(Time)
    
def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    speak("ఈరోజు తేదీ : ")
    speak(date)
    speak(month)
    speak(year)
    
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("శుభోదయం!")
    elif hour >= 12 and hour <18:
        speak("శుభ మద్యాహ్నం !")
    elif hour >= 18 and hour < 24:
        speak("మీకు మంచి మరియు ఆహ్లాదకరమైన సాయంత్రం!")
    else:
        speak("మీకు విశ్రాంతి మరియు ప్రశాంతమైన రాత్రి!")
 
def wishme():
    speak("మీరు తిరిగి వచ్చినందుకు ఆనందంగా ఉంది ! ")
    greeting()
    speak("నేను మీకు ఏవిధంగా సహాయపడగలను?")
def takeCommandCMD():
    query = input("మీరు తెలుసుకోవాలనుకున్న ఏదైనా నన్ను అడగండి...\n")
    return query

def takeCommandMIC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("hmmmm.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="te-IN")
        print(query)
    
    except Exception as e:
        print(e)
        speak("దయచేసి మీరు దానిని పునరావృతం చేయగలరా?....")
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
    speak('మీరు గూగుల్‌లో ఏమి వెతకాలనుకుంటున్నారు ?')
    search = takeCommandMIC()
    wb.open('https://www.google.com/search?q='+search)
def news():
    newsapi = NewsApiClient(api_key='5e2527c963de439886c13e53d391706b')
    speak('మీకు ఏ అంశం గురించి వార్తలు కావాలి ?')
    topic = takeCommandMIC()
    data = newsapi.get_top_headlines(q=topic,
                                     language='en',
                                     page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
        
    speak("ప్రస్తుతానికి అంతే. నేను కొంత సమయంలో మరింత అప్‌డేట్ చేస్తాను")
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
    wakeword = "రిచా"
    while True:
        query = takeCommandMIC().lower()
        query1 = query
        query = word_tokenize(query)
        print(query)
        if wakeword in query:
            if'టైం ఎంత' in query:
                time()
            elif 'సమయం' in query:
                time()
            elif 'తేదీ' in query:
                date()
            elif 'ఈ రోజు తారీకు ఎంత' in query:
                date()
            elif 'మెయిల్' in query:
                email_list = {
                    'test': 'rishabhp780@gmail.com' 
                }
                try:
                    speak("మీరు ఎవరికి మెయిల్ పంపాలనుకుంటున్నారు ?")
                    name = takeCommandMIC()
                    reciever = email_list[name]
                    speak("మెయిల్ యొక్క విషయం ఏమిటి ?")
                    subject = takeCommandMIC()
                    speak('నేను ఏమి చెప్పాలి ?')
                    content = takeCommandMIC()
                    sendEmail(reciever, subject, content)
                    speak("నేను మెయిల్ పంపాను")
                except Exception as e:
                    print(e)
                    speak("ఇమెయిల్ పంపడం సాధ్యం కాలేదు")
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
            elif 'Vetakaṇḍi' in query:
                searchgoogle()  
            elif 'యూట్యూబ్‌లో' in query:
                speak("నేను యూట్యూబ్‌లో ఏమి వెతకాలి ?")
                topic = takeCommandMIC()
                pywhatkit.playonyt(topic)
            elif 'news' in query:
                news()
            elif 'చదవండి' in query:
                text2speech()
            elif 'తెరవండి' in query:
                os.system('explorer C://{}'.format(query.replace('open','')))
            elif 'తమాషా' in query:
                speak(pyjokes.get_joke())
            elif 'స్క్రీన్షాట్' in query:
                screenshot()
            elif 'గుర్తుంచుకోవాలి' in query:
                speak("నేను దాని కోసం చాలా తెలివైనవాడిని. ఇప్పుడు నాకు చెప్పండి?")
                data = takeCommandMIC()
                speak("అది గుర్తుంచుకోవాలని మీరు నాకు చెప్పారు"+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()
            elif 'రిమైండర్లు' in query:
                remember = open('data.txt','r')
                speak("అది గుర్తుంచుకోవాలని మీరు నాకు చెప్పారు"+remember.read())
                
            elif 'ఆఫ్‌లైన్' in query:
                speak('మంచి రోజు. నాతో ఇంటరాక్ట్ అయినందుకు ధన్యవాదాలు')
                quit()
            elif 'ధన్యవాదాలు' in query:
                speak('మంచి రోజు. నాతో ఇంటరాక్ట్ అయినందుకు ధన్యవాదాలు')
                quit()
            else:
                gpt_output(query1)
            
    