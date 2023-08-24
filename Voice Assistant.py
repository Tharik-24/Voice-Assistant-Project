import speech_recognition as sr
import pywhatkit
from gtts import gTTS
from playsound import playsound
import datetime
from wikipedia import*
 


def speech(text):
    print(text)
    language="en"
    output=gTTS(text=text,lang=language,slow=False)

    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")





def get_audio():
    while 1:
        recorder=sr.Recognizer()
        with sr.Microphone()as source:
            print("Listening...")
            audio=recorder.listen(source)

        text=recorder.recognize_google(audio)
        print(text)




        if "Wanda" in text:
            time.sleep(2)
            speech("\tHow May I Help You")
            playsound("./sounds/wav.mp3")

        else:
            break
    return text


    
text=get_audio()



if "youtube" in text.lower():
    speech("okay,i will bring that on youtube for you")
    pywhatkit.playonyt(text)
    
    
elif "joke" in text.lower():
        wikipedia.telljoke(text)


elif "time" in text.lower:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}.")
            
     
        
else:
    speech("Working on it...")
    pywhatkit.search(text)

