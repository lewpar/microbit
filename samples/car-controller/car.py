import radio

from microbit import *
from Ringbit import RINGBIT

radio.on()
ringbit = RINGBIT(pin1, pin2)

is_turning_left = False
is_turning_right = False

def drive_forward():
    ringbit.set_motors_speed(100 if is_turning_right else 50, 100 if is_turning_left else 50)

def drive_backward():
    ringbit.set_motors_speed(-100 if is_turning_right else -50, -100 if is_turning_left else -50)

def stop():
    ringbit.set_motors_speed(0, 0)

def left_on():
    global is_turning_left
    is_turning_left = True

def left_off():
    global is_turning_left
    is_turning_left = False

def right_on():
    global is_turning_right
    is_turning_right = True

def right_off():
    global is_turning_right
    is_turning_right = False

handlers = {
    "forward": drive_forward,
    "backward": drive_backward,
    "stop": stop,
    "left_on": left_on,
    "left_off": left_off,
    "right_on": right_on,
    "right_off": right_off
}

def handle_message(message):
    if message in handlers:
        print("Received message for handler '" + message + "', executing..")
        handler = handlers[message]
        handler()
    else:
        print("Received message '" + message + "' but no matching handler exists.")

while True:
    message = radio.receive()
    if message:
        handle_message(message)
