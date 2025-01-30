from gpiozero import MotionSensor
import time

# Set up the motion sensor
pir = MotionSensor(23)

def detect_motion():
    # Pauses Script until motion is detected
    pir.wait_for_motion()
    return time.time()  # Return the timestamp of when motion is detected

