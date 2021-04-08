def working():

    from selenium import webdriver
    class infow():
        def __init__(self):
            self.driver=webdriver.Chrome(executable_path='C:/userdrive/chromedriver.exe')
        def get_info(self,query):
            self.query=query
            self.driver.get(url="https://www.wikipedia.org/")
            search=self.driver.find_element_by_xpath('//*[@id="searchInput"]')
            search.click()
            search.send_keys(query)
            enter=self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
            enter.click()

        def youtube(self,query):
            self.query=query
            self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
            video=self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
            video.click()

        def WhatsApp(self,query):
            self.query=query
            self.driver.get(url="https://web.whatsapp.com/")

        def google(self,query):
            self.query=query
            self.driver.get(url="https://www.google.co.in/")
            search=self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
            search.click()
            search.send_keys(query)
            enter=self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
            enter.click()


    import subprocess as sp

    def sub(self):
        sp.getoutput(self)
    #sub("notepad")

    import pyttsx3 as p
    import speech_recognition as sr 
    engine=p.init()

    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    voices=engine.getProperty('voices')

    engine.setProperty("voice",voices[1].id)

    #engine.say("hello there,i am Minni, how are you? ")
    #engine.say("how can i help you")
    def speak(text):
        engine.say(text)
        engine.runAndWait()

    speak("hello,i am Minni, how are you?")
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
        audio=r.listen(source)
        text=r.recognize_google(audio)
        print(text)

    if "what" and "about" and "you" in text:
        speak("i am also having a good day sir")


    def main():

        speak("how can i help you")
        with sr.Microphone() as source:
            r.energy_threshold=10000
            r.adjust_for_ambient_noise(source,1.2)
            print("listening")
            audio=r.listen(source)
            text2=r.recognize_google(audio)

        if "information" in text2:
            speak("which type of information you want?")

            with sr.Microphone() as source:
                r.energy_threshold=10000
                r.adjust_for_ambient_noise(source,1.2)
                print("listening")
                audio=r.listen(source)
                infom=r.recognize_google(audio)

            speak("okay, let me search {} in wikipedia".format(infom))
            assist=infow()
            assist.get_info(infom)

        elif "Search" and "Google" in text2:
            speak("what you want to search?")

            with sr.Microphone() as source:
                r.energy_threshold=10000
                r.adjust_for_ambient_noise(source,1.2)
                print("listening_google")
                audio=r.listen(source)
                infom=r.recognize_google(audio)

            speak("okay, let me srch {} in google".format(infom))
            assist=infow()
            assist.google(infom)


        elif "WhatsApp" in text2:
            speak("let me open whatsapp for you.")
            assist=infow()
            assist.WhatsApp('hii')

        elif "Song" and "play" in text2:
            speak("which video or song you want to play ?")

            with sr.Microphone() as source:
                r.energy_threshold=10000
                r.adjust_for_ambient_noise(source,1.2)
                print("listening...")
                audio=r.listen(source)
                infom=r.recognize_google(audio)

            speak("okay, let me play {} on youtube ".format(infom))
            assist=infow()
            assist.youtube(infom)
            engine.runAndWait()

        elif "Notepad" in text2:
            print("sure; let me open notepad, for you.")
            speak("sure; let me open notepad, for you.")
            sub("notepad")

        else:
            print("sorry; i can't recognized what you trying to say...")
            speak("sorry; i can't recognized what you trying to say...")
            return main()
    main()  

from tkinter import *
t=Tk()
t.title("Voice Assistant System")
t.minsize(400,310)
t.resizable(0,0)
w=600
h=600
x=(t.winfo_screenwidth()-w)/2
y=(t.winfo_screenheight()-h)/2
t.geometry("%dx%d+%d+%d"%(w,h,x,y))
t.configure(bg="yellow")

u1=Label(text="Welcome to mini world,\n Please click to Speak...",font=("bell mt",22),bg="yellow",fg="black")
u1.place(x=150,y=100)

b1=Button(text="Speak",font=("bell mt",22),bg="lightblue",command=working)
b1.place(x=200,y=270,height=60,width=200)
t.mainloop()
