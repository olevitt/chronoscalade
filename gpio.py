import RPi.GPIO as GPIO
import time

# Utiliser les numéros de broche physiques
GPIO.setmode(GPIO.BOARD)

# Bleu
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Rouge
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Vert
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Blanc
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def my_callback(channel):
    print("Hello")

GPIO.add_event_detect(16, GPIO.RISING, callback=my_callback, bouncetime=300)

start_time = 0
stop_time = 0

# Boucle principale
while True:
    pass
    # Vérifier si le bouton start est enfoncé
    #if GPIO.input(11) == False:
        #print("Start button pressed")
    # Vérifier si le bouton stop est enfoncé
    #if GPIO.input(15) == False:
        #print("Stop button pressed")
        # Vérifier si le bouton start est enfoncé
    #if GPIO.input(12) == False:
        #print("Start2 button pressed")
    # Vérifier si le bouton stop est enfoncé
    #if GPIO.input(16) == False:
        #print("Stop2 button pressed")

