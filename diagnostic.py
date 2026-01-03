import winsound
import time

print("Testing Windows Media Sound...")

try:
    # This plays the standard Windows "Exclamation" sound
    # It uses the Media Driver (Speakers), not the Beeper Driver
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    print("Command Sent.")
except Exception as e:
    print(f"Error: {e}")