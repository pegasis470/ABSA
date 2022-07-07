# !/bin/python3
# MIT License
# (c) pegasis470 (Sumant Dhere) <www.sumantdhere@gamil.com>
import os
try: 
    import wikipedia
    import pyttsx3
    import speech_recognition as sr
    import sys
    import time
    import socket
    import vlc
    import getpass
    import random 
    import time
    from tkinter import *
    from PIL import ImageTk, Image
    import subprocess
    from datetime import datetime as dt
except ModuleNotFoundError:
    print("some modules are missing installing them now")
    os.system("pip install wikipedia pyttsx3 SpeechRecognition ")


host = socket.gethostname()
user = getpass.getuser()
current_time = dt.now().hour
loop_main=2
r = sr.Recognizer()
engine=pyttsx3.init()
engine.setProperty('rate',167)


def say(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
def save_and_close():
    global txt
    txt=entry.get()
def take_input():
    global entry
    global root
    root = Tk()
    root.title("Manual input")
    root['background']='#219882'
    label=Label(root,text="sorry i didnt get that please type it",background='#219882')
    entry=Entry(root)
    button=Button(root,text="submit",background='#219882',command=lambda:[save_and_close(),root.quit(),root.destroy()])
    label.pack()
    entry.pack()
    button.pack()
    root.mainloop()
    return txt
def take_command():
    say("Listening....")
    try:
        test=sr.Microphone()
    except AttributeError:
        say("An AttributeError has been raised attempting to correct by installing a package NOTE :- please enter password below if needed")
        time.sleep(2)
        os.system("gnome-terminal -e 'sudo apt install python3-pyaudio'")

    with sr.Microphone() as source:
        try:
            r.pause_threshold = 0.5
            audio = r.listen(source)
            query=" "
            say ("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            say(f"user said, {query}")
        except sr.UnknownValueError:
            say("Sorry i didnt get that please type it")
            query=take_input()
        except sr.RequestError:
            say("connection error, please check your internet connectin and try again ")
            query = 'failed'
        return query


def program_checker(program):
    """ taken from https://geekflare.com/learn-python-subprocess/ """
    process = subprocess. run(['which', program], capture_output=True, text=True)
    if process.returncode == 0:
        return True
    else:
        return False
def music():
    say("Initializing media player....")
    path=os.path.join( os.path.expanduser('~'),"Music")
    say(f"scanning user music at {path}")
    play =2
    files=os.listdir(path)
    while play <3 :
        try:
            mp3_files=[]
            all_files=os.listdir(path)
            for files in all_files:
                f=files.split('.')[-1]
                if f == "mp3":
                    mp3_files.append(files)
            d=random.choice(mp3_files)
        except IndexError:
            say("no music found in defalt directory ")
            say("changing search path to inbuilt music ")
            path=os.path.join(os.getcwd(),"ABSA","music")
            say("succes")
            mp3_files=[]
            all_files=os.listdir(path)
            for files in all_files:
                f=files.split('.')[-1]
                if f == "mp3":
                    mp3_files.append(files)
            d=random.choice(mp3_files)
        final_path=os.path.join(path ,d)
        say(f"now playing {d}")
        path_to_in = os.path.join(path,"in.txt")
        os.system(f'ffprobe -i "{final_path}" -show_entries format=duration -v quiet -of csv="p=0" > {path_to_in}')
        f=open(os.path.join(path,"in.txt"),"r")
        text=f.read()
        text=text.rstrip('\n')
        sec=int(float(text))
        p = vlc.MediaPlayer(final_path)
        p.play()
        time.sleep(sec)
        p.stop()
        f.close()
        say("play next")
        say("yes or no")
        agian=take_command()
        if 'no' in agian.split(' ') :
            music_window.destroy()
            say("keep vibing")
            music_window.quit()
            break
        else:
            pass
def search():
            say("Initializing cincinati....")
            say("say what to search")
            query=take_command()
            while True:

            ### acces the web ###
                try:
                    say("Searching")
                    results = wikipedia.summary(query, sentences=2)
                except wikipedia.DisambiguationError:
                    say(f"{query} not found,try another word.")
                    results=""
                except wikipedia.exceptions.PageError:
                    say(f"{query} not found, {query} dosent match anything on the web.")
                    results=""
                try:
                    say("i found")
                    say (results)
                except NameError:
                    say("SORRY ")
                say("can I search anything else?")
                query2=take_command()
                if "no" or "no " or "not really" or "not really " in query2 :
                    say("cincinati out")
                    search_window.destroy()
                    search_window.quit()
                    break
                else:
                    query=query2
                    continue


def  main():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if current_time >= 0 and current_time < 12:
                    say(f"Good Morning ")
            elif current_time >= 12 and current_time < 18:
                    say("Good Afternoon ")
            else:
                    say("Good Evening")
            say("welcome to ABSA")
            say(f"host name = {host}")
            say(f"welcome {user} sir")
            say("how can I be of assistance")
            
            command=take_command()
            while True:
                #small talk#
                #system commands#
                if "restart" in command :
                    say("please comfirm restart by saying yes")
                    confirm=take_command()
                    if confirm=="yes":
                        say("execunting restat")
                        os.system("reboot")
                    else:
                        say("process aborted")
                elif "shutdown" in command :
                    say("please comfirm shutdown by saying yes")
                    confirm=take_command()
                    if confirm=="yes":
                        say("execunting shutdown")
                        os.system("poweroff")
                    else :
                        say("process aborted")
                elif "open settings" in command:
                        say("opening settings")
                        os.system("gnome-terminal -e 'gnome-control-center'")
                elif "open task manager" in command :
                        say("openning taskmanager")
                        os.system("gnome-terminal -e 'gnome-system-monitor'")
                elif "open calculator" in command:
                        say("openning calculator")
                        os.system("gnome-terminal -e 'gnome-calculator'")
        # openning installed applications #
                elif "open browser" in command:
                ## opens defalt browser ## 
                        say("openning default browser")
                        os.system("gnome-terminal -e 'sensible-browser'")
                elif "open Brave" in command:
                    say("opening brave")
                    check=program_checker("brave")
                    if check == True:
                        os.system("gnome-terminal -e 'brave'")
                    else:
                        say("Sorry brave is not installed")
        ## directily opening websites in defalt browser ##
                elif "open YouTube" in command:
                    say("opening youtube in defalt browser")
                    os.system( "gnome-terminal -e 'sensible-browser http://www.youtube.com'")
                elif "open Instagram" in command:
                    say("openning instagram in defalt browser")
                    os.system("gnome-terminal -e 'sensible-browser http:://www.instagram.com'")
        ## open websites in brave if installed ##
                elif "YouTube" and "brave" in command:
                    say("opening youtube in brave browser")
                    check=program_checker("brave")
                    if check == True:
                        os.system( "gnome-terminal -e 'brave http://www.youtube.com'")
                    else:
                        say("Sorry brave is not installed")
                elif "Instagram" and "brave" in command:
                    say("opening instagram in brave browser")
                    check=program_checker("brave")
                    if check == True:
                        os.system( "gnome-terminal -e 'brave http://www.instagram.com'")
                    else:
                        say("Sorry brave is not installed")
        ## these are personal commands based on my usage ##
                elif "open Google meet" in command:
                    say("openning google meet in brave")
                    os.system("gnome-terminal -e 'sensible-browser -window https://meet.google.com/'")
                elif "open Google duo" in command:
                    say("openning google duo")
                    os.system("gnome-terminal -e 'sensible-browser https://duo.google.com/?web&utm_source=marketing_page_button_top'")
        ## other apps ##
                elif "open telegram" in command:
                    say("openning telegram")
                    check=program_checker("telegram-desktop")
                    if check==True:
                        os.system("gnome-terminal -e 'telegram-desktop'")
                    else:
                        say("sorry telegram is not installed")
                elif "open WhatsApp" in command:
                    say("openning whats app")
                    check=program_checker("whatsie")
                    if check==True:
                        os.system("gnome-terminal -e 'whatsie'")
                    else:
                        say("sorry whatsie whatsapp client is not installed")
                elif "open droidcam" in command :
                    say("openning droidcam")
                    check=program_checker("droidcam")
                    if check == True:
                        os.system("gnome-terminal -e 'droidcam'")
                    else:
                        say("sorry droidcam is not installed")
                elif "open droidcam client" in command:
                    say("openning droidcam")
                    check=program_checker("droidcam")
                    if check == True:
                        os.system("gnome-terminal -e 'droidcam-cli 192.168.29.175 4747'")
                    else:
                        say("Sorry droidcam is not installed")
                elif "open jupyter lab" in command:
                    say("openning jupyterlab")
                    check=program_checker("jupyter-lab")
                    if check == True:
                        os.system("gnome-terminal -e 'jupyter-lab'")
                    else:
                        say("sorry jupyter lab is not installed ")
                elif command == "open source code in edit":
                    say("opening source code with vim")
                    os.system("vim ABSA.py")
                elif "open terminal" in  command:
                    say("openning new terminal window")
                    os.system("gnome-terminal")
        # other #
                elif "search" in command:
                    global search_window
                    search_window=Toplevel()
                    path=os.path.join(os.getcwd(),"icons","search.png")
                    search_img = ImageTk.PhotoImage(Image.open(path))
                    search_label=Label(search_window,image=search_img)
                    search_label.pack()
                    search_window.after(500,search)
                    search_window.mainloop()
           # cincinati is done executing , back to sdmak #
                elif "play" and "music" in command:
                    global music_window
                    music_window = Toplevel()
                    path=os.path.join(os.getcwd(),"icons","music.png")
                    music_img = ImageTk.PhotoImage(Image.open(path))
                    music_label=Label(music_window,image=music_img)
                    music_label.pack()
                    music_window.after(500,music)
                    music_window.mainloop()

                elif "open" and "source code" in command:
                    say("authorization required")
                    auth=take_command()
                    if auth == user :
                        say("authorization confirmed Opennig source code")
                        os.system("gedit ABSA.py")
                    else:
                        say("authorization failed")
                elif "open" and "author profile" in command:
                    say("opening sumant dhere's profile")
                    os.system("gnome-terminal -e 'sensible-browser https://www.facebook.com/sumant.dhere.1'")
                    os.system("gnome-terminal -e 'sensible-browser https://www.instagram.com/sdmak_03'")
                    os.system("gnome-terminal -e 'sensible-browser https://github.com/pegasis470'")
                elif "unknown" in command:
                    path_to_improvement=os.path.join(os.getcwd(), "improvement.txt")
                    file = open(path_to_improvement , "r")
                    say("here is a list of unknown commands recived")
                    print(file.read())
                    time.sleep(5)
                    file.close()
                elif command == 'failed':
                    sys.exit()
                else:
                ## incase of unclear or invalid command ##
                    say(f"{host} cannot understand. making a note in improvement file")
                    path_to_improvement=os.path.join(os.getcwd(), "improvement.txt")
                    improvment = open(path_to_improvement , "a+")
                    if f"{command} \n" in improvment.readlines():
                        say("query already in improvement, It will me added soon!!")
                    else:
                        improvment.write(f"{command} \n")
                    improvment.close()

                say("can I help with anything else?")
                #### continue or break loop ####
                end=take_command()
                if 'no' in end.split(' ')[0] :
                    say("happy to help")
                    sys.exit(0)
                else:
                    command=end
                    continue
path=os.path.join(os.getcwd(),"icons","main.png")
window= Tk()
window.after(500,main)
window.title("ABSA")
img = ImageTk.PhotoImage(Image.open(path))
label = Label(window, image = img)
label.pack()
window.mainloop()
