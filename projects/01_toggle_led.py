import RPi.IO as IO
import time

# Cleaning up the board
IO.cleanup()

# Set pin numbering
IO.setmode(IO.BOARD)

# Global Data
ledPin = 12

# Set pins direction
IO.setup(ledPin, IO.OUT)
IO.output(ledPin, False)
IO.output(ledPin, IO.HIGH)

# Super Loop
while(1):
	IO.output(ledPin, True)		# IO.HIGH = True = Non-Zero
	time.sleep(1)
	IO.output(ledPin, False)		# IO.LOW = False = Zero
	time.sleep(1)

# Cleaning up the IO
IO.cleanup()
