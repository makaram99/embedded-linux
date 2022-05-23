# Importing libraries
import RPi.IO as IO
import time

# Garbage Collector
IO.cleanup()

# Setting pins numbering mode (BCM or BOARD)
IO.setmode(IO.BOARD)

# Variables
ledPin = 12
button = 11

# Configuring pins
IO.setup(ledPin, IO.OUT)
IO.output(ledPin, False)
IO.setup(button, IO.IN)        # Pull Up / Pull Down disabledPin


# Super loop: Set ledPin High if Button is pressed, and Set Low otherwise.
while(1):
    if IO.input(button):
        print("Button is pressed (3.3v)")
        IO.output(ledPin, True)     # IO.HIGH = Non-Zero Value = True
    else:
        print("Button is not pressed (0v)")
        IO.output(ledPin, False)      # IO.LOW = Zero = False
    time.sleep(1)

# Garbage Collector
IO.cleanup()