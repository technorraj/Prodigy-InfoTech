# Keylogger

This Python program implements a basic keylogger designed for **educational and ethical** use only. It records the keystrokes made during a specified time period and logs them to a local text file along with timestamps.

This project was created as part of an internship at **The Prodigy Infotech**, focusing on demonstrating the use of Python libraries for monitoring input events in a secure and responsible environment.


## Disclaimer

**This program is intended strictly for learning and ethical research purposes.**

Before the program starts, users are required to accept terms and conditions that emphasize:
- Legal and ethical use only.
- Use only on systems where you have explicit permission.
- No use for data theft, privacy invasion, or illegal activity.


## Features

- **Key Logging**: Captures all key presses including special keys.
- **Timestamped Entries**: Each entry is logged with the exact date and time.
- **Log Duration Control**: Users can specify how long the keylogger should run.
- **Log File Output**: Stores keystrokes in a file named `keylogger_log.txt`.


## Requirements

- Python 3.x
- `pynput` library:
  ```bash
  pip install pynput

## Usage
Run the Script:
 ```bash
python Keylogger.py
 ```

- **Accept Terms and Conditions**: Enter `y` to proceed.

- **Enter Duration**: Input the number of seconds to log keystrokes.

- **Monitor**: The program will log all keystrokes to keylogger_log.txt in the same directory.

- **Log File Output**: fter the duration ends, a message will show the path to the saved log file.
