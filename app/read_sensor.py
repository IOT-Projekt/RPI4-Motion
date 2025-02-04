from gpiozero import MotionSensor
from datetime import datetime
import os


# Get GPIO Pin from env
GPIO_PIN = os.getenv("GPIO_PIN", 23)

# Set up the motion sensor
pir = MotionSensor(GPIO_PIN)

def detect_motion():
    # Pauses Script until motion is detected
    pir.wait_for_motion()
   # current date and time
    now = datetime.now()

    # convert from datetime to timestamp
    ts = datetime.timestamp(now)
    
    return ts