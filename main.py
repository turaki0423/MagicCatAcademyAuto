from pynput.mouse import Button, Controller
from pynput import keyboard
from time import sleep
import pyautogui



mouse = Controller()

def move1():
    print("move1")
    mouse.press(Button.left)
    sleep(0.1)
    for i in range(100):
        mouse.move(0, 1)
        sleep(0.0001)
    mouse.release(Button.left)
    sleep(0.1)
    mouse.move(0, -100)

def move2():
    print("move1")
    mouse.press(Button.left)
    sleep(0.1)
    for i in range(100):
        mouse.move(1, 0)
        sleep(0.0001)
    mouse.release(Button.left)
    sleep(0.1)
    mouse.move(-100, 0)

def move3():
    print("move1")
    mouse.press(Button.left)
    sleep(0.1)
    for i in range(100):
        mouse.move(1, 1)
        sleep(0.00005)
    for i in range(100):
        mouse.move(1, -1)
        sleep(0.00005)
    mouse.release(Button.left)
    sleep(0.1)
    mouse.move(-200, 0)

def move4():
    print("move1")
    mouse.press(Button.left)
    sleep(0.1)
    for i in range(100):
        mouse.move(1, -1)
        sleep(0.00005)
    for i in range(100):
        mouse.move(1, 1)
        sleep(0.00005)
    mouse.release(Button.left)
    sleep(0.1)
    mouse.move(-200, 0)

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    try:
        ikey = key.char
        if ikey == "y":
            move1()
        elif ikey == "m":
            move2()
        elif ikey == "t":
            move4()
        elif ikey == "b":
            move3()
    except AttributeError:
        pass

listener = keyboard.Listener(
    on_release=on_release)
listener.start()

input("press Enter to end")
