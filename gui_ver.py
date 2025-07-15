import speech_recognition as sr
import pyttsx3 
import pyaudio
import webbrowser as wb
from datetime import datetime
import time
import random
import os

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from threading import Thread
from datetime import datetime
  
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
        
    print(f"Processing command: {w}")
    w = cleanCommand(w)
    try:
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
    
    while run:
        try:
            print('Waiting for wake word...')
            
            word = listenCommand(5,3)
            print(f"Heard: {word}")
            
            with open("jarvis_log.txt", "a") as log: # logging
                log.write(f"{datetime.now()} - Wake word heard: {word}\n")
            
            if any(sleepWord in word for sleepWord in sleepWords):
                speak("Going to sleep. Goodbye!")
                command = ""
                break
                
            if any(wakeWord in word for wakeWord in wakeWords):
                speak(random.choice(startingWords))
                unknownCount = 0
                timeoutCount = 0
                while inner:
                    try:
                        print('Jarvis is Listening...')
                        command = listenCommand(8,5)
                        
                        print(f"Command received: {command}")
                        with open("jarvis_log.txt", "a") as log: # logging
                            log.write(f"{datetime.now()} - Command: {command}\n")
                        
                        
                        
                        if any(sleepWord in command for sleepWord in sleepWords):
                            speak("Going to sleep. Goodbye!")
                            run = False
                            command = ""
                            break
                        
                        if any(pauseWord in command for pauseWord in pauseWords):
                            speak("Paused. Say 'Jarvis' or your wake word to resume.")
                            while True:
                                try:
                                    print('Jarvis is Listening...')
                                    
                                    command = listenCommand(5,3)
                                    print(f"Command received: {command}")
                                    
                                    with open("jarvis_log.txt", "a") as log: # logging
                                        log.write(f"{datetime.now()} - Command: {command}\n")
                                    
                                    
                                    if any(sleepWord in command for sleepWord in sleepWords):
                                        speak("Going to sleep. Goodbye!")
                                        run = False
                                        inner = False
                                        command = ""
                                        break
                                    
                                    for wakeWord in wakeWords:
                                        if wakeWord in command:
                                            command = command.replace(wakeWord, "").strip()
                                            break
                                
                                except sr.UnknownValueError:
                                    print("Could not understand")
                                    unknownCount += 1
                                    if unknownCount >= 3:
                                        print("Multiple unclear audio attempts")
                                        speak("I'm having trouble understanding. Please speak clearly.")
                                        unknownCount = 0
                                    continue
                                except Exception as e:
                                    print(temp := f'paused Error in command loop: {e}')
                                    with open("jarvis_log.txt", "a") as log: # logging
                                        log.write(f"{datetime.now()} - Except: {temp}\n")
                                    continue
                        processCommand(command)
                        
                    # except sr.UnknownValueError:
                    #     unknownCount += 1
                    #     if unknownCount >= 3:
                    #         print("Multiple unclear audio attempts")
                    #         speak("I'm having trouble understanding. Please speak clearly.")
                    #         unknownCount = 0
                    #     continue
                    except sr.WaitTimeoutError:
                        timeoutCount += 1
                        print("Listening timeout - continuing to listen...")
                        if timeoutCount >= 4:
                            speak("I'm still here. Say something or say 'sleep' to end.")
                            timeoutCount = 0 
                        continue
                    except Exception as e:
                        print(temp:=f'Error in command loop: {e}')
                        with open("jarvis_log.txt", "a") as log: # logging
                            log.write(f"{datetime.now()} - Except: {temp}\n")
                        continue
                        
        
            print(temp:="No wake word detected, continuing to listen...")
            with open("jarvis_log.txt", "a") as log: # logging
                log.write(f"{datetime.now()} - Except: {temp}\n")
            continue
        except sr.UnknownValueError:
            print("Could not understand wake word")
            continue
        except Exception as e:
            print(temp:= f'Error in main loop: {e}')
            with open("jarvis_log.txt", "a") as log: # logging
                log.write(f"{datetime.now()} - Except: {temp}\n")
            continue
    
    speak("Session ended. Thanks for using Jarvis!")
    with open("jarvis_log.txt", "a") as log: # logging
        log.write(f"-----SESSION END-----")

# test line
# processCommand("search money can't buy happiness by nick hustles on spotify") 

BG_COLOR = "#0f111a"
FG_COLOR = "#ffffff"
ACCENT_COLOR = "#00f0ff"
HEADER_FONT = ("Segoe UI", 20, "bold")
TEXT_FONT = ("Consolas", 12)
LOG_FONT = ("Fira Code", 10)

class JarvisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis - Voice Assistant")
        self.root.geometry("700x600")
        self.root.configure(bg=BG_COLOR)

        self.listening = False
        self.thread = None

        # Header
        self.title = tk.Label(
            root, text="⦿ JARVIS", font=HEADER_FONT,
            fg=ACCENT_COLOR, bg=BG_COLOR
        )
        self.title.pack(pady=15)

        # Mic Status Circle
        self.canvas = tk.Canvas(root, width=80, height=80, bg=BG_COLOR, highlightthickness=0)
        self.status_circle = self.canvas.create_oval(10, 10, 70, 70, fill="gray20")
        self.canvas.pack()

        # Command Box
        self.cmd_label = tk.Label(root, text="Last Command:", font=("Segoe UI", 12), fg=FG_COLOR, bg=BG_COLOR)
        self.cmd_label.pack(pady=(20, 5))

        self.cmd_display = tk.Text(root, height=2, font=TEXT_FONT, fg=ACCENT_COLOR, bg="#1c1f2e", bd=0, relief=tk.FLAT)
        self.cmd_display.pack(fill="x", padx=40, pady=(0, 10))
        self.cmd_display.configure(state="disabled")

        # Log Area
        self.log_label = tk.Label(root, text="Jarvis Log:", font=("Segoe UI", 12), fg=FG_COLOR, bg=BG_COLOR)
        self.log_label.pack(pady=(10, 0))

        self.log_box = scrolledtext.ScrolledText(
            root, font=LOG_FONT, wrap=tk.WORD, height=15, bg="#1c1f2e", fg="#b8e0f9", bd=0, relief=tk.FLAT
        )
        self.log_box.pack(fill="both", padx=40, pady=(0, 10))
        self.log_box.configure(state="disabled")

        # Control Button
        self.control_btn = tk.Button(
            root, text="▶ Start Listening", command=self.toggle_listen,
            font=("Segoe UI", 12, "bold"), bg=ACCENT_COLOR, fg="black",
            activebackground="#03d0dd", activeforeground="white", relief=tk.FLAT, padx=10, pady=5
        )
        self.control_btn.pack(pady=10)

        # Status
        self.status_label = tk.Label(root, text="Status: Idle", font=("Segoe UI", 10), fg="gray", bg=BG_COLOR)
        self.status_label.pack()

    def toggle_listen(self):
        if not self.listening:
            self.listening = True
            self.control_btn.config(text="■ Stop Listening", bg="#ff4c4c")
            self.set_status("Listening...")
            self.thread = Thread(target=self.run_jarvis)
            self.thread.daemon = True
            self.thread.start()
        else:
            self.listening = False
            self.control_btn.config(text="▶ Start Listening", bg=ACCENT_COLOR)
            self.set_status("Idle")
            self.set_mic_color("gray20")

    def log(self, msg):
        self.log_box.configure(state="normal")
        timestamp = datetime.now().strftime("[%H:%M:%S] ")
        self.log_box.insert(tk.END, timestamp + msg + "\n")
        self.log_box.configure(state="disabled")
        self.log_box.see(tk.END)

    def update_command(self, command):
        self.cmd_display.configure(state="normal")
        self.cmd_display.delete("1.0", tk.END)
        self.cmd_display.insert(tk.END, command)
        self.cmd_display.configure(state="disabled")

    def set_status(self, status):
        self.status_label.config(text=f"Status: {status}")
        if status == "Listening...":
            self.set_mic_color("#00ffcc")
        elif status == "Idle":
            self.set_mic_color("gray20")
        elif status == "Processing":
            self.set_mic_color("orange")

    def set_mic_color(self, color):
        self.canvas.itemconfig(self.status_circle, fill=color)

    def run_jarvis(self):
        speak("Jarvis GUI initialized.")
        while self.listening:
            try:
                self.log("Waiting for wake word...")
                self.set_status("Listening...")
                word = listenCommand(5, 3)
                self.update_command(word)
                self.log(f"Heard: {word}")

                if any(w in word for w in sleepWords):
                    speak("Shutting down.")
                    self.log("Jarvis sleeping...")
                    self.toggle_listen()
                    return

                if any(w in word for w in wakeWords):
                    speak(random.choice(startingWords))
                    while self.listening:
                        try:
                            self.set_status("Listening...")
                            command = listenCommand(8, 5)
                            self.set_status("Processing")
                            self.update_command(command)
                            self.log(f"Command: {command}")

                            if any(w in command for w in sleepWords):
                                speak("Going to sleep. Goodbye!")
                                self.toggle_listen()
                                return

                            processCommand(command)
                        except sr.WaitTimeoutError:
                            self.log("Timeout. Listening again...")
                            continue
                        except Exception as e:
                            self.log(f"Error: {e}")
                            continue
            except sr.UnknownValueError:
                self.log("Could not understand wake word.")
                continue
            except Exception as e:
                self.log(f"Critical error: {e}")
                break


if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisGUI(root)
    root.mainloop()