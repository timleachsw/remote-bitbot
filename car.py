from microbit import *
import radio


# The maximum amount to reduce the motor speed by when turning
turn_max_sub = 1023

# The assumed maximum reading; turning the controller further than this won't do anything
max_reading = 800

# Images, for debugging
full_im = Image("99999:99999:99999:99999:99999")
none_im = Image("00000:00000:00000:00000:00000")
righ_im = Image.ARROW_E
left_im = Image.ARROW_W
stop_im = Image("90009:09090:00900:09090:90009")

# Define functions
def go_straight():
    pin0.write_digital(1)
    pin1.write_digital(1)
    pin8.write_digital(0)
    pin12.write_digital(0)

def stop():
    pin0.write_digital(0)
    pin1.write_digital(0)
    pin8.write_digital(0)
    pin12.write_digital(0)

def go_right(reading):
    # Clip
    if reading > max_reading:
        reading = max_reading
    
    # Left motor full speed ahead
    pin0.write_digital(1)
    pin8.write_digital(0)
    
    # Right motor change based on reading
    pin1.write_analog(1023 - (reading / max_reading) * turn_max_sub)
    pin12.write_digital(0)
    
def go_left(reading):
    if reading < -max_reading:
        reading = -max_reading
        
    pin1.write_digital(1)
    pin12.write_digital(0)
    
    pin0.write_analog(1023 + (reading / max_reading) * turn_max_sub)
    pin8.write_digital(0)

# Turn radio on
radio.on()

while True:
    # Get radio message
    message = radio.receive()
    if message:
        # Only do anything if the message begins with "go"
        if message[0:2] == "go":
            reading = int(message[3:])
            if reading < 100 and reading > -100:
                # Drive straight ahead
                go_straight()
                display.show(full_im)
            elif reading >= 100:
                # Turn right
                go_right(reading)
                display.show(righ_im)
            else:
                # Turn left
                go_left(reading)
                display.show(left_im)
        elif message == "stop":
            # Stop the engines
            stop()
            display.show(stop_im)
