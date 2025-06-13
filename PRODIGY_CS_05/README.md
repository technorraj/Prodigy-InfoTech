# Packet Sniffer Tool

This Python program is a basic packet sniffer built using the Scapy library. It captures TCP packets and displays key details like source and destination IPs, ports, protocol number, and partial payloads. The tool is intended for **ethical and educational use only**.

This tool was developed as part of an internship at **The Prodigy Infotech**, demonstrating network traffic monitoring through packet analysis.


## Features

- **TCP Packet Capture**: Captures and displays key information about TCP packets.
- **Logging**: Saves captured packet details into a text file.
- **User Consent**: Includes a disclaimer and requires user agreement before proceeding.
- **Lightweight Analysis**: Extracts and logs IP, port, protocol, and basic payload information.


## Requirements

- Python 3.x
- [Scapy](https://scapy.net/) library

Install Scapy using pip:

```bash
pip install scapy
```


## Usage

### 1. Run the Script

```bash
python packet_sniffer.py
```

### 2. Accept Terms and Conditions

Type `y` to accept and proceed. If you do not accept, the program will exit.

### 3. Monitor Packets

The script will sniff **10 TCP packets** and display their details:

- Source and Destination IP
- Source and Destination Port
- Protocol Number
- Partial Payload (first 50 characters)

### 4. Log File Output

Captured packet information will be saved to a file named:

```
packet_sniffer_results.txt
```

You can open this file to review the logged data after execution.


## Disclaimer

This tool **must only be used on networks for which you have explicit permission**. Misuse of this tool may result in legal consequences. The developer is **not responsible for any misuse or resulting damages**.

---

>  **Note:** Always use ethical hacking tools responsibly and within legal boundaries.
