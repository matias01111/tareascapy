from scapy.all import *

SRC_IP = "172.19.0.3"
DST_IP = "172.19.0.2"
SRC_PORT = 57662
DST_PORT = 3306

SEQ = 4124872161
ACK = 1530782586

payload = b"\x03\xff\xff\xff\xffFUZZINGCOMMAND\x00"

ip = IP(src=SRC_IP, dst=DST_IP)
tcp = TCP(sport=SRC_PORT, dport=DST_PORT, flags="PA", seq=SEQ, ack=ACK)

pkt = ip / tcp / Raw(load=payload)

send(pkt, verbose=1)
print("Paquete fuzzing2 enviado con payload y secuencia simulada")