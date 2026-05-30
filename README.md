# CodeAlpha_Basic-Network-Sniffer
#Basic Network Sniffer
##Overview
This project is a simple Python-based Network Sniffer built using the Scapy library. It captures network packets in real time, analyzes their structure, and displays useful information such as source and destination IP addresses, protocols, ports, and payload data.
The project helps beginners understand how data travels through networks and how common protocols such as TCP, UDP, and ICMP operate.
________________________________________
##Features
●	Capture live network packets
●	Identify TCP, UDP, and ICMP protocols
●	Display source and destination IP addresses
●	Display source and destination port numbers
●	Extract and display packet payloads
●	Detect and display non-IP packets
●	Capture a specified number of packets before stopping
________________________________________
##Technologies Used
●	Python 3
●	Scapy
________________________________________
##Installation
1. Clone the Repository
git clone https://github.com/your-username/basic-network-sniffer.git
cd basic-network-sniffer

2. Install Dependencies
pip install scapy

3. Windows Users
Install Npcap from:
https://npcap.com/
During installation, enable:
●	Install Npcap in WinPcap API-compatible Mode
●	Start Npcap driver at boot time
________________________________________
##Usage
Run the script with administrator/root privileges.
python basic_packet_sniffer.py

The program will capture 10 packets and display details such as:
●	Protocol Type
●	Source IP Address
●	Destination IP Address
●	Source Port
●	Destination Port
●	Payload Data
________________________________________
Sample Output
Starting Network Sniffer...

[TCP PACKET]
Source IP       : 192.168.1.5
Destination IP  : 142.250.183.78
Source Port     : 52341
Destination Port: 443
Payload (first 60 bytes): b'...'

------------------------------------------------------------

________________________________________
##Project Structure
Basic-Network-Sniffer/
│
├── basic_packet_sniffer.py
├── README.md
└── requirements.txt

________________________________________
Learning Outcomes
●	Understanding packet sniffing fundamentals
●	Learning network protocols (TCP, UDP, ICMP)
●	Analyzing packet headers and payloads
●	Working with Python networking libraries
●	Exploring cybersecurity and network monitoring concepts
________________________________________
Disclaimer
This tool is intended for educational and ethical purposes only. Use it only on networks that you own or have explicit permission to monitor. Unauthorized packet sniffing may violate laws, regulations, or organizational policies.
________________________________________
Author
Suganth
Cybersecurity & Python Development Enthusiast

