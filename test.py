import winsound, time

def warning():
    winsound.Beep(1500, 500)
    time.sleep(0.5)
    winsound.Beep(1500, 500)
    time.sleep(0.5)
    winsound.Beep(1500, 1000)

warning()

