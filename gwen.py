import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import random
import webbrowser
import subprocess
import os




listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',145)


sl = ('its okay', 'What happened?', 'Why are you sad?', 'Its alright I am here for you')
tl = ("Don't mention it", 'Your welcome', 'Never mind', 'Have a nice day')
ll = ('Yes and I love myself too', 'I will always love my user ','I love you too')
hl = ('Hola', 'Hey', 'Hello there')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command(recognizer, microphone):
    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("listening")
        audio = recognizer.listen(source)
        
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
        
    try:
        response = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response = "error"
        
        
    return response
if __name__ == "__main__":
    def run_gwen():
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        command = take_command(recognizer, microphone)
        print("you said:",command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
            quit()
        elif 'search' in command:
            doggle = command.replace('search', '')
            talk('searching '+doggle)
            print("search"+doggle)
            pywhatkit.search(doggle)
            quit()
        elif 'good' in command:
            hour = datetime.datetime.now().hour
            if hour >= 0 and hour < 12:
                talk("Hello,Good Morning")
                print("Hello,Good Morning")
            elif hour >= 12 and hour < 18:
                talk("Hello,Good Afternoon")
                print("Hello,Good Afternoon")
            else:
                talk("Hello,Good Evening")
                print("Hello,Good Evening")
        elif 'open youtube' in command:
            webbrowser.open_new_tab("https://www.youtube.com")
            talk("youtube is open now")
            quit()
        elif 'open google' in command:
            webbrowser.open_new_tab("https://www.google.com")
            talk("Google is open now")
            quit()
        elif 'open gmail' in command:
            webbrowser.open_new_tab("http://mail.google.com/mail")
            talk("Google Mail open now")
            quit()
        elif 'news' in command:
            webbrowser.open_new_tab("http://thetimesofindia.com/")
            talk('Here are some headlines from the Times of India,Happy reading')
            quit()
        elif 'weather' in command:
            webbrowser.open_new_tab("https://weatherextension.com/")
            talk('Here is the weather report')
            quit()
        elif 'open stackoverflow' in command:
            webbrowser.open_new_tab("https://stackoverflow.com/")
            talk('Stack Overflow is open now')
            quit()
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            print('Current time is ' + time)
        elif 'today' in command:
            day = datetime.datetime.today().weekday() + 1
            Day_dict = {1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday', 6: 'saturday',
                            7: 'sunday'}
            day_of_the_week = Day_dict[day]
            talk('today is' + day_of_the_week)
            print('today is' + day_of_the_week)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'what is' in command:
            person = command.replace('what is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'open powerpoint' in command:
            talk("opening Power Point presentation")
            power = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
            os.startfile(power)
        elif 'open word' in command:
            talk("opening Word")
            power = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
            os.startfile(power)
        elif 'will you go on a date with me' in command:
            talk('Are you a machine?')
            print('Are you a machine?')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
            print('I am in a relationship with wifi')
        elif 'tell me a joke' in command:
            talk(pyjokes.get_joke())
            print(pyjokes.get_joke())
        elif 'i am sad' in command:
            talk(random.choice(sl))
            print(random.choice(sl))
        elif "who am i" in command:
            talk("If you talk then definitely you are a human.")
            print("If you talk then definitely you are a human.")
        elif 'hello' in command:
            talk(random.choice(hl))
            print(random.choice(hl))
        elif 'hai' in command:
            talk(random.choice(hl))
            print(random.choice(hl))
        elif 'i love you' in command:
            talk(random.choice(ll))
            print(random.choice(ll))
        elif 'thank you' in command:
            talk(random.choice(tl))
            print(random.choice(tl))
        elif 'who are you' in command:
            print('I am gwen version 1 point O your personal assistant. I am programmed to minor tasks like'
                 'opening youtube,google chrome, gmail and stackoverflow ,predict time,search wikipedia,predict weather'
                 'In different cities, get top headline news from times of india and many more!')
            talk('I am gwen version 1 point O your personal assistant. I am programmed to minor tasks like'
              'opening youtube,google chrome, gmail and stackoverflow ,predict time,search wikipedia,predict weather'
              'In different cities, get top headline news from times of india and many more!')
        elif 'what can you do' in command:
            print('I am gwen version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,search wikipedia,'
                  'get top headline news from times of india and many more!')
            talk('I am gwen version 1 point O your personal assistant. I am programmed to minor tasks like'
                 'opening youtube,google chrome, gmail and stackoverflow ,predict time,search wikipedia'
                 ', get top headline news from times of india and many more!')
        elif 'who made you' in command:
            print('I was built by  Vamshi Krishna')
            talk('I was built by  Vamshi Krishna')
        elif 'who discovered you' in command:
            print('I was built by Vamshi Krishna')
            talk('I was built by Vamshi Krishna')
        elif "shutdown" in command:
            talk("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
        else:
            talk("I dont know what you are talking about")
            print("I dont know what you are talking about")


print("Hi this is Gwen\nA friendly V.U.I.\n")
talk("Hi this is Gwen\nA friendly V.U.I.")


for _ in range(15):
    run_gwen()
