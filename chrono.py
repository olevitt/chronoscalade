import tkinter as tk
from datetime import datetime
from gpio import init

def start_timer():
    global start_time
    start_time = datetime.now()
    update_timer()

def stop_timer():
    global start_time
    start_time = None

def reset_timer():
    stop_timer()
    label_timer.config(text="00:00:00.000")

def update_timer():
    if start_time:
        elapsed_time = datetime.now() - start_time
        label_timer.config(text=str(elapsed_time)[:-3])
        label_timer.after(10, update_timer)

def quit():
    root.destroy()


root = tk.Tk()
root.title("Chronomètre")
root.geometry("800x480")
root.attributes("-fullscreen", True)

label_timer = tk.Label(root, text="00:00:00.000", font=("Helvetica", 100))
label_timer.pack(expand=True, fill='both')

button_start = tk.Button(root, text="Démarrer", command=start_timer)
button_start.pack(expand=True, fill='both')

button_stop = tk.Button(root, text="Arrêter", command=stop_timer)
button_stop.pack(expand=True, fill='both')

button_reset = tk.Button(root, text="Réinitialiser", command=reset_timer)
button_reset.pack(expand=True, fill='both')

button_quit = tk.Button(root, text="Quitter", command=quit)
button_quit.pack(expand=True, fill='both')

init(start_timer,stop_timer)

root.mainloop()
