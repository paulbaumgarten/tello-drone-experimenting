import time
from pynput import keyboard

def on_press(key):
    try:
        print(f'alphanumeric key {key.char} pressed')
    except AttributeError:
        print(f'special key {key} pressed')    

listener = keyboard.Listener(on_press=on_press)
listener.start()

input()

