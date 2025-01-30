from gpiozero import MotionSensor
from datetime import datetime



# Set up the motion sensor
pir = MotionSensor(23)

def detect_motion():
    # Pauses Script until motion is detected
    pir.wait_for_motion()
   # current date and time
    now = datetime.now()

    # convert from datetime to timestamp
    ts = datetime.timestamp(now)
    
    return ts