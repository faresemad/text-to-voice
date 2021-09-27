from gtts import gTTS
from playsound import playsound
import os
import time, sys
while True:
    os.system('clear')
    from termcolor import colored
    team='''

    \u001b[30m███████╗ ██████╗ ██████╗ ██████╗ ██████╗ ██╗ ██████╗ ███╗   ██╗
    \u001b[35m██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗██║██╔═══██╗████╗  ██║
    \u001b[35m███████╗██║     ██║   ██║██████╔╝██████╔╝██║██║   ██║██╔██╗ ██║
    \u001b[35m╚════██║██║     ██║   ██║██╔══██╗██╔═══╝ ██║██║   ██║██║╚██╗██║
    \u001b[35m███████║╚██████╗╚██████╔╝██║  ██║██║     ██║╚██████╔╝██║ ╚████║
    \u001b[36m╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                    \u001b[33mCopyright:faresemadx
    '''
    col=colored(team,'red')
    print(col)
    print('-'*45)
    names=input("\u001b[33;1m[+]Enter name file:- ")
    lan=input("\u001b[34;1m[+]Chosse the language(en/ar):- ")
    txt=input("\u001b[35;1m[+]Enter the Text here:- ")
    def loading():
        print("\u001b[37;1mLoading...")
        for i in range(0, 100):
            time.sleep(0.001)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.flush()
            time.sleep(0.001)
            sys.stdout.write(str(i + 1) + "%")
            sys.stdout.flush()
    loading()
    audio = names+'.mp3'
    sp = gTTS(text=txt , lang = lan , slow=False)
    try:
        sp.save(audio)
        playsound(audio)
    except ValueError:
        pass
