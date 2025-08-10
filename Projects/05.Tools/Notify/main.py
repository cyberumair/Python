import os
import time

title = "⏳ One Hour Passed!"
body = "Focus on your Cyber Sec goal @cyberUmair.\nDon't waste your time in low-level things..."

while True:
    os.system(f'notify-send "{title}" "{body}" -t 7000') # Show for 7 seconds
    time.sleep(3600) # Runs after 1 hour
