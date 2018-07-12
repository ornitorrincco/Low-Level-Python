import socket
import os

# host to listen on
host = '192.168.0.5'
# create a raw socket and bind it to the public interfaces
if os.name == 'nt':
    socketProtocol = socket.IPPROTO_IP
else:
    socketProtocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socketProtocol)
sniffer.bind((host, 0))
# we want the IP headerss included in the captured
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
# if we'are using window, we need to esnt an IOCTL to set up promiscouos mode
if os.name == 'nt':
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
# read in a single packet
print(sniffer.recvfrom(65565))
# if we are using windows, turn off promiscouos mode
if os.name == 'nt':
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
