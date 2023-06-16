
import scapy.all as scapy

request = scapy.ARP()

request.pdst = '192.168.1.1/24'
broadcast = scapy.Ether()

broadcast.dst = 'ff:ff:ff:ff:ff:ff'

request_broadcast = broadcast / request
clients = scapy.srp(request_broadcast, timeout = 1)[0]

print("")
print(" ____________________________")
print("|-New IP----|----New MAC-|")
print("l-------------|--------------j")
print("")
for element in clients:
    print(element[1].psrc + " | " + element[1].hwsrc)
print("")
print("Network scan finished...")

