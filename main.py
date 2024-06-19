import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
if __name__ == '__main__':
    print("Welcome to robo speaker  Created by Eyeronic")
    while True:
        x=input("Enter what do you want me to speak: ")
        if x=='q':
            speak.Speak('signing out')
            break
        speak.Speak(x)