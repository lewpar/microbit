import radio
from microbit import *

radio.on()

while True:
    y = accelerometer.get_y()

    if y < 400:
        print("Sending forward command..")
        radio.send("forward")
    elif y > 900:
        print("Sending backward command..")
        radio.send("backward")
    else:
        print("Sending stop command..")
        radio.send("stop")

    left_message = "left_" + ("on" if button_a.is_pressed() else "off")
    right_message = "right_" + ("on" if button_b.is_pressed() else "off")
    radio.send(left_message)
    radio.send(right_message)

    print(left_message)
    print(right_message)

    sleep(50)
