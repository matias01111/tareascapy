from scapy.all import *

SRC_IP = "172.19.0.3"
DST_IP = "172.19.0.2"
SRC_PORT = 12345
DST_PORT = 3306

ip = IP(src=SRC_IP, dst=DST_IP)
tcp = TCP(sport=SRC_PORT, dport=DST_PORT, flags="R", seq=1000)

pkt = ip / tcp

send(pkt, verbose=1)
print("Paquete fuzzing1 enviado (TCP con RST)")