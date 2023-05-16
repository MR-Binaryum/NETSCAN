# NETSCAN

NETSCAN its a software make in python that you can know all hosts connected to the network that are you connected.

When you execute the program you can get IP addreses and MAC addreses so with this data you can try later to get info of MAC addreses and scan ports of IP's.


In this part of code you have to put the IP address of youre gateway and know youre netmask

request.pdst = '192.168.1.1/24'

example ip of my gateway: 192.168.4.1

example netmask:  255.255.255.0 -> 0 = no bits
                   
                   255.255.255
                   |   |   |   
                   8 + 8 + 8 = 24 bits of netmask are = to 256 host on the network -2 (id broadcast and network id are = 254)


####Requeriments####

git 

python3

python3-pip

python3-scapy

####EXECUTE#######

git clone https://github.com/MR-Binaryum/NETSCAN.git

cd NETSCAN

sudo python3 scanner.py
