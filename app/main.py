import os
import time
import paho.mqtt.client as mqtt
from read_sensor import detect_motion
import json
import logging
import threading

# Create a lock for thread-safe operations
lock = threading.Lock()

# setup basic logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Constants based on environment variables
BROKER = os.getenv("BROKER_IP", "localhost")
PORT = int(os.getenv("BROKER_PORT", 1883))
TOPIC_MOTION = os.getenv("TOPIC_MOTION", "iot/devices/motion_sensor")
MQTT_USERNAME = os.getenv("MQTT_USERNAME", None)
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", None)
CLIENT_ID = os.getenv("CLIENT_ID", "hc-sr501")

# Initialize the MQTT client
client = mqtt.Client()

# If username and password are set, use them for authentication
if MQTT_USERNAME and MQTT_PASSWORD:
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)


# Callback function for connection logging
def on_connect(client, userdata, flags, rc):
    # If the connection was successful, subscribe to the frequency topic
    if rc == 0:
        logging.info("Verbunden mit dem Broker")
    else:
        logging.error(f"Verbindung fehlgeschlagen. Code: {rc}")


# Callback function for message logging
def on_publish(client, userdata, mid):
    logging.info(f"Nachricht mit ID {mid} veröffentlicht")

# Set the callback functions
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the broker
client.connect(BROKER, PORT, keepalive=60)


def send_mqtt(data):
    """ Send Motion and timestamp to the MQTT broker."""
    # If no data was provided, return without sending
    if data is None:
        return

    # Create humidity payload and send it to the MQTT broker
    motion_payload = json.dumps(
        {
            "source": "mqtt",
            "device_id": CLIENT_ID,
            "motion": "True",
            "timestamp": data,
        }
    )
    client.publish(TOPIC_MOTION, motion_payload)
    logging.info(f"Bewegung gesendet: {motion_payload}")

if __name__ == "__main__":
    # start the MQTT client loop in a separate thread. Therefore messages with a new frequency can be received while sending data
    client.loop_start()
    while True:
        print("Ready")
        timestamp = detect_motion()  # Call the sensor function to detect motion and get timestamp
        print("Motion Detected")
        send_mqtt(timestamp)  # Send the message with the motion timestamp
        time.sleep(1)


