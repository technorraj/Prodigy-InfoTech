import os
import sys
from scapy.all import sniff, IP, TCP

def display_disclaimer():
    print("----------- Packet Sniffer Tool Disclaimer -----------")
    print("This tool is intended for EDUCATIONAL and ETHICAL use only.\n")
    print("By proceeding, you agree to the following:")
    print("1. You have explicit permission to monitor the network.")
    print("2. You will not use this tool to break any laws or policies.")
    print("3. You will not harm, disrupt, or exploit systems or data.")
    print("4. You accept full responsibility for how you use this tool.")
    print("5. The developer is not liable for any misuse or damages.")
    print("6. Redistribution is prohibited without author consent.")
    print("7. Always respect privacy and data confidentiality.")

    consent = input("\nDo you accept the terms? (y/n): ").strip().lower()
    if consent != 'y':
        print("Access denied. Exiting the tool.")
        sys.exit()

def process_packet(packet):
    if packet.haslayer(TCP) and packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        protocol = packet[IP].proto
        payload = str(packet[TCP].payload)

        packet_info = (
            f"Source IP       : {src_ip}\n"
            f"Destination IP  : {dst_ip}\n"
            f"Source Port     : {src_port}\n"
            f"Destination Port: {dst_port}\n"
            f"Protocol Number : {protocol}\n"
            f"Payload         : {payload[:50]}...\n"
            "--------------------------------------------------\n"
        )

        print(packet_info)
        with open("packet_sniffer_results.txt", "a") as log_file:
            log_file.write(packet_info)

def main():
    display_disclaimer()
    
    print("\n📡 Starting TCP packet sniffing...")
    print("Capturing 10 TCP packets...\n")

    try:
        sniff(filter="tcp", prn=process_packet, store=0, count=10)
    except KeyboardInterrupt:
        print("\nSniffing interrupted by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit()

    output_file = os.path.abspath("packet_sniffer_results.txt")
    print(f"\n Packet sniffing complete. Results saved to:\n{output_file}")

if __name__ == "__main__":
    main()

