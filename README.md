# Basic Network Sniffer

## Overview

This project is a simple Python-based Network Sniffer built using the Scapy library. It captures network packets in real time, analyzes their structure, and displays useful information such as source and destination IP addresses, protocols, ports, and payload data.

## Features

- Capture live network packets
- Identify TCP, UDP, and ICMP protocols
- Display source and destination IP addresses
- Display source and destination port numbers
- Extract and display packet payloads
- Detect non-IP packets
- Capture a specified number of packets before stopping

## Technologies Used

- Python 3
- Scapy

## Installation

```bash
pip install scapy
```

### Windows Users

Install Npcap from https://npcap.com/

## Usage

```bash
python basic_packet_sniffer.py
```

## Project Structure

```text
Basic-Network-Sniffer/
├── basic_packet_sniffer.py
├── README.md
└── requirements.txt
```

## Disclaimer

This tool is intended for educational and ethical purposes only. Use it only on networks that you own or have permission to monitor.
