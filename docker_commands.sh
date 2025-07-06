#!/bin/bash

# Crear red docker personalizada (si no existe)
docker network create mysql-net || echo "La red mysql-net ya existe"

# Levantar contenedor servidor MySQL
docker run -d --name mysql-server \
  --network mysql-net \
  -e MYSQL_ROOT_PASSWORD=rootpassword \
  -e MYSQL_DATABASE=testdb \
  mysql:8.0

# Levantar contenedor cliente MySQL
docker run -dit --name mysql-client \
  --network mysql-net \
  mysql:8.0 bash

echo "Contenedores mysql-server y mysql-client creados y corriendo en red mysql-net."
echo "Para el contenedor atacante con Scapy usar el comando docker run proporcionado en README."