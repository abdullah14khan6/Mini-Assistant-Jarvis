import speech_recognition as sr
import pyttsx3 
import pyaudio
import webbrowser as wb
from datetime import datetime
import time
import random
import os
import threading
  
startingWords = ['ya', 'what can i do for you today', 'hi', 'hello', 'yup', 'hmmm']
sleepWords = {"end jarvis", "exit", "bye", "sleep jarvis", "bye jarvis", "end", "terminate jarvis", "terminate" , "ok bye", "sleep", "sleep jarvis"}
wakeWords = {"jarvis", "hey jarvis", "hello jarvis", "hi jarvis", "heya jarvis"}
pauseWords = {"pause", "stop", "quiet", "shut up", "stop talking", "pause jarvis", "stop jarvis"}

webpages = {
    "google": "https://www.google.com",
    "wikipedia": "https://www.wikipedia.org",
    "youtube": "https://www.youtube.com",
    "quora": "https://www.quora.com",
    "stack overflow": "https://stackoverflow.com",
    "reddit": "https://reddit.com",
    "gmail": "https://mail.google.com",
    "outlook": "https://outlook.live.com",
    "whatsapp": "https://web.whatsapp.com",
    "discord": "https://discord.com/app",
    "telegram": "https://web.telegram.org",
    "khan academy": "https://www.khanacademy.org",
    "coursera": "https://www.coursera.org",
    "edx": "https://www.edx.org",
    "chatgpt": "https://chat.openai.com",
    "geeks for geeks": "https://www.geeksforgeeks.org",
    "w3schools": "https://www.w3schools.com",
    "leetcode": "https://leetcode.com",
    "hackerrank": "https://www.hackerrank.com",
    "codeforces": "https://codeforces.com",
    "linkedin": "https://www.linkedin.com",
    "upwork": "https://www.upwork.com",
    "fiverr": "https://www.fiverr.com",
    "indeed": "https://www.indeed.com",
    "google colab": "https://colab.research.google.com",
    "github": "https://github.com",
    "hugging face": "https://huggingface.co",
    "papers with code": "https://paperswithcode.com",
    "spotify": "https://open.spotify.com"
}

apps = {
    "calculator": "calc.exe",
    "command prompt": "cmd.exe",
    "task manager": "taskmgr.exe",
    "control panel": "control.exe",
    "notepad": "notepad.exe",
    "snipping tool": "snippingtool.exe",
    "word": "C://Program Files//Microsoft Office//root//Office16//WINWORD.EXE",
    "powerpoint": "C://Program Files//Microsoft Office//root//Office16//POWERPNT.EXE",
    "excel": "C://Program Files//Microsoft Office//root//Office16//EXCEL.EXE",
    "visual studio": "C://Program Files//Microsoft Visual Studio//2022//Community//Common7//IDE//devenv.exe",
    "illustrator": "C://Program Files//Adobe//Adobe Illustrator 2025//Support Files//Contents//Windows//Illustrator.exe",
    "photoshop": "C://Program Files//Adobe//Adobe Photoshop 2025//Photoshop.exe",
}

r = sr.Recognizer()
r.energy_threshold = 6000  # Lower = more sensitive
r.dynamic_energy_threshold = True
mic = sr.Microphone()

def speak(w):
    try:
        engine = pyttsx3.init() # only works if the engine is reinitialized every call
        engine.setProperty('rate', 150) 
        engine.setProperty('volume', 0.9)
        engine.say(w)
        engine.runAndWait()
        time.sleep(0.1)
        with open("jarvis_log.txt", "a") as log: # logging
            log.write(f"{datetime.now()} - Assistant: {w}\n")
    except Exception as e:
        print(f"Error in speak function: {e}")

def listenCommand(TO, PTL):
    with sr.Microphone() as m:
        r.adjust_for_ambient_noise(m, duration=1)
        audio = r.listen(m, timeout=TO, phrase_time_limit=PTL)
    return r.recognize_google(audio).lower() # type: ignore
        
