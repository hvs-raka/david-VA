import speech_recognition as sr
import pyttsx3
import pywhatkit 
import datetime
import pyjokes
from googlesearch import search



listener = sr.Recognizer() # this is listener which hears through mic
engine = pyttsx3.init()  # this is to initiate the pyttsx3
voices = engine.getProperty('voices') # giving the voice 
engine.setProperty('voices', voices[1].id) # setting up the voice  

def talk(text): # function which will use text and convert it into the voice
    engine.say(text)  # this engine say is to convert the text to voice
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:  # will get the sound from the source 
            print("listening...")
            voice = listener.listen(source)  # adding the voice in the voice variable 
            command = listener.recognize_google(voice) # it will use the recognition of google and convert our speech into text
            command = command.lower() 
            if 'david' in command: # in this condition if the word david is present only then the following commands are gonna work 
                command = command.replace('david', '')

    except:  # if the 'david' word is not present in the speech then the it will just get passed
        talk("can't understand you")
        pass
    return command

def calc():
    talk("tell the function your want to perform")

def google_search(to_search):
    for j in search(to_search, tld="co.in", num=10, stop=10, pause=2):
        print(j)

def run_david():
    command = take_command()
    print(command)

    if 'play' in command: # will play song on youtube
        song = command.replace('play','')
        talk("playing"+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:  # to tell the current time 
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk("The current time is "+time)
    
    elif 'joke' in command:  # random joke
        talk(pyjokes.get_joke())

    elif 'lee' in command:  # lee is gay
        talk("lee is gay.")

    elif 'shutdown' in command:  # to turnoff this
        talk("have a good day")
        exit()

    elif 'calculate' in command:  # to calculate still in process
        print("calculating")
        calc()
    
    elif 'search ' in command:  # will show the links of the topic you'll ask to search 
        to_search = command.replace('search ','')
        talk("searching " + to_search)
        google_search(to_search)
    
    else:   
        talk("can't understand you.")

while True: #will make the david to listen our commands on repeat
    run_david()

