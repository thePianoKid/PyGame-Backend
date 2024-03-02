import certifi
import threading
import paho.mqtt.client as mqtt

class MQTT:
    def __init__(self, outgoing_queue):
        self.outgoing_queue = outgoing_queue
    # on_connect is called when the app successfully connects to the broker
    def on_connect(self, client, userdata, flags, rc):
        print(f'Connected (Result: {rc})')
        # Subscribe to all messages coming from player, or any nested topics
        # This includes player/r, to make the player move right
        # player/l, to make the player move left... you get the idea
        client.subscribe('player/#')

    def on_message(self, client, userdata, msg):
        print(f'Message received on topic: {msg.topic}. Message: {msg.payload}')
        # Topic or payload that we really care about?
        outgoing_queue.put(msg.topic)

    def start_client(self):
        # Connect to the Solace broker via the MQTT client
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

        # Defining which functions will be exeucted when the client connects to the Solace broker
        client.on_connect = self.on_connect
        # If an event is published to a topic that the client is subscribed to, on_message will be called
        client.on_message = self.on_message

        # Some networking BS... don't ask me
        client.tls_set(ca_certs=certifi.where())

        # The broker's password is entered here: 
        client.username_pw_set('solace-cloud-client', 'ars0ejhtoqh8ucvebu7ueo2iqk')

        # Use the host and port from Solace Cloud without the protocol
        # ex. "ssl://yoururl.messaging.solace.cloud:8883" becomes "yoururl.messaging.solace.cloud"
        client.connect('mr-connection-2r2gh8jfz5h.messaging.solace.cloud', port=8883)

        thread = threading.Thread(target=client.loop_forever)
        thread.daemon = True
        thread.start()
