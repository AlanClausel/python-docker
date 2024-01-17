#!/bin/bash

# Nombre de la imagen y contenedor
IMAGE_NAME="pythonapp-image"
CONTAINER_NAME="pythonapp-container"

# Eliminar el contenedor si ya existe
if [ "$(docker ps -a -q -f name=$CONTAINER_NAME)" ]; then
    docker rm -f $CONTAINER_NAME
fi

# Construir la imagen de Docker
docker build -t $IMAGE_NAME .

# Ejecutar el contenedor
docker run -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME
