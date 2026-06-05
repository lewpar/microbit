import radio
from microbit import *

radio.on()

while True:
    y = accelerometer.get_y()
    
    if y < 100:
        radio.send("forward")
        display.show(Image.ARROW_N)
    elif y > 700:
        radio.send("backward")
        display.show(Image.ARROW_S)
    else:
        radio.send("stop")
        display.show(Image.SQUARE_SMALL)

    left_message = "left_" + ("on" if button_a.is_pressed() else "off")
    right_message = "right_" + ("on" if button_b.is_pressed() else "off")
    
    radio.send(left_message)
    radio.send(right_message)

    sleep(50)
