import threading
import time
import queue
import random


def message_sender(outgoing_queue, incoming_queue):
    letters_l = ['r','l','g','s','j']
    """Background thread function for sending messages to and receiving actions from the main game loop."""
    counter = 0
    initial_num = 0
    while True:
       
        time.sleep(0.01)  # Simulate delay between sending messages
        
        message = letters_l[4]

        outgoing_queue.put(message)
        print(f"Sent: {message}")
        print( "THIS IS THE CURRENT COMMAND: " + letters_l[initial_num])
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

