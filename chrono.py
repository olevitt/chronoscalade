from tkinter import *
from datetime import datetime

gpio = True

start_time = None
stop_time = None

def start_timer():
    global start_time
    global stop_time
    start_time = datetime.now()
    stop_time = None
    update_timer()

def stop_timer():
    global stop_time
    if not stop_time:
        stop_time = datetime.now()
    majAffichage()

def reset_timer():
    global start_time
    start_time = None
    stop_timer()
def ready():
    reset_timer()
    label_timer.config(text="Prêt?")
def update_timer():
    if start_time:
        majAffichage()
        label_timer.after(10, update_timer)
def majAffichage(fin=False):
    affichageStr = "..."
    global start_time
    global stop_time
    if start_time:
        elapsed_time = datetime.now() - start_time
        if stop_time:
            elapsed_time = stop_time - start_time
        affichageStr = strdelta(elapsed_time)
    label_timer.config(text=affichageStr)

def strdelta(elapsed_time):
    returnStr = '{:0>2}'.format(elapsed_time.seconds%60)
    if (elapsed_time.seconds > 60):
        returnStr = str(elapsed_time.seconds//60)+":"+returnStr
    returnStr = returnStr + ":" + '{:0>2}'.format(int(elapsed_time.microseconds/10000))
    return returnStr

root = Tk()
root.title("Chronoscalade")
root.geometry("800x480")
root.attributes("-fullscreen", True)

label_timer = Label(root, text="...", font=("Helvetica", 200))
label_timer.pack(expand=True, fill='both')

button_start = Button(root, text="Démarrer", command=start_timer)
button_start.pack(side=LEFT,fill='x',expand=True)

button_stop = Button(root, text="Arrêter", command=stop_timer)
button_stop.pack(side=LEFT,fill='x',expand=True)

button_reset = Button(root, text="Réinitialiser", command=reset_timer)
button_reset.pack(side=LEFT,fill='x',expand=True)

button_quit = Button(root, text="Quitter", command=quit)
button_quit.pack(side=LEFT,fill='x',expand=True)

if gpio:
    from gpio import init
    init(ready,start_timer,stop_timer)

root.mainloop()
