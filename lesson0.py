from djitellopy import Tello
import tkinter
import time
import winsound

def warning():
    for n in range(4): # 4 short beeps
        winsound.Beep(1500, 500)
        time.sleep(0.5)
    winsound.Beep(1500, 1000) # 1 long beep

print("Starting up")
tello = Tello()
tello.connect()
time.sleep(5)
warning()
tello.takeoff()
# Fly around a bit
tello.send_rc_control(0, 30, 0, 0) # forward
time.sleep(2)
tello.send_rc_control(30, 0, 0, 0) # right
time.sleep(2)
tello.send_rc_control(-30, 0, 0, 0) # left
time.sleep(2)
tello.send_rc_control(0, -30, 0, 0) # reverse
time.sleep(2)
# Terminate
tello.land()
tello.end()

