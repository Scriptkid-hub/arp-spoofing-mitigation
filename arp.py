from scapy.all import *

def make_invisible():
    # Craft a spoofed ARP response
    arp_response = ARP(op=2, pdst="0.0.0.0", hwdst="ff:ff:ff:ff:ff:ff", psrc="192.168.1.1", hwsrc="00:11:22:33:44:55")

    # Send the spoofed ARP response
    send(arp_response, verbose=False)

def main():
    print("Making the computer invisible on the network...")
    try:
        while True:
            make_invisible()
            time.sleep(2)  # Send ARP response every 2 seconds
    except KeyboardInterrupt:
        print("\nExiting...")

if _name_ == "_main_":
    main()