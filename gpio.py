import RPi.GPIO as GPIO
import time

def init(start,stop):
    def event_start(event):
        start()
    def event_stop(event):
        stop()
    GPIO.setmode(GPIO.BOARD)

    # Bleu
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Rouge
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Vert
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Blanc
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(12, GPIO.RISING, callback=event_start, bouncetime=300)
    GPIO.add_event_detect(15, GPIO.RISING, callback=event_stop, bouncetime=300)

