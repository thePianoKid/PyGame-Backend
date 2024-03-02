import threading
import time
import queue
from random import random


def message_sender(outgoing_queue, incoming_queue):
    letters_l = ['r','l','g','s','j']
    """Background thread function for sending messages to and receiving actions from the main game loop."""
    counter = 0
    initial_num = 0
    while True:
        rand = int(random() * (10000 - 0) + 0);
        if (rand in range(0, 100)):
            if rand in range(0,10):
                message = 'r' 
            elif rand in range(20, 30):
                message = 'j'
            elif rand in range(30, 40):
                message = 'l'
            else:
                message = "g"
            outgoing_queue.put_nowait(message)

            #print(f"Sent: {message}")
            #print( "THIS IS THE CURRENT COMMAND: " + letters_l[initial_num])
            counter += 1
            initial_num += 1
            if initial_num == 4:
                initial_num = 0

            try:
                # Attempt to receive an "action processed" notification from the game
                incoming_queue.get_nowait()  # Use non-blocking get
                counter -= 1  # Decrement the counter when an action is processed
                print(f"Action processed, counter decremented. New counter: {counter}")
            except queue.Empty:
                # No action received, continue
                pass

    
    

def start_message_thread(outgoing_queue, incoming_queue):
    """Starts the background thread for sending messages and receiving actions."""
    thread = threading.Thread(target=message_sender, args=(outgoing_queue, incoming_queue))
    thread.daemon = True
    thread.start()

