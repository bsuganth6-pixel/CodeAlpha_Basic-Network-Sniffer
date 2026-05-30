from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def handle_packet(packet):
    """This function is called for every captured packet"""
    
    # Check if packet has an IP layer
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        # Determine protocol
        if TCP in packet:
            proto = "TCP"
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            print(f"[TCP] {src_ip}:{sport} -> {dst_ip}:{dport}")
        elif UDP in packet:
            proto = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            print(f"[UDP] {src_ip}:{sport} -> {dst_ip}:{dport}")
        elif ICMP in packet:
            proto = "ICMP"
            print(f"[ICMP] {src_ip} -> {dst_ip} (ping or error)")
        else:
            proto = "Other IP"
            print(f"[{proto}] {src_ip} -> {dst_ip}")
        
        # Extract payload if present (first 60 bytes)
        if Raw in packet:
            payload = packet[Raw].load
            print(f"    Payload (first 60 bytes): {payload[:60]}")
        print("-" * 60)
    else:
        # Non-IP packet (like ARP)
        print(f"Non-IP packet: {packet.summary()}")

# Start sniffing – capture 10 packets then stop
print("Sniffing 10 packets... Press Ctrl+C to stop early")
sniff(prn=handle_packet, count=10)
print("Done capturing.")