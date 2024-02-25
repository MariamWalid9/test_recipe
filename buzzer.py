import time

from gpiozero import Buzzer
from time import sleep

pin_number = 17
duration=1
def initialize_buzzer(pin_number):

    buzzer = Buzzer(pin_number)
    return buzzer

   """"" GPIO.setmode(GPIO.BCM)

      #Configure Pin (BCM) as output
     GPIO.setup (LED ,GPIO.OUT)
     GPIO.output (LED ,GPIO.LOW)"""

def play_buzzer(buzzer, duration):



    buzzer.on()
   time.sleep(duration)
    buzzer.off()

