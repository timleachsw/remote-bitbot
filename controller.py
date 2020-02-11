from microbit import *
import radio


# Define display images
centre = Image("00000:00000:00900:00000:00000")
right_tilts = [
    Image("00000:00000:00990:00000:00000"),
    Image("00000:00000:00999:00000:00000"),
    Image("00000:00000:00999:90000:00000"),
    Image("00000:00000:00999:99000:00000"),
    Image("00000:00000:00999:99900:00000"),
    Image("00000:00000:00999:99990:00000"),
    Image("00000:00000:00999:99999:00000"),
    Image("00000:00000:00999:99999:90000"),
    Image("00000:00000:00999:99999:99000"),
    Image("00000:00000:00999:99999:99900"),
    Image("00000:00000:00999:99999:99990"),
    Image("00000:00000:00999:99999:99999")
]
left_tilts = [
    Image("00000:00000:09900:00000:00000"),
    Image("00000:00000:99900:00000:00000"),
    Image("00000:00009:99900:00000:00000"),
    Image("00000:00099:99900:00000:00000"),
    Image("00000:00999:99900:00000:00000"),
    Image("00000:09999:99900:00000:00000"),
    Image("00000:99999:99900:00000:00000"),
    Image("00009:99999:99900:00000:00000"),
    Image("00099:99999:99900:00000:00000"),
    Image("00999:99999:99900:00000:00000"),
    Image("09999:99999:99900:00000:00000"),
    Image("99999:99999:99900:00000:00000")
]
full = Image("99999:99999:99999:99999:99999")
scale_factor = 85

# Turn radio on
radio.on()

while True:
    # Take accelerometer reading (left-right)
    reading = accelerometer.get_x()
    if reading < 100 and reading > -100:
        display.show(centre)
    elif abs(reading) >= 12 * scale_factor:
        display.show(full)
    elif reading >= 100:
        display.show(right_tilts[reading // scale_factor])
    else:
        display.show(left_tilts[abs(reading) // scale_factor])
    
    # Send a message with drive data
    if button_b.is_pressed():
        radio.send("go {}".format(reading))
    else:
        radio.send("stop")
    
    # Do this 10 times a second
    sleep(100)
        
