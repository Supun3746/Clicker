import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode


toogle_key = KeyCode(char="s")
clicking = False
mouse = Controller()



def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(0.001)

def toogle_event(key):
    if key == toogle_key:
        global clicking
        clicking = not clicking

def main():
    clicking_thread = threading.Thread(target=clicker)
    clicking_thread.start()
    with Listener(on_press=toogle_event) as listener:
        listener.join()


if __name__ == "__main__":
    main()