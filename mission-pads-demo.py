from djitellopy import Tello
import tkinter, time, winsound

def warning():
    for n in range(4): # 4 short beeps
        winsound.Beep(1500, 500)
        time.sleep(0.5)
    winsound.Beep(1500, 1000) # 1 long beep

tello = Tello()
tello.connect()
# Activate the mission pads
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(0)  # use downward camera
# Take off
warning()
tello.takeoff()
tello.send_rc_control(0, 30, 0, 0)  # Move forward

pad = tello.get_mission_pad_id()    # Look for a mission pad
while pad != 1:                     # While we don't see pad 1
    if pad == 4:                    # If we see pad 4
        winsound.Beep(2500, 500)
    pad = tello.get_mission_pad_id()# Take another look

# Land
tello.disable_mission_pads()
tello.land()
tello.end()

