# !/bin/python3
# GNU General Public License v3.0-or-later
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
    engine.say(text)
    engine.runAndWait()
def take_command():
    print("Listening....")
    say("Listening....")
    try:
        test=sr.Microphone()
    except AttributeError:
        print("An AttributeError has been raised attempting to correct by installing a package NOTE :- please enter password below if needed")
        say("An AttributeError has been raised attempting to correct by installing a package NOTE :- please enter password below if needed")
        time.sleep(2)
        os.system("sudo apt install python3-pyaudio")

    with sr.Microphone() as source:
        try:
            r.pause_threshold = 0.5
            audio = r.listen(source)
            query=" "
            print("Recognizing....")
            say ("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print("user said",query)
            say(f"user said, {query}")
        except sr.UnknownValueError:
                print("sorry I didnt get that please type it:")
                query=input("")
        except sr.RequestError:
            print("connection error, please check your internet connection and try again ")
            say("connection error, please check your internet connectin and try again ")
            query = 'failed'
        return query
print("welcom to ABSA")
print("host name  =",host)
say("welcome to absa")
say(f"host name = {host}")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if current_time >= 0 and current_time < 12:
    print(f"Good Morning {user} sir ")
    say(f"Good Morning {user} sir ")
elif current_time >= 12 and current_time < 18:
    print(f"Good Afternon {user} sir ")
    say(f"Good Afternoon {user} sir ")
else:
    print(f"Good Evening {user} sir ")
    say(f"Good Evening {user} sir ")

print("how can I be of assistance")
say("how can i be of assistance")
    
command=take_command()

while loop_main < 3 :
# system actions # 
    if "restart" in command :
        say("please comfirm restart by saying yes")
        print("please confirm restart by saying 'yes'")
        confirm=take_command()
        if confirm=="yes":
            say("execunting restat")
            print("executing restart")
            os.system("reboot")
        else :
            print("process aborted")
            say("process aborted")
    elif "shutdown" in command :
        say("please comfirm shutdown by saying yes")
        print("please confirm shutdown by saying 'yes'")
        confirm=take_command()
        if confirm=="yes":
            say("execunting shutdown")
            print("executing shutdown")
            os.system("poweroff")
        else :
            print("process aborted")
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
        print("openning brave")
        say("opening brave")
        os.system("gnome-terminal -e 'brave'")
## directily opening websites in defalt browser ##
    elif "open YouTube" in command:
        print("opening youtube in defalt browser")
        say("opening youtube in defalt browser")
        os.system( "gnome-terminal -e 'sensible-browser http://www.youtube.com'")
    elif "open Instagram" in command:
        print("opening instagram in defalt browser")
        say("openning instagram in defalt browser")
        os.system("gnome-terminal -e 'sensible-browser http:://www.instagram.com'")
## open websites in brave if installed ##
    elif "YouTube" and "brave" in command:
        print("opening youtube in brave")
        say("opening youtube in brave browser")
        os.system( "gnome-terminal -e 'brave http://www.youtube.com'")
    elif "Instagram" and "brave" in command:
        print("opening instagram in brave")
        say("opening instagram in brave browser")
        os.system( "gnome-terminal -e 'brave http://www.instagram.com'")
## these are personal commands based on my usage ##
    elif "open Google meet" in command:
        print("openning google meet in brave")
        say("openning google meet in brave")
        os.system("gnome-terminal -e 'brave -window https://meet.google.com/'")
    elif "open Google duo" in command:
        print("openning google duo")
        say("openning google duo")
        os.system("gnome-terminal -e 'brave https://duo.google.com/?web&utm_source=marketing_page_button_top'")
## other apps ##
    elif "open telegram" in command:
        say("openning telegram")
        os.system("gnome-terminal -e 'telegram-desktop'")
    elif "open WhatsApp" in command:
        say("openning whats app")
        os.system("gnome-terminal -e 'whatsie'")
    elif "open droidcam" in command :
        say("openning droidcam")
        os.system("gnome-terminal -e 'droidcam'")
    elif "open droidcam client" in command:
        say("openning droidcam")
        os.system("gnome-terminal -e 'droidcam-cli 192.168.29.175 4747'")
    elif "open jupyter lab" in command:
        say("openning jupyterlab")
        os.system("gnome-terminal -e 'jupyter-lab'")
    elif command == "open source code in edit":
        say("opening sorce code with vim")
        os.system("vim ABSA.py")
    elif "open terminal" in  command:
        say("openning new terminal window")
        os.system("gnome-terminal")
# other #
    elif "Run audio search" in command:
    ## sorce code of audio search engine ##
        print("Initializing voice seacrh....")
        loop=2
        say("Initializing cincinati....")
        print("say what to search ? ")
        say("say what to search")
        query=take_command()
        while loop < 3:
        ### acces the web ###
            try:
                print("Searching....")
                say("Searching")
                results = wikipedia.summary(query, sentences=2)
            except wikipedia.DisambiguationError:
                say(f"{query} not found,try another word.")
                print(query,"not found,try another word.")
                results=""
            except wikipedia.exceptions.PageError:
                say(f"{query} not found, {query} dosent match anything on the web.")
                print(query,"not found,",query,"dosent match anything on the web.")
                results=""
            try:
                print(results)
                say (results)
            except NameError:
                print("SORRY ")
            print("can I search anything else?")
            say("can i search anything else?")
        #### continue or break loop ####
            query2=take_command() 
            if 'yes' in query2.split(' ')[0]:
                query=query2.partition(' ')[2]
                continue
            elif "no" or "no " or "not really" or "not really " in query2 :
                print("cincinati out ;)")
                say("cincinati out")
                break
            else:
                say("invalid input,exiting voice search audio search")
                break
   # cincinati is done executing , back to sdmak #
    elif "play" and "music" in command:
        print("Initializing media player....")
        say("Initializing media player....")
        path=os.path.join( os.path.expanduser('~'),"Music")
        print("scanning user music at -> ")
        print(path)
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
                print("no music found in defalt directory ")
                say("no music found in defalt directory ")
                print("changing search path to inbuilt music")
                say("changing search path to inbuilt music ")
                path=os.path.join(os.getcwd(),"ABSA","music")
                print("succes")
                say("succes")
                mp3_files=[]
                all_files=os.listdir(path)
                for files in all_files:
                    f=files.split('.')[-1]
                    if f == "mp3":
                        mp3_files.append(files)
                d=random.choice(mp3_files)
            final_path=os.path.join(path ,d)                  
            print("now playing",d)
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
            print("play next?")
            print("yes or no")
            say("play next")
            say("yes or no")
            agian=take_command()
            if 'yes' in agian:
                continue
            elif 'no' in agian:
                print("keep vibing")
                say("keep vibing")
                break
    elif "open" and "source code" in command:
        print("Opennig source code")
        say("Opennig source code")
        os.system("gedit ABSA.py")
    elif "open" and "author profile" in command:
        print("opening sumant dhere's profile")
        say("opening sumant dhere's profile")
        os.system("gnome-terminal -e 'sensible-browser https://www.facebook.com/sumant.dhere.1'")
        os.system("gnome-terminal -e 'sensible-browser https://www.instagram.com/sdmak._.03'")
    elif "unknown" in command:
        path_to_improvement=os.path.join(os.getcwd(), "improvement.txt")
        improvment = open(path_to_improvement , "a+")
        print("here is a list of unknown commands recived")
        print(file.read())
        file.close()
    elif command == 'failed':
        sys.exit()
    else:
    ## incase of unclear or invalid command program exits ##
        print(host,"cannot understand. making a note in improvement file ")
        say(f"{host} cannot understand. making a note in improvement file")
        path_to_improvement=os.path.join( os.path.expanduser('~'),"ABSA")
        improvment = open(path_to_improvement , "a+")
        if command in improvement:
            print("query already in improvement, It will me added soon!!")
            say("query already in improvement, It will me added soon!!")
        else:
            improvment.write(f"{command} \n")
        improvment.close()

    print("can I help with anything else?")
    say("can i help with anything else?")
    #### continue or break loop ####
    end=take_command()
    if 'yes' in end.split(' ')[0]  :
        command=end.partition(' ')[2]
        continue
    elif 'no' in end.split(' ')[0] :
        print("happy to help ;)")
        say("happy to help")
        break
    else:
        print("did not recive a yes or no command , exiting ABSA ")
        say("did not recive a yes or no in command exiting absa  ")  
        break
try:
    sys.exit()
except SystemExit:
    print("")
