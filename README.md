# Tarea Análisis y Modificación de Tráfico MySQL con Scapy

## Contenido
- `Dockerfile-scapy`: Dockerfile para construir la imagen con Scapy y herramientas de red.
- `scripts/modificar_paquete.py`: Script principal para interceptar y modificar paquetes MySQL en tiempo real.
- `scripts/fuzzing1.py`: Script que envía un paquete TCP con flag RST para fuzzing.
- `scripts/fuzzing2.py`: Script que envía un payload personalizado con TCP PA para fuzzing.
- `docker_commands.sh`: Comandos para crear y ejecutar contenedores Docker para servidor MySQL, cliente y atacante con Scapy.

## Instrucciones

1. Construir la imagen Scapy:

```bash
docker build -t scapy-image -f Dockerfile-scapy .
```
2. Crear y levantar los contenedores MySQL

Ejecutar el script para crear la red y levantar los contenedores:

```bash
chmod +x docker_commands.sh
./docker_commands.sh 
```

3. Ejecutar el contenedor atacante con Scapy

Este contenedor permitirá interceptar y modificar paquetes con acceso a las interfaces de red:

```bash
docker run --rm -it \
  --network host \
  --cap-add=NET_ADMIN \
  --cap-add=NET_RAW \
  --entrypoint bash \
  -v $(pwd)/scripts:/scripts \
  scapy-image
  ```

4. Uso de los scripts en el contenedor atacante
Dentro del contenedor, para ejecutar el sniffer y modificador de paquetes:

```bash
python3 /scripts/modificar_paquete.py

Para enviar el paquete fuzzing 1 (TCP con flag RST):
python3 /scripts/fuzzing1.py

Para enviar el paquete fuzzing 2 (payload anómalo con TCP PA):
python3 /scripts/fuzzing2.py
```

Notas adicionales
La interfaz usada en modificar_paquete.py está configurada para br-dfeb538b2e43. Cambiarla si su entorno usa una distinta.

Las direcciones IP y puertos están definidos para los contenedores en la red Docker. Ajustar si cambia la configuración.

El script modificar_paquete.py solicita interacción para elegir qué modificación aplicar a cada paquete interceptado.

Se recomienda ejecutar Wireshark para verificar visualmente la captura y efectos de las modificaciones y fuzzing.


Referencias

- [Scapy Documentation](https://scapy.readthedocs.io/en/latest/)
- [Docker Documentation](https://docs.docker.com/)
- [MySQL Official Documentation](https://dev.mysql.com/doc/)

Autor
Matías Mora
Fecha: Julio 2025