# Importing libraries
import RPi.IO as IO
import time

# NOTEs:
# IO.LOW = Zero = False
# IO.HIGH = Non-Zero Value = True

# Garbage Collector
IO.cleanup()

# Setting pins numbering mode (BCM or BOARD)
IO.setmode(IO.BOARD)

# Global Data
ledPin = 12
ldrPin = 11
morningState = False

# Configuring pins
IO.setup(ledPin, IO.OUT)
IO.output(ledPin, False)
IO.setup(ldrPin, IO.IN)        # Pull Up / Pull Down disabledPin

# Super loop: turn on led if in evening, and off if in morning
while 1:
    if(IO.input(ldrPin) == morningState):
        print("Good morning")
        IO.output(ledPin, False)      
    else:
        print("Good evening")
        IO.output(ledPin, True)
    time.sleep(1)

# Garbage Collector
IO.cleanup()