def searchWebsite(search, site="google"):
    try:
        query = search.replace(" ", "+")
        searchUrls = {
            "google": f"https://www.google.com/search?q={query}",
            "youtube": f"https://www.youtube.com/results?search_query={query}",
            "wikipedia": f"https://en.wikipedia.org/wiki/Special:Search?search={query}",
            "quora": f"https://www.quora.com/search?q={query}",
            "stack overflow": f"https://stackoverflow.com/search?q={query}",
            "spotify": f"https://open.spotify.com/search/{query}",
            "reddit": f"https://www.reddit.com/search/?q={query}",

            "bing": f"https://www.bing.com/search?q={query}",
            "duckduckgo": f"https://duckduckgo.com/?q={query}",
            "brave": f"https://search.brave.com/search?q={query}",

            "github": f"https://github.com/search?q={query}",
            "geeksforgeeks": f"https://www.geeksforgeeks.org/?s={query}",
            "w3schools": f"https://www.w3schools.com/howto/howto_js_search_menu.asp?q={query}",
            "khan academy": f"https://www.khanacademy.org/search?page_search_query={query}",
            "coursera": f"https://www.coursera.org/search?query={query}",

            "amazon": f"https://www.amazon.com/s?k={query}",
            "daraz": f"https://www.daraz.pk/catalog/?q={query}",
            "ebay": f"https://www.ebay.com/sch/i.html?_nkw={query}",

            "netflix": f"https://www.netflix.com/search?q={query}",
            "imdb": f"https://www.imdb.com/find?q={query}",

            "unsplash": f"https://unsplash.com/s/photos/{query}",
            "pexels": f"https://www.pexels.com/search/{query}",
            "dribbble": f"https://dribbble.com/search/{query}",
            "behance": f"https://www.behance.net/search/projects?search={query}",

            "arxiv": f"https://arxiv.org/search/?query={query}&searchtype=all",
            "huggingface": f"https://huggingface.co/search/full-text?q={query}",
            "openai": f"https://platform.openai.com/docs/search?q={query}"
        }

        
        if site in searchUrls:
            speak(f"searching {search} on {site}")
            wb.open(searchUrls[site])
        else:
            speak(f"Sorry, I don't know how to search on {site}")
    except Exception as e:
        print(f"Error in searchWebsite: {e}")
        speak("Sorry, I couldn't perform the search")

def cleanCommand(cmd):
    filler_phrases = {
        "for me", "please", "can you", "could you", "would you",
        "i want you to", "i need you to", "kindly", "will you", "would you kindly",
        "can u", "could u", "would u"
    }
    
    cmd = cmd.lower()
    for phrase in filler_phrases:
        cmd = cmd.replace(phrase, "")
    
    return cmd.strip()

def processCommand(w):
    if w == "":
        return
    if "help" in w or "what can you do" in w:
        speak("You can ask me to open apps, search websites, tell time, and more.")
        commandLoop()
        
    print(f"Processing command: {w}")
    w = cleanCommand(w)
    try:
        if "are you listening" in w:
            speak("yes i am")
            commandLoop()

        if "time" in w:
            now = datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")
            return

        elif "date" in w:
            today = datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today is {today}")
            return
        
        elif ("play" in w or "search" in w) and ("on" in w or "at" in w):
            if "on" in w:
                parts = w.split(" on ")  
            elif "at" in w:
                parts = w.split(" at ")
            else:
                parts = [w,]
                
            if len(parts) == 2:
                search = parts[0].replace("search", "").replace("play", "").strip()
                site = parts[1].strip()
                searchWebsite(search, site)
                return
        
        elif "search" in w:
            search = w.replace("search", "").strip()
            if search:
                searchWebsite(search)
                return
        
        elif any(keyword in w for keyword in {"application", "app"}):
            appFound = False
            for app in apps:
                if app in w:
                    try:
                        speak(f"Opening {app}")
                        os.startfile(apps[app])
                        
                        os.startfile(apps[app])
                        appFound = True
                        break
                    except Exception as e:
                        print(f"Error opening {app}: {e}")
                        speak(f"Sorry, I couldn't open {app}")
                        appFound = True
                        break
            
            if not appFound:
                speak("I couldn't find that application")
            return
        
        else:
            siteFound = False
            for site in webpages:
                if site in w:
                    speak(f"Opening {site}")
                    wb.open(webpages[site])
                    siteFound = True
                    break
            
            if not siteFound:
                speak("I couldn't understand. Try rephrasing or say 'help'")
                
    except Exception as e:
        print(f"Error in processCommand: {e}")
        speak("Sorry, I encountered an error processing your command")

