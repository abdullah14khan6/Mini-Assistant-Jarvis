import speech_recognition as sr
import pyttsx3 
import pyaudio
import webbrowser as wb
from datetime import datetime
import time
import random
import os
  
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
    print(f"Processing command: {w}")
    w = cleanCommand(w)
    try:
        if "help" in w or "what can you do" in w:
            speak("You can ask me to open apps, search websites, tell time, and more.")

        if "are you listening" in w:
            speak("yes i am")
            return

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

def main():
    time.sleep(1)
    speak('Initializing Jarvis...')
    run = True
    inner = True
    r = sr.Recognizer()
    r.energy_threshold = 6000  # Lower = more sensitive
    r.dynamic_energy_threshold = True
    
    while run:
        try:
            print('Waiting for wake word...')
            with sr.Microphone() as m:
                print('Say "Jarvis" to wake me up')
                audio = r.listen(m, timeout=5, phrase_time_limit=3)
            
            word = r.recognize_google(audio).lower() # type: ignore
            print(f"Heard: {word}")
            
            with open("jarvis_log.txt", "a") as log: # logging
                log.write(f"{datetime.now()} - Wake word heard: {word}\n")
            
            if any(sleepWord in word for sleepWord in sleepWords):
                speak("Going to sleep. Goodbye!")
                break
                
            if any(wakeWord in word for wakeWord in wakeWords):
                speak(random.choice(startingWords))
                # unknown_count = 0
                timeout_count = 0
                
                while inner:
                    try:
                        with sr.Microphone() as m:
                            print('Jarvis is Listening...')
                            r.adjust_for_ambient_noise(m, duration=1)
                            audio = r.listen(m, timeout=8, phrase_time_limit=5)
                        
                        command = r.recognize_google(audio).lower() # type: ignore
                        print(f"Command received: {command}")
                        with open("jarvis_log.txt", "a") as log: # logging
                            log.write(f"{datetime.now()} - Command: {command}\n")
                        
                        # unknown_count = 0
                        timeout_count = 0
                        
                        if any(sleepWord in command for sleepWord in sleepWords):
                            speak("Going to sleep. Goodbye!")
                            run = False
                            break
                        
                        if any(pauseWord in command for pauseWord in pauseWords):
                            speak("Paused. Say 'Jarvis' or your wake word to resume.")
                            while True:
                                try:
                                    with sr.Microphone() as m:
                                        print('Jarvis is Listening...')
                                        r.adjust_for_ambient_noise(m, duration=1)
                                        audio = r.listen(m, timeout=8, phrase_time_limit=5)
                                    
                                    command = r.recognize_google(audio).lower() # type: ignore
                                    print(f"Command received: {command}")
                                    
                                    with open("jarvis_log.txt", "a") as log: # logging
                                        log.write(f"{datetime.now()} - Command: {command}\n")
                                    
                                    if any(sleepWord in command for sleepWord in sleepWords):
                                        speak("Going to sleep. Goodbye!")
                                        run = False
                                        inner = False
                                        break
                                    
                                    for wakeWord in wakeWords:
                                        if wakeWord in command:
                                            command = command.replace(wakeWord, "").strip()
                                            break

                                except Exception as e:
                                    print(f'Error in command loop: {e}')
                                    continue
                        processCommand(command)
                        
                    # except sr.UnknownValueError:
                    #     unknown_count += 1
                    #     if unknown_count >= 3:
                    #         print("Multiple unclear audio attempts")
                    #         speak("I'm having trouble understanding. Please speak clearly.")
                    #         unknown_count = 0
                    #     continue
                    except sr.WaitTimeoutError:
                        timeout_count += 1
                        print("Listening timeout - continuing to listen...")
                        if timeout_count >= 4:
                            speak("I'm still here. Say something or say 'sleep' to end.")
                            timeout_count = 0 
                        continue
                    except Exception as e:
                        print(f'Error in command loop: {e}')
                        continue
                        
        except sr.WaitTimeoutError:
            print("No wake word detected, continuing to listen...")
            continue
        except sr.UnknownValueError:
            print("Could not understand wake word")
            continue
        except Exception as e:
            print(f'Error in main loop: {e}')
            continue
    
    speak("Session ended. Thanks for using Jarvis!")

# test line
# processCommand("search money can't buy happiness by nick hustles on spotify") 

if __name__ == "__main__":
    main()