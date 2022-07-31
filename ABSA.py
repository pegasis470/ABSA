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
    import pyautogui as pg
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
def submit():
    global txt
    txt=entry.get()
    #print(txt)
    root.destroy()
    root.quit()
def take_input():
    global entry
    global root
    root = Toplevel()
    #root.geometry("600x400")
    root.title("Manual input")
    path=os.path.join(os.getcwd(),"icons","background.png")
    bg=PhotoImage(file=path)
    canvas1 = Canvas(root,width = 600,height = 270)
    canvas1.pack()
    canvas1.create_image(0,0,image= bg, anchor = "nw")
    canvas1.create_text(300,100,text="sorry i didnt get that please type it",fill="white")
    entry=Entry(root)
    button=Button(root,text="submit",command=submit)
    entry_canvas = canvas1.create_window( 125, 150,anchor = "nw",window = entry)
    button_canvas = canvas1.create_window( 230, 200,anchor = "nw",window = button)
    root.mainloop()
    global txt
    print(txt)
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
            txt=''
        except sr.RequestError:
            say("connection error, please check your internet connectin and try again ")
            window.destroy()
            sys.exit(1)
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
            path=os.path.join(os.getcwd(),"music")
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
def reframe_for_god_mode(txt):
        while True:
            if " " in txt:
               txt="".join(txt.split(" "))
            elif "space" in txt:
                txt=txt.replace("space"," ")
                break
            elif " " not in txt and "space" not in txt:
               break
        return txt.lower()
def god_mode():
     say("Initializing god mode....")
     say("say a command line argument")
     argument=reframe_for_god_mode(take_command())
     os.system(f"gnome-terminal")
     time.sleep(2)
     pg.write(argument)
     pg.press("Enter")
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
                elif "open jupyter lab" in command:
                    say("openning jupyterlab")
                    check=program_checker("jupyter-lab")
                    if check == True:
                        os.system("gnome-terminal -e 'jupyter-lab'")
                    else:
                        say("sorry jupyter lab is not installed ")
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
                    say("openning source code")
                    os.system("gnome-terminal -e 'https://github.com/pegasis470/ABSA/blob/main/ABSA.py'")
                elif "open" and "author profile" in command:
                    say("opening sumant dhere's profile")
                    os.system("gnome-terminal -e 'sensible-browser https://www.facebook.com/sumant.dhere.1'")
                    os.system("gnome-terminal -e 'sensible-browser https://www.instagram.com/sdmak_03'")
                    os.system("gnome-terminal -e 'sensible-browser https://github.com/pegasis470'")
                elif "unknown" in command:
                    path_to_improvement=os.path.join(os.getcwd(), "improvement.txt")
                    file = open(path_to_improvement , "r")
                    say("here is a list of unknown commands recived")
                    for line in file.readlines():
                        say(line.strip("\n"))
                    time.sleep(5)
                    file.close()
                elif "God mode" in command :
                    god_mode()
                else:
                ## incase of unclear or invalid command ##
                    say(f"{host} cannot understand. making a note in improvement file")
                    path_to_improvement=os.path.join(os.getcwd(), "improvement.txt")
                    try:
                        improvment = open(path_to_improvement , "r")
                    except FileNotFoundError:
                        file = open(path_to_improvement , "w")
                        file.close()
                        improvement=open(path_to_improvement , "r")
                    if f"{command} \n" in improvment.readlines():
                        say("query already in improvement, It will me added soon!!")
                    else:
                        improvment = open(path_to_improvement , "a+")
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
