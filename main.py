import sys
import time


def type_message(message):
	for char in message:
		sys.stdout.write(char) # Write to terminal
		sys.stdout.flush() # Print to terminal
		time.sleep(0.05) # Adjust the delay here


welcome_msg = "Welcome to CannaSelect. Here, we will take your requests, and give you the best strains. With the legalization of marijuana, it is important to stay informed in order to remain safe"
type_message(welcome_msg)


csv_file = open("strains_cleaned.csv", "r")

