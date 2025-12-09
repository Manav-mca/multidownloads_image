import time
from datetime import datetime

def water_reminder():
    interval = 2 * 60 * 60  # 2 hours in seconds

    while True:
        print(f"💧 {datetime.now().strftime('%H:%M')} - Time to drink water!")
        time.sleep(interval)

if __name__ == "__main__":
    print("Water reminder started! Press Ctrl+C to stop.")
    try:
        water_reminder()
    except KeyboardInterrupt:
        print("\nReminder stopped.")
