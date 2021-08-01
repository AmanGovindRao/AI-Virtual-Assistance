#version - 1.5
#Date - O1.O8.2O21

from jarvis import speak
from platform import version
import sys
import pyttsx3
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pywhatkit
import wikipedia
from googletrans import Translator
import os
import pyautogui
import psutil
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import requests
from tkinter import Tk
from gtts import gTTS
from tkinter import StringVar
import PyPDF2
from pytube import YouTube
import datetime
from playsound import playsound
import keyboard
import pyjokes
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

def Speak(Audio):
    engine.say(Audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        print("Good Morning sir I am E.D.I.T.H.")
        Speak("good morning sir I am Edith")
    elif hour>=12 and hour<16:
        print("Good Afternoon Sir I am E.D.I.T.H.")
        Speak("good afternoon sir I am Edith")
    elif hour>=16 and hour<20:
        print("Good Evening Sir I am E.D.I.T.H.")
        Speak("good Evening sir I am Edith")
    else:
        print("Good Night Sir I am E.D.I.T.H.")
        Speak("good night sir I am Edith")




def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "None"
        
    return query.lower()

def TaskExe():

    def Music():
        Speak("Tell Me The NamE oF The Song!")
        musicName = takecommand()

        if 'akeli' in musicName:
            os.startfile('E:\\Songs\\akeli.mp3')

        elif 'blanko' in musicName:
            os.startfile('E:\\Songs\\blanko.mp3')

        else:
            pywhatkit.playonyt(musicName)

        Speak("Your Song Has Been Started! , Enjoy Sir!")

    def OpenApps():
        Speak("Ok Sir")
        
        if 'code' in query:
            os.startfile("C:\\Users\\Amanr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            Speak("opening code")

        elif 'whatsapp' in query:
            os.startfile("C:\\Users\\Amanr\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
            Speak("opening whatsapp")

        elif 'browser' in query:
            os.startfile("A:\\PROGRAM_FILE\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
            Speak("opening browser")

        elif 'c folder' in query or 'see folder' in query:
            os.startfile("P:\\C - Language\\C - Language")
            Speak("opening browser")
        
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')
            Speak("opening facebook")

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')
            Speak("opening instagram")

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/')
            Speak("opening map")

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')
            Speak("opening youtube")

        elif 'notepad' in query or 'note' in query:
            os.startfile("C:\\Windows\\system32\\notepad.exe")

        elif 'm s word' in query or 'microsoft word' in query or 'word' in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.EXE")

        elif 'm s exel' in query or 'microsoft exel' in query or 'exel' in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

        elif 'zoom' in query or 'joom' in query:
            os.startfile("C:\\Users\\amanr\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")


        Speak("opened")

    def CloseAPPS():
        Speak("Ok Sir , Wait A second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'browser' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'whatsapp' in query:
            os.system("TASKKILL /F /im whatsapp.exe")

        elif 'm s word' in query:
            os.system("TASKKILL /F /im WINWORD.EXE")

        elif 'exel' in query:
            os.system("TASKKILL /F /im EXCEL.EXE")

        elif 'Zoom' in query:
            os.system("TASKKILL /F /im Zoom.exe")
            
        Speak("Closed ")

    def Temp():
        search = "temperature in delhi"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"The Temperature Outside Is {temperature} celcius")

        Speak("Do I Have To Tell You Another Place Temperature ?")
        next = takecommand()

        if 'yes' in next:
            Speak("Tell Me The Name Of tHE Place ")
            name = takecommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Speak(f"The Temperature in {name} is {temperature} celcius")

        else:
            Speak("no problem sir")

    def Reader():
        Speak("Tell Me The Name Of The Book!")

        name = takecommand()

        if 'india' in name:

            os.startfile('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 1.pdf')
            book = open('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 1.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading ?")
            numPage = int(input("Enter The Page Number :"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language , I Have To Read ?")
            lang = takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                Speak(text)

        elif 'europe' in name:
            os.startfile('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 3.pdf')
            book = open('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 3.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading ?")
            numPage = int(input())
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language , I Have To Read ?")
            lang = takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:

                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                Speak(text)


    def YoutubeAuto():
        Speak("ok sir")

        if 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        Speak("done")

    def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing.....")
                query = command.recognize_google(audio,language='hi')
                print(f"You Said : {query}")

            except:
                return "none"

            return query.lower()

    def Tran():
        Speak("Tell Me The Line!")
        line = TakeHindi()
        traslate = Translator()
        result = traslate.translate(line)
        Text = result.text
        Speak(Text)
        
    def ChromeAuto():
        Speak("Chrome Automation started!")

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'close the window' in command:
            keyboard.press_and_release('alt + f4')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl +h')

    def whatsapp():
        Speak("tell me the name of person")
        name = takecommand()

        if 'Home' in name:
            Speak("okk sir, tell me the message")
            msg = takecommand()
            Speak("tell me the time sir")
            Speak("time in hour!")
            hour = int(takecommand())
            Speak("time in minute")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+919918541517",msg,hour,min,20)
            Speak("okk sir, message is sending")

        elif 'golu bhaiya' in name or 'rebel rajput' in name or 'fb' in name:
            Speak("ok sir, message is sending to rebel rajput")
            Speak("tell me the message")
            msg = takecommand()
            Speak("tell me the time")
            Speak("in hour sir")
            hour = int(takecommand())
            Speak("time in minute")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+918299289085",msg,hour,min,20)
            Speak("okk sir, message is sending")

        elif 'Abhishek' in name:
            Speak("okk sir, tell me the message")
            msg = takecommand()
            Speak("tell me the time sir")
            Speak("time in hour!")
            hour = int(takecommand())
            Speak("time in minute")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+919696315994",msg,hour,min,20)
            Speak("okk sir, message is sending")

        elif 'anshu bhaiya' in name:
            Speak("okk sir, tell me the message")
            msg = takecommand()
            Speak("tell me the time sir")
            Speak("time in hour!")
            hour = int(takecommand())
            Speak("time in minute")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+919335365953",msg,hour,min,20)
            Speak("okk sir, message is sending")

        elif 'Prince' in name:
            Speak("okk sir, tell me the message")
            msg = takecommand()
            Speak("tell me the time sir")
            Speak("time in hour!")
            hour = int(takecommand())
            Speak("time in minute")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+918299289085",msg,hour,min,20)
            Speak("okk sir, message is sending")

        else:
            Speak("ok sir, this message will send on jio number")
            Speak("tell me the massage")
            msg = takecommand()
            Speak("tell me the time sir")
            Speak("time in hour!")
            hour = int(takecommand())
            Speak("time in minute")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+919026240970",msg,hour,min,20)
            Speak("okk sir, message is sending")

    def screenshot():
        Speak("Ok Sir , What Should I Name That File ?")
        path = takecommand()
        path1name = path + ".png"
        path1 = "Z:\\screen shots"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("Z:\\screen shots\\")
        Speak("Here Is Your ScreenShot") 

    while True:

        query = takecommand()

        if 'hello' in query or 'hello jarvis' in query or 'hello Ned' in query or 'hello edith' in query or 'hii jarvis' in query or 'hii edith' in query:
            Speak("Hello Sir , I Am Edith .")
            Speak("How May I Help You?")

        elif 'how are you' in query:
            Speak("I Am Fine Sir!")
            Speak("Whats About YOU?")

        elif 'youtube search' in query:
            Speak("OK sIR , This Is I found For Your Search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'website' in query:
            Speak("Ok Sir , Launching.....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'launch a website' in query:
            Speak("Tell Me The Name Of The Website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("jarvis","")
            query = query.replace("edith","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")


        elif 'whatsapp message' in query:
            whatsapp()

        elif 'screenshot' in query or 'take a screenshot' in query or 'take a s s' in query:
            screenshot()
            Speak("done")

        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()
            
        elif 'open whatsapp' in query:
            OpenApps()

        elif 'open browser' in query:
            OpenApps()

        elif 'open notepad' in query:
            OpenApps()


        elif 'open m s word' in query:
            OpenApps()

        elif 'open m s exel' in query:
            OpenApps()

        elif 'open zoom' in query:
            OpenApps()

        elif 'close browser' in query:
            CloseAPPS()

        elif 'music' in query:
            Music()

        elif 'close whatsapp' in query:
            CloseAPPS()

        elif 'close instagram' in query:
            CloseAPPS()

        elif 'close facebook' in query:
            CloseAPPS()

        elif 'close m s exel' in query:
            CloseAPPS()

        elif 'close m s word' in query:
            CloseAPPS()

        elif 'close zoom' in query:
            CloseAPPS()


        elif 'pause' in query or 'stop' in query:
            YoutubeAuto()

        elif 'restart' in query:
            YoutubeAuto()

        elif 'mute' in query:
            YoutubeAuto()

        elif 'skip' in query:
            YoutubeAuto()

        elif 'back' in query:
            YoutubeAuto()

        elif 'full screen' in query:
            YoutubeAuto()

        elif 'film mode' in query:
            YoutubeAuto()

        elif 'youtube tool' in query:
            YoutubeAuto()


        elif 'close this tab' in query or 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')
            Speak("done")

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')
            Speak("done")

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
            Speak("done")

        elif 'history' in query:
            keyboard.press_and_release('ctrl +h')
            Speak("done")

        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'repeat my word' in query:
            Speak("okk sir ! Speak your word")
            jj = takecommand()
            Speak(f"You Said : {jj}")

        elif 'my location' in query:
            Speak("Ok Sir , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/@26.8791088,83.8832042,335m/data=!3m1!1e3!4m2!10m1!1e2')

        elif 'alarm' in query:
            Speak("Enter The Time !")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time To Wake Up Sir!")
                    playsound('iron.mp3')
                    Speak("Alarm Closed!")

                elif now>time:
                    break

        elif 'video downloader' in query:
            root = Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.title("Youtube Video Downloader")
            Speak("Enter Video Url Here !")
            Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
            link = StringVar()
            Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
            Entry(root,width = 70,textvariable = link).place(x=32,y=90)

            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

            Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

            root.mainloop()
            Speak("Video Downloaded")
            
        elif 'translator' in query or 'translate' in query or 'open translator' in query:
            Tran()
        
        elif 'speak in hindi' in query or 'hindi' in query or 'activate hindi mode' in query:
            TakeHindi()



        elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("jarvis","")
            Speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            Speak("You Tell Me That" + remeber.read())

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak("No Speakable Data Available!")

        elif 'how to' in query:
            Speak("Getting Data From The Internet !")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)
            
        elif 'temperature' in query:
            Temp()

        elif 'read book' in query:
            Reader()


            # PHOTOS


        elif "show my photo" in query or "show my photos" in query:
            Speak("ok sir, showing your photo")
            pic_dir = 'D:\hm\my_photo'
            pics = os.listdir(pic_dir)
            os.startfile(os.path.join(pic_dir,pics[0]))

        elif "biru bhaiya ka photo" in query or "biru bhaiya" in query or "veeru bhaiya" in query:
            Speak("ok sir, showing photos of Biru bhaiya")
            pic_dir = 'D:\Biru_bhaiya_(shaadi)'
            pics = os.listdir(pic_dir)
            os.startfile(os.path.join(pic_dir,pics[0]))


        elif "show the photos of kushinagar tour" in query or "kushinagar tour" in query or "pics of kushinagar tour" in query:
            Speak("ok sir, showing photos of kushinagar tour")
            pic_dir = 'D:\kushinagar tour'
            pics = os.listdir(pic_dir)
            os.startfile(os.path.join(pic_dir,pics[0]))


        elif "show my another photo" in query or "show my another photo" in query or "so my another photo" in query:
            Speak("okay, showing your another photo")
            pic_dir = 'D:\hm\my_photos2'
            pics = os.listdir(pic_dir)
            os.startfile(os.path.join(pic_dir,pics[0]))


        elif "show my brother photo" in query or "show my brother pic" in query or "show my brother photos" in query:
            Speak("okay, showing your brother photo")
            pic_dir = 'D:\hm\my_brother'
            pics = os.listdir(pic_dir)
            os.startfile(os.path.join(pic_dir,pics[0]))



        

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How about you']
            ans_q = random.choice(stMsgs)
            Speak(ans_q)  
            ans_take_from_user_how_are_you = takecommand()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                Speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                Speak('oh sorry..')

        elif 'who make you' in query or 'who created you' in query or 'who develop you' in query:
            ans_m = " For  your  information  Aman Rajput  Created me, ! I give Lot of Thannks to Him "
            print(ans_m)
            Speak(ans_m)
        
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Edith, an A I based computer program but i can help you lot like a your close friend !"
            print(about)
            Speak(about)

        elif "what do you feel" in query or "what about your feeling" in query:
            print("feeling Very sweet after meeting with you")
            Speak("feeling Very sweet after meeting with you")
        





        

        elif "activate how to do mode" in query:
            Speak("how to do mode is activated")
            from pywikihow import search_wikihow
            while True:
                Speak("please tell me what you want know")
                how = takecommand()
                try:
                    if "exit" in how or "close" in how:
                        Speak("okay sir, how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) -- 1
                        how_to[0].print()
                        Speak(how_to[0].summary)
                except Exception as e:
                    Speak("sorry sir  i am not  able  find  this")

        

        elif "what can do" in query or "what you can do" in query:
            Speak("ooo ")
            pic_dir = 'D:\what_can_do'
            pics = os.listdir(pic_dir)
            os.startfile(os.path.join(pic_dir,pics[0]))
       

        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            Speak(ex_exit)
            exit()

        elif "sleep" in query or "you can sleep jarvis" in query or "sleep jarvis" in query or "you need a break" in query or "jarvis you can sleep" in query or "jarvis you can sleep now" in query:
            Speak("okay sir i am going to sleep, you can call me anytime.")
            print("Ok... sir I am going to sleep, You can call me anytime.")
            break

        elif "take a break" in query or "you can sleep edith" in query or "you need to go" in query or "you need a rest" in query or "you need a break" in query or "edith you can sleep" in query or "edith you can sleep now" in query:
            Speak("okay sir i am going to sleep, you can call me anytime! just say Wakeup")
            print("Ok... sir I am going to sleep, You can call me anytime! just say Wakeup")
            break

        elif "shutdown" in query:
            Speak("shutting down")
            os.system('shutdown -s')


if __name__ == "__main__":
    while True:
        Permission = takecommand()
        if "activate jarvis" in Permission or "activate" in Permission or "17" in Permission or 'jarvis come on' in Permission or 'edith come on' in Permission or 'edith activate' in Permission or 'activate edith' in Permission or 'come on' in Permission or 'lets start' in Permission or 'start' in Permission or 'start karo edith' in Permission or 'start karo jarvis' in Permission:
            wish()
            TaskExe()

        elif "make up" in Permission or "wake up jarvis" in Permission or "244" in Permission or "Hey jarvis" in Permission or "come back jarvis" in Permission  or "come jarvis" in Permission or "wake up edith" in Permission or "come back edith" in Permission  or "come edith" in Permission or "wapas aa jao jarvis" in Permission or "wapas a jao" in Permission:
            print("Welcome Back Sir")
            Speak("Welcome Back Sir")
            TaskExe()

        elif "bye jarvis" in Permission or "bye" in Permission or "close" in Permission or "Deactivate" in Permission or "bye edith" in Permission or "exit" in Permission or "you need to go" in Permission or "you need to go edith" in Permission or "you need to go jarvis" in Permission:
            Speak("thanks for using me sir, have a good day")
            print("thanks for using me sir, have a good day")
            sys.exit()