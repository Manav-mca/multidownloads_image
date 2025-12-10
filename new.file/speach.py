import win32com.client

def speak_text(text: str) -> None:
    """
    Uses Windows SAPI to speak the given text aloud.
    """
    try:
        # Create SAPI voice object
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(text)
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Windows SAPI Text-to-Speech")
    print("Type '-1' to exit.\n")

    while True:
        user_input = input("Enter text to speak: ").strip()
        
        # Exit condition
        if user_input == "-1":
            print("Exiting...")
            break
        
        # Skip empty input
        if not user_input:
            print("Please enter some text.")
            continue
        
        speak_text(user_input)

if __name__ == "__main__":
    main()

