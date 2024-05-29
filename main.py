import sys
import time


def print_newline():
    print("\n")


def type_message(message):
    for char in message:
        sys.stdout.write(char)  # Write to terminal
        sys.stdout.flush()  # Print to terminal
        time.sleep(0.02)  # Adjust the delay here


welcome_msg = "Welcome to CannaSelect. Here, we will take your requests, and give you the best strains. " \
              "With the legalization of marijuana, it is important to stay informed in order to remain safe. "
type_message(welcome_msg)
print_newline()

csv_file = open("strains_cleaned.csv", "r")

answer = str(input("Would you like for us to suggest a strain or do you need help finding more "
                                "information? "))

response_to_answer = "Awesome! We are excited to help keep you safe. You said: " + answer
type_message(response_to_answer)

csv_file.close()
