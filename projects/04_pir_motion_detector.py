# Importing libraries
import RPi.IO as IO
import time

# Garbage Collector
IO.cleanup()

# Setting pins numbering mode (BCM or BOARD)
IO.setmode(IO.BOARD)

# Variables
ledPin = 12
pirPin = 11

# Configuring pins
IO.setup(ledPin, IO.OUT)
IO.output(ledPin, False)
IO.setup(pirPin, IO.IN)        # Pull Up / Pull Down disabledPin

# Super loop: Turn on led if PIR detects someone, and Off otherwise.
while(1):
    if(IO.input(pirPin)):
        print("BeeBeeBee... A thief is there. Catch him!!!")
        IO.output(ledPin, True)     # IO.HIGH = Non-Zero Value = True
        time.sleep(10)
    else:
        print("You are safe, relax Mr. X")
        IO.output(ledPin, False)      # IO.LOW = Zero = False
    time.sleep(1)
    
# Garbage Collector
IO.cleanup()