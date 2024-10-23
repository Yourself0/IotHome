import paho.mqtt.client as mqtt

# Define the broker URL and port
broker = "0.tcp.in.ngrok.io"
port = 15551

# Define the callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Publish the message once connected
    topic = "test/topic"
    message = "Hello, MQTT"
    client.publish(topic, message)

def on_publish(client, userdata, mid):
    print(f"Message published: {mid}")

# Create a new MQTT client instance
client = mqtt.Client()

# Assign the callback functions
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the broker
client.connect(broker, port, 60)

# Start the loop to process network traffic
client.loop_start()

# Optionally wait for a few seconds before disconnecting to allow the message to be sent
import time
time.sleep(2)

# Disconnect from the broker
client.loop_stop()
client.disconnect()
