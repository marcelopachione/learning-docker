# Learning-docker

## 1. Basic Docker Concepts and Terms

### 1. Docker Image
A lightweight, stand-alone, executable package that includes everything needed to run a piece of software.

### 2. Docker Container
A runtime instance of a Docker image.

### 3. Docker Hub
A cloud-based registry service where Docker users and partners create, test, store, and distribute container images.

### 4. Dockerfile
A text document that contains all the commands a user could call on the command line to assemble an image.

### 5. Docker Compose
A tool for defining and running multi-container Docker applications.

---

## 2. Basic Docker Commands

- `docker --version`: Display Docker version.  
- `docker info`: Display system-wide information.  
- `docker run image`: Run a Docker container from an image.  
- `docker ps`: List running Docker containers.  
- `docker ps -a`: List all Docker containers.  
- `docker stop container_id`: Stop a running container.  
- `docker rm container_id`: Remove a Docker container.  
- `docker images`: List Docker images.  
- `docker rmi image_id`: Remove a Docker image.  
- `docker pull image`: Pull an image from a Docker registry (Docker Hub by default).  
- `docker push image`: Push an image to a Docker registry.  
- `docker exec -it container_id command`: Execute a command in a running container.  
- `docker logs container_id`: Fetch the logs of a container.  
- `docker start`: Starts one or more stopped containers.  
- `docker stop`: Stops one or more running containers.  
- `docker build`: Builds an image from a Dockerfile.  
- `docker pull`: Pulls an image or a repository from a registry.  
- `docker push`: Pushes an image or a repository to a registry.  
- `docker export`: Exports a container’s filesystem as a tar archive.  
- `docker exec`: Runs a command in a run-time container.  
- `docker search`: Searches the Docker Hub for images.  
- `docker attach`: Attaches to a running container.  
- `docker commit`: Creates a new image from a container’s changes.  

---

## 3. Intermediate Docker Commands

- `docker run -d image`: Run a Docker container in detached mode.  
- `docker run -p host_port:container_port image`: Map a port from the host to a container.  
- `docker run -v host_volume:container_volume image`: Mount a volume from the host to a container.  
- `docker run -e VAR=VALUE image`: Set environment variables in a container.  
- `docker inspect container_id/image_id`: Return low-level information on Docker objects.  
- `docker build -t tag .`: Build a Docker image with a tag from a Dockerfile in the current directory.  
- `docker tag image new_tag`: Tag an image with a new tag.  

---

## 4. Dockerfile Commands

- `FROM image`: Set the base image.  
- `RUN command`: Run a command.  
- `CMD command`: Set a default command that will run when the container starts.  
- `ENV VAR=VALUE`: Set environment variables.  
- `ADD source destination`: Copy files from source to the container's filesystem at the destination.  
- `COPY source destination`: Copy new files or directories from source and add them to the container.  
- `ENTRYPOINT command`: Configure a container to run as an executable.  
- `LABEL`: Adds metadata to an image.  
- `EXPOSE`: Informs Docker that the container listens on the specified network ports at runtime.  
- `VOLUME`: Creates a mount point and marks it for externally mounted volumes.  
- `USER`: Sets the user (or UID/GID) to run the image and subsequent instructions.  
- `WORKDIR`: Sets the working directory for subsequent instructions.  
- `ARG`: Defines a variable passed at build-time with `docker build`.  
- `ONBUILD`: Adds a trigger instruction when the image is used as a base for another build.  

---

## 5. Docker Compose Commands

- `docker-compose up`: Create and start containers.  
- `docker-compose down`: Stop and remove containers, networks, images, and volumes.  
- `docker-compose build`: Build or rebuild services.  
- `docker-compose logs`: View output from containers.  
- `docker-compose restart`: Restart services.  
- `docker-compose pause`: Pause services.  
- `docker-compose unpause`: Unpause services.  
- `docker-compose start`: Start existing containers for a service.  
- `docker-compose stop`: Stop running containers without removing them.  
- `docker-compose config`: Validate and view the compose file.  

---

## 6. Docker Networking

- `docker network ls`: List networks.  
- `docker network create network`: Create a network.  
- `docker network rm network`: Remove a network.  
- `docker network inspect network`: Display detailed information on one or more networks.  

### Network Drivers

- **Bridge**:  
  Docker's default networking driver. If no driver is specified, this is the default.

- **Host**:  
  For standalone containers, removes network isolation between the container and the host.

- **Overlay**:  
  Connects multiple Docker daemons together and enables swarm services to communicate.

- **Macvlan**:  
  Assigns a MAC address to a container, making it appear as a physical device on the network.  

---

## 7. Docker Volumes

- `docker volume ls`: List volumes.  
- `docker volume create volume`: Create a volume.  
- `docker volume rm volume`: Remove a volume.  
- `docker volume inspect volume`: Display detailed information on one or more volumes.  

---

## 8. Docker Object Commands

- `docker image`: Manages images.  
- `docker container`: Manages containers.  
- `docker network`: Manages networks.  
- `docker volume`: Manages volumes.  
- `docker secret`: Manages Docker secrets.  
- `docker plugin`: Manages plugins.  

---

## 9. Docker Advanced Commands

- `docker history image`: Show the history of an image.  
- `docker save image > file`: Save an image to a tar archive.  
- `docker load < file`: Load an image from a tar archive.  
- `docker commit container image`: Create a new image from a container’s changes.  

---

## 10. Docker System Commands

- `docker info`: Displays system-wide information.  
- `docker version`: Shows the Docker version information.  
- `docker system df`: Shows Docker disk usage.  
- `docker system events`: Gets real-time events from the server.  
- `docker system prune`: Removes unused data.  

---