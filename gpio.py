import RPi.GPIO as GPIO
import time

GPIO_START=12
GPIO_STOP=15

def init(ready,start,stop):
    def event_start(event):
        if GPIO.input(GPIO_START) == True:
            start()
        else:
            ready()
    def event_stop(event):
        stop()
    GPIO.setmode(GPIO.BOARD)

    # Bleu
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Rouge
    GPIO.setup(GPIO_STOP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Vert
    GPIO.setup(GPIO_START, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Blanc
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(GPIO_START, GPIO.RISING, callback=event_start, bouncetime=300)
    GPIO.add_event_detect(GPIO_STOP, GPIO.RISING, callback=event_stop, bouncetime=300)

