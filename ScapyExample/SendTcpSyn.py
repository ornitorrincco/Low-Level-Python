from scapy.all import *
conf.verb = 0

# p = IP(dst="github.com")/TCP()
p = IP(dst="192.168.0.6")/TCP()
r = sr1(p)
print(r.summary())
