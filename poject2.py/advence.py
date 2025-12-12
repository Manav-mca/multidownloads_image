import time
from datetime import datetime
import json
import os

try:
    from plyer import notification
    HAS_NOTIFICATIONS = True
except ImportError:
    HAS_NOTIFICATIONS = False

class WaterReminder:
    def __init__(self):
        self.data_file = "water_log.json"
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {"daily_goal": 8, "consumed": 0, "drink_times": [], "date": datetime.now().strftime('%Y-%m-%d')}
    
    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def reset_daily_data(self):
        today = datetime.now().strftime('%Y-%m-%d')
        if self.data.get("date") != today:
            self.data = {"daily_goal": 8, "consumed": 0, "drink_times": [], "date": today}
            self.save_data()
    
    def notify(self, title, message):
        if HAS_NOTIFICATIONS:
            notification.notify(title=title, message=message, timeout=10)
        print(f"{datetime.now().strftime('%H:%M')} - {message}")
    
    def log_drink(self):
        self.reset_daily_data()
        current_time = datetime.now().strftime('%H:%M')
        self.data["consumed"] += 1
        self.data["drink_times"].append(current_time)
        self.save_data()
        remaining = max(0, self.data["daily_goal"] - self.data["consumed"])
        self.notify("Water Logged!", f"Glass #{self.data['consumed']} at {current_time} | Remaining: {remaining}")
    
    def show_history(self):
        if self.data["drink_times"]:
            times = ", ".join(self.data["drink_times"])
            print(f"Today's drinks: {times}")
        else:
            print("No drinks recorded today")
    
    def remind(self):
        remaining = max(0, self.data["daily_goal"] - self.data["consumed"])
        self.notify("Drink Water!", f"Stay hydrated! {remaining} glasses left today")
    
    def start(self):
        self.reset_daily_data()
        print("Water Reminder started!")
        print("Commands: 'd' = log drink, 'h' = show history, 'q' = quit")
        
        while True:
            self.remind()
            
            for _ in range(120):  # 2 hours = 120 minutes
                time.sleep(60)
                
                try:
                    import msvcrt
                    if msvcrt.kbhit():
                        key = msvcrt.getch().decode('utf-8').lower()
                        if key == 'd':
                            self.log_drink()
                        elif key == 'h':
                            self.show_history()
                        elif key == 'q':
                            return
                except ImportError:
                    pass

if __name__ == "__main__":
    reminder = WaterReminder()
    try:
        reminder.start()
    except KeyboardInterrupt:
        print("\nReminder stopped.")

# # Water Reminder App

# A Python app that reminds you to drink water every 2 hours with time tracking.

# ## Features
# - Desktop notifications
# - Daily water intake tracking (8 glasses goal)
# - Time recording for each drink
# - Persistent data storage

# ## Usage
# ```bash
# python advence.py
