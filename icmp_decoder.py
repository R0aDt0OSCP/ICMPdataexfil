import scapy.utils
from scapy.all import *
scapy_cap = scapy.utils.rdpcap('foren4.pcap') #file to parse
print(scapy_cap)
s=''
for p in scapy_cap[ICMP]:
    print(p[ICMP].type) #list type of packet
    print(p.show())     #raw structure of packet
    
    if p[ICMP].type==8:
       s=s+' '+str((p[IP].ttl))

print (s)
#printing flag of ctf file
print(bytes(map(int, s.split())).decode())
