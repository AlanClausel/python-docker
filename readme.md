# Desafio entrevista con Python y Docker

## Configuración de Vagrant :

En el directorio de tu proyecto, encontrarás una carpeta llamada "Vagrant". Esta carpeta contiene la configuración necesaria para levantar una máquina virtual.

1. **Iniciar la Máquina Virtual**: Ejecuta el siguiente comando dentro del directorio "Vagrant":
   ```bash
   vagrant up
   ```
2. **Conexión SSH**:  Para conectarte a la máquina virtual por SSH, utiliza el siguiente comando:
   ```bash
   vagrant ssh
   ```
3. **Túnel a la Máquina Host**: Puedes crear un túnel desde la máquina virtual a tu máquina host para acceder a servicios que se ejecuten en la VM desde el host. Utiliza el siguiente comando para configurar el túnel:
   ```bash
   vagrant ssh -- -L 5000:localhost:5000
   ```

## Ejecucion Dockerfile

1. **Dockerfile**: Es necesario un dockerfile para la construccion de la imagen, en este repositorio se encuentra el de este proyecto
2. **Construccion imagen**: Ejecuta el siguiente comando dentro del directorio donde se encuentre el "Dockerfile"
    ```bash
   docker build -t pythonApp .
   ```
3. **Ejecución docker**: Ejecute el siguiente comando con la imagen creada anteriormente para ejecutar el contenedor
    ```bash
   docker run -p 5000:5000 pythonapp
   ```

## Ejecucion del microservicio

En este punto hace referencia a hacer las solicitudes solicitadas en el desafio, los siguientes son 3 metodos HTTP 

1. **POST: Solicitar un archivo**: 
    Descripción: Envía datos al servidor para ser procesados.
    Uso común: Enviar datos del formulario, cargar archivos u otros datos al servidor.
    Comando a ejecutar:
    ```bash
   curl -X POST -F "file=@/vagrant/applicacion/archivos/usuario1.json" http://localhost:5000/upload
   ```
2. **GET: Listar los archivos disponibles**: 
    Descripción: Solicita datos del servidor.
    Uso común: Obtener información del servidor.
    ```bash
   curl http://localhost:5000/list
   ```
3. **DELETE: Borrar un archivo**: 
    Descripción: Solicita al servidor que elimine un recurso.
    Uso común: Utilizado para eliminar un recurso específico en el servidor.
    ```bash
   curl -X DELETE http://localhost:5000/delete/usuario1.json
   ```
