from scapy.all import *

def modificar_paquete(pkt, opcion):
    nuevo_pkt = pkt.copy()

    if Raw in nuevo_pkt:
        payload = nuevo_pkt[Raw].load
    else:
        payload = b""

    if opcion == '1':
        print("[*] Aplicando modificación 1: Cambiando payload (ejemplo)")
        original = payload
        nuevo_payload = b"FUZZ1" + payload[5:] if len(payload) > 5 else b"FUZZ1"
        print(f"    Payload original: {original[:20]}...")
        print(f"    Payload modificado: {nuevo_payload[:20]}...")
        nuevo_pkt[Raw].load = nuevo_payload
    elif opcion == '2':
        original = nuevo_pkt[TCP].dport
        nuevo_pkt[TCP].dport = 3307
        print(f"[*] Aplicando modificación 2: Cambiando puerto destino TCP")
        print(f"    Puerto destino original: {original}")
        print(f"    Puerto destino modificado: {nuevo_pkt[TCP].dport}")
    elif opcion == '3':
        original = nuevo_pkt[TCP].flags
        nuevo_pkt[TCP].flags = "R"
        print(f"[*] Aplicando modificación 3: Cambiando bandera TCP")
        print(f"    Flags TCP original: {original}")
        print(f"    Flags TCP modificadas: {nuevo_pkt[TCP].flags}")
    else:
        print("[!] Opción inválida. Enviando paquete original")
        return None

    # Recalcular checksums IP y TCP
    del nuevo_pkt[IP].chksum
    del nuevo_pkt[TCP].chksum

    return nuevo_pkt

def interceptar(pkt):
    if pkt.haslayer(TCP) and (pkt[TCP].dport == 3306 or pkt[TCP].sport == 3306):
        print("\n[+] Paquete MySQL detectado:")
        print(pkt.summary())

        opcion = input("Seleccione modificación a aplicar (1, 2, 3): ")

        pkt_modificado = modificar_paquete(pkt, opcion)
        if pkt_modificado is None:
            return

        # Construir trama Ethernet para enviar el paquete con MAC corregida
        ether = Ether(src=pkt[Ether].src, dst=pkt[Ether].dst)
        full_pkt = ether / pkt_modificado[IP]

        sendp(full_pkt, iface="br-dfeb538b2e43", verbose=0)
        print("[+] Paquete modificado enviado correctamente con MAC corregida.")
        exit(0)

def main():
    iface = "br-dfeb538b2e43"
    print("[*] Iniciando sniffer de paquetes MySQL...")
    sniff(filter="tcp port 3306", iface=iface, prn=interceptar, store=0)

if __name__ == "__main__":
    main()