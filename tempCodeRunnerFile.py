
    while True:
        print(f"water {datetime.now().strftime('2:30')} - Time to drink water!")
        time.sleep(interval)

if __name__ == "__main__":
    print("water reminder started! Press Ctrl+C to stop.")
    try:
        water_reminder()
    except KeyboardInterrupt:
        print("\nReminger stopped.")