def commandLoop():
    global flag
    run = True

    while run:
        try:
            print('Jarvis is Listening...')
            command = listenCommand(8, 5).replace('-', ' ')
            
            print(f"Command received: {command}")
            with open("jarvis_log.txt", "a") as log:  # logging
                log.write(f"{datetime.now()} - Command: {command}\n")

            if any(sleepWord in command for sleepWord in sleepWords):
                speak("Going to sleep. Goodbye!")
                run = False
                command = ""
                break
                
            if "destruct" in command:
                speak("Shutting down. Goodbye!")
                command = ""
                flag = False
                run = False
                return
            
            if any(pauseWord in command for pauseWord in pauseWords):
                speak("Paused. Say 'Jarvis' or your wake word to resume")
                return

            processCommand(command)

        except sr.UnknownValueError:
            with open("jarvis_log.txt", "a") as log:  # logging
                log.write(f"{datetime.now()} - Except: Gibbrish\n")
            speak("Sorry... couldn't understand what you said. Can you please repeat")
            continue
        except sr.WaitTimeoutError:
            with open("jarvis_log.txt", "a") as log:  # logging
                log.write(f"{datetime.now()} - Except: timed out\n")
            print("back to background listening")
            return
        except Exception as e:
            temp = f'Error in command loop: {e}'
            print(temp)
            with open("jarvis_log.txt", "a") as log:  # logging
                log.write(f"{datetime.now()} - Except: {temp}\n")
            speak("Sorry... Encountered an error. Can you please repeat")
            continue      

def wakeWordCallback(r, mic):
    global stopListening
    global flag
    try:
        word = r.recognize_google(mic).lower() # type: ignore
        
        print(f"Heard: {word}")
                
        if "destruct" in word:
            speak("Shutting down. Goodbye!")
            flag = False
            return
        
        if any(sleepWord in word for sleepWord in sleepWords):
            return
            
                    
        if any(wakeWord in word for wakeWord in wakeWords):
            speak(random.choice(startingWords))
            
            with open("jarvis_log.txt", "a") as log: # logging
                log.write(f"{datetime.now()} - Wake word heard: {word}\n")
                
            def handler(): # used this handler because if we donot use it the stop listening throws an exception and tries to terminate the current thread too
                stopListening() # stops the background listening thread
                commandLoop() # runs the inner command identifying logic
                start() # after the command loop returns it continues listening for the wake word

            threading.Thread(target=handler).start() # starts the handler thread

            # stopListening() # stops the background listening thread
            # commandLoop() # runs the inner command identifying logic
            # start() # after the command loop returns it continues listening for the wake word
    
    except sr.UnknownValueError:
        with open("jarvis_log.txt", "a") as log:  # logging
            log.write(f"{datetime.now()} - Except: Gibbrish\n")

    except Exception as e:
        temp = f'Error in Wake Word Callback: {e}'
        print(temp)
        with open("jarvis_log.txt", "a") as log:  # logging
            log.write(f"{datetime.now()} - Except: {temp}\n")

def start():
    global stopListening # an object of function which is global and uses concept of closures in python to stop the background listening thread 
    stopListening = r.listen_in_background(mic, wakeWordCallback)
    pass

def main():
    global flag
    flag = True
    with open("jarvis_log.txt", "a") as log: # logging
        log.write(f"-----SESSION STARTED-----\n\n")
        
    time.sleep(1)
    speak('Initializing Jarvis...')
    print("Waiting for wake word!")
    
    start()
    
    try:
        while flag:
            time.sleep(0.1)  # Keep the main thread alive
    except KeyboardInterrupt:
        speak("Session ended. Thanks for using Jarvis!")
        
    with open("jarvis_log.txt", "a") as log:
            log.write(f"\n-----SESSION END-----\n\n")

# test line
# processCommand("search money can't buy happiness by nick hustles on spotify") 

if __name__ == "__main__":
    main()