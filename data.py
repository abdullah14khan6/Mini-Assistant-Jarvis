import os
import win32com.client

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

downloadable_apps = {
    # Browsers
    "Google Chrome", "Mozilla Firefox", "Microsoft Edge",

    # Media
    "VLC Media Player", "PotPlayer",

    # PDF & Documents
    "Adobe Acrobat Reader", "SumatraPDF",

    # Compression Tools
    "7-Zip", "WinRAR",

    # Cloud & Backup
    "Google Drive", "Dropbox", "OneDrive",

    # Messaging & Calls
    "WhatsApp Desktop", "Telegram", "Discord",
    "Zoom", "Skype", "Microsoft Teams", "Google Meet",

    # Security
    "Windows Defender", "Malwarebytes", "Avast",

    # Clipboard & Productivity
    "Ditto", "ClipboardFusion",

    # Notes & Study
    "Notion", "Evernote", "Anki", "Grammarly Desktop",

    # Office Tools
    "Microsoft Word", "Microsoft Excel", "Microsoft PowerPoint",
    "LibreOffice", "WPS Office", "PDF-XChange Editor",

    # Developer Tools
    "Visual Studio Code", "Visual Studio", "PyCharm", "IntelliJ IDEA",
    "Git", "GitHub Desktop", "Docker Desktop", "Postman",
    "Node.js", "Python", "Java JDK", "XAMPP", "Android Studio",

    # Design & Creative
    "Adobe Photoshop", "Adobe Illustrator", "Figma Desktop", "Canva Desktop",
    "Adobe Premiere Pro", "DaVinci Resolve", "Audacity", "Blender",

    # Gaming & Streaming
    "Steam", "Epic Games Launcher", "OBS Studio", "GeForce Experience",

    # System Utilities
    "CCleaner", "Everything", "Rufus", "PowerToys",
    "Speccy", "HWMonitor", "CrystalDiskInfo"
}

start_menu_dirs = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs")
]

shell = win32com.client.Dispatch("WScript.Shell")

for dir_path in start_menu_dirs:
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".lnk"):
                shortcut_path = os.path.join(root, file)
                shortcut = shell.CreateShortcut(shortcut_path)
                target_path = shortcut.Targetpath
                app_name = file.replace(".lnk", "").lower()
                apps[app_name] = target_path

apps = {name: path for name, path in apps.items() if name in downloadable_apps}

print(apps)