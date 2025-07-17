# Mini Voice Assistant - Jarvis

A **Python-based voice assistant** that listens to your commands and performs smart tasks — from opening websites and apps to searching the web, playing music, and more.

This is my **first major Python project**, and it's been a challenging yet fulfilling learning journey after coding primarily in C++. Through this, I not only explored key Python modules but also picked up professional coding practices like error handling, logging, modular structure, and even dabbled with GUI tools.

---

## Features

- 🎙️ **Voice-activated Commands**  
  Activate Jarvis by saying "Jarvis" and speak naturally.

- 🌐 **Smart Web Search**
  Ask things like:  
  > *"search history of pakistan on wikipedia"*  
  > *"search bayyan at spotify"*  
  > *"search chat gpt on google"*

- 🖥️ **Open Local Applications**  
  Launch apps like Calculator, Word, Photoshop, VS, etc. with your voice.

- 🧠 **Platform Awareness**  
  Knows where to search depending on the website/platform mentioned.

- 📋 **Activity Logging**  
  Everything is logged in `jarvis_log.txt`:  
  - Chat sessions (commands & responses)  
  - Wake/sleep states  
  - All exceptions for later debugging

- ⚙️ **Robust Exception Handling**  
  All exceptions are gracefully handled and logged — keeping Jarvis stable even when unexpected errors occur.

---

## 📦 Project Structure

```bash
.
├── jarvis.py          # Main assistant logic (speech, commands, app/web handling)
├── gui_ver.py         # GUI version (experimental using Tkinter)
├── requirements.txt   # All dependencies
├── transcript.txt     # Sample interaction log from a real session
├── .gitignore
```

---

## 🪟 GUI Version
I also developed a basic **GUI interface** *(gui_ver.py)* with the help of AI tools.
Even though I didn’t know Tkinter before, this experience **inspired me to learn it properly**, and I’m looking forward to building more interactive Python apps!

```
Wake word heard: jarvis
Assistant: hello
Command: open calculator app
Assistant: Opening calculator

Command: search bayan at spotify
Assistant: searching bayan on spotify

Command: search today pakistani rupees to usd on google
Assistant: searching today pakistani rupees to usd on google
```

---

## 🛠 Installation
**🔧 Requirements**
  Install the dependencies using pip:
  ```bash
  pip install virtualenv
  virtualenv venv
  .\venv\Scripts\activate
  
  pip install -r requirements.txt
  ```

---

## 🧠 Lessons Learned
- Python's dynamic typing, exception handling, and module usage
  
- Real-world debugging and log analysis

- How to create CLI/GUI-based assistants

- Building search automation across dozens of platforms

- How much I love voice + AI-based interfaces!

---

## 🤝 Contributions Welcome!
I'm just getting started in Python and AI — so I’m open to **feedback, advice, code suggestions, or even feature ideas**.
Feel free to open issues or pull requests — your input is welcome!