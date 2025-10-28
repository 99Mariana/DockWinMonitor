# [Docker](#Docker)

## [Content](#content)

- [Docker](Docker.md):
    - [What is Docker?](#introduction)
    - [Difference between Docker and Virtual Machines](#machines)
    - [Images and Containers?](#images_containers)
    - [Creation of a Dockerfile](#dockerfile)
    - [Docker Compose](#dockercompose)
    - [Main Docker commands](#commands)


### What is Docker?
> [Docker](#Docker) > [Content](#content) > [This section](#introduction)

Docker is a virtualization software that helps developers create, run, and manage applications more easily. It works by packaging application in a container with all necessary dependencies, configurations, system tools and runtime. Containers are lightweight and can run on any computer in the same way, which prevents problems that happen when an application works on one machine but not another. 

It also makes it easier to share applications with other developers or teams, because the container includes everything needed to run the application correctly. Docker standardizes how services are run in local development environments, removing the need for developers to manually install and configure all dependencies on their own machines. Using Docker, developers can quickly deploy applications, update them without breaking other parts of the system, and run multiple applications on the same computer without conflicts. Addicionaly Docker allow developers to have different versions of the same app without any conflicts. 

### Difference between Docker and Virtual Machines
> [Docker](#Docker) > [Content](#content) > [This section](#machines)

To explore the different of Docker and Virtual Machines is important to go a little bit deeper and undestand how an Operating system is made up. An operating system have to main layer: Operating System Kernel and the Operating System Application Layer. 

**Operating System Kernel** -> Is the core of operating systems, kernel interacts between hardware and software components. The kernel of the OS is the one that talk to the hardware components to allocate resources like CPU, memory storage, etc... to the applications then running on that operating system. 

**Operating System Application Layer** -> The applications, like word, google chrome, etc... are part of the Os Application layer and they run on top of the kernel layer.

Both Docker and Virtual Machines are virtualization tools; however, the main difference between them lies in the part of the operating system they virtualize. Docker virtualizes the OS application layer, so when we run a Docker container, it contains the applications and services installed on top of that layer, such as the Java Runtime or Python. Unlike virtual machines, Docker containers share the host’s kernel, as they do not have their own operating system kernel.

The virtual machine virtualize both Operating System Kernel layer and Operating System Application Layer. 

<p align="center">
<img width="60%"  alt="" src="https://github.com/user-attachments/assets/b3e8b694-e976-436f-a522-e8312bbe79a8" />
</p>


As a result, Docker images are much smaller compared to virtual machine images. Consequently, Docker can start containers much faster because virtual machines need to boot their own kernel every time, whereas Docker reuses the host’s kernel. Regarding compatibility, virtual machines allow you to run an image of any OS on a different host OS, for example, running a Linux virtual machine on a Windows machine. However, Docker does not provide this level of OS isolation directly, as containers rely on the host’s kernel. 

Docker was originally build for Linux OS , and so most of containers are Linux based. However later Docker made a update and developed the Docker Desktop for Windows and Mac that allows us to run Linux containers on Windows or Mac OS. 

### Images and Containers
> [Docker](#Docker) > [Content](#content) > [This section](#images_containers)

A Docker image is an executable application artifact that can be easily shared and moved between systems. It can be uploaded to an artifact repository and then downloaded to a server whenever needed. A Docker image not only includes the application’s source code but also the complete environment configuration. This ensures that the application runs the same way on any system, making deployment faster and more reliable. 

The image is like a immutable template that defines how container will be realized. A container is a running instance of a image, and corresponde of the moment when the environment is created. And so for an image we can run multiple containers.

Docker Hub is a cloud-based repository service where developers can store, share, and manage Docker images: https://hub.docker.com/search?badges=official

To upload an image using Docker Desktop, simply run a command like the one below in the Docker terminal:

```
docker pull {name}:{tag}
```

The tag is a identifier for the different versions of an image. 

### Creation of a Dockerfile
> [Docker](#Docker) > [Content](#content) > [This section](#dockerfile)

To create a custom image, you need to create a Dockerfile, which serves as a “definition” of how to build an image from your application.
For a more detailed explanation of how to do this, I recommend watching this video (starting at 49:10): https://www.youtube.com/watch?v=pg19Z8LL06w

An example of a Dockerfile would be something like this:
````
# Dockerfile
FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
````

This Dockerfile defines how to build a Docker image,  specifying which dependencies to install, which application files to copy, and which command to execute when the container starts. This code example starts with ````FROM python:3.12````, which gives the container a ready-to-use Python 3.12 environment. It sets /app as the working folder inside the container using WORKDIR /app, so all commands run from there. The requirements.txt file is copied into the container with ````COPY requirements.txt```` ., and ````RUN pip install --no-cache-dir -r requirements.txt```` installs all the needed Python packages without keeping unnecessary cache files. Then, COPY . . adds the rest of your project files to the container. Finally, ````CMD ["python", "app.py"]```` tells the container to run your Python application when it starts.

Then to build the image, we execute this command
```
docker build -t my_app .
```
And to run it :
```
docker run -p 5000:5000 my_app
```


### Docker Compose
> [Docker](#Docker) > [Content](#content) > [This section](#dockercompose)

When we already have the images we want to use, it is common to create a Docker Compose file to define how to run the containers. This file specifies which images to use (including those built from Dockerfiles), the ports to expose, volumes to mount, networks to connect, environment variables, and other configuration options that control how the containers interact with each other and with the host system. 

Using Docker Compose is especially used when multiple containers need to work together, for example, in a project that monitors Windows servers using Prometheus and Grafana. In this case, one container could run Prometheus to collect metrics, another Grafana to visualize them, and optionally exporters to gather Windows-specific metrics. Instead of manually running each container with ````docker run````, Docker Compose allows to define everything in a single YAML file, including container dependencies. This approach makes it much easier to start, stop, and manage the entire monitoring stack consistently, both in development and in production.

````
services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus:/etc/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
    restart: unless-stopped

  grafana:
    image: grafana/grafana:10.4.3
    container_name: grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana-data:/var/lib/grafana
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=admin
      - GF_FEATURE_TOGGLES_ALERTINGTEMPLATESINLABELSANNOTATIONS=true
    restart: unless-stopped
    depends_on:
      - prometheus

volumes:
  grafana-data:
````
Explaining a little bit of the code below: 

The **Prometheus** service uses the official Prometheus image and exposes port 9090 to access its web interface. It mounts a local folder `./prometheus` to `/etc/prometheus` inside the container, allowing Prometheus to read its configuration file (`prometheus.yml`), and the `command` specifies which config file to use. The `restart: unless-stopped` option ensures the container restarts automatically unless explicitly stopped.

The **Grafana** service uses the official Grafana image (version 10.4.3) and exposes port 3000 for its web interface. It persists data using a Docker volume called `grafana-data`, sets environment variables to define the admin username and password, and enables a specific feature toggle. With `depends_on: - prometheus`, Grafana starts after Prometheus, and `restart: unless-stopped` ensures it restarts automatically. 

Finally, the **volumes** section defines `grafana-data` as a named volume to persist Grafana dashboards, settings, and data even if the container is removed.

Related to this document is important to know some commands: 
* **Navigate to the folder containing your docker-compose.yml file:** `cd /path/to/your/project`
* **Build images:** `docker-compose build`
* **Run containers:** `docker-compose up` (add `-d` for background)
* **Build & run together:** `docker-compose up --build`
* **Stop containers:** `docker-compose down`

### Main Docker commands
> [Docker](#Docker) > [Content](#content) > [This section](#commands)

#### **General Docker Commands**

| Command                | Description                                                                                                            |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `docker --version`     | Displays the installed Docker version.                                                                                 |
| `docker info`          | Shows detailed system-wide information about Docker, including number of containers, images, storage driver, and more. |
| `docker help`          | Lists all available Docker commands and options.                                                                       |
| `docker login`         | Authenticates with a Docker registry (like Docker Hub).                                                                |
| `docker logout`        | Logs out from a Docker registry.                                                                                       |
| `docker search <term>` | Searches Docker Hub (or another registry) for images by keyword.                                                       |


#### **Container Commands**

| Command                                              | Description                                                                     |
| ---------------------------------------------------- | ------------------------------------------------------------------------------- |
| `docker run <image>`                                 | Creates and starts a container from a specified image.                          |
| `docker run -d <image>`                              | Runs a container in detached mode (in the background).                          |
| `docker run -it <image> /bin/bash`                   | Runs a container interactively with a terminal session (ideal for debugging).   |
| `docker run --name <container_name> <image>`         | Assigns a custom name to the container when it’s created.                       |
| `docker run -p <host_port>:<container_port> <image>` | Maps a port from the host to the container (for exposing web apps, APIs, etc.). |
| `docker run -v <host_path>:<container_path> <image>` | Mounts a local directory or volume to a path inside the container.              |
| `docker start <container_id>`                        | Starts a stopped container.                                                     |
| `docker stop <container_id>`                         | Gracefully stops a running container.                                           |
| `docker restart <container_id>`                      | Restarts a running container.                                                   |
| `docker pause <container_id>`                        | Pauses all processes inside a container.                                        |
| `docker unpause <container_id>`                      | Resumes all processes inside a paused container.                                |
| `docker rm <container_id>`                           | Removes a stopped container from the system.                                    |
| `docker exec -it <container_id> <command>`           | Executes a command inside a running container (e.g., `bash` or `sh`).           |
| `docker logs <container_id>`                         | Shows the standard output (stdout/stderr) logs of a container.                  |
| `docker stats`                                       | Displays a live stream of resource usage (CPU, memory, I/O) for all containers. |
| `docker top <container_id>`                          | Lists running processes inside a container.                                     |

#### **Image Commands**

| Command                                               | Description                                                                      |
| ----------------------------------------------------- | -------------------------------------------------------------------------------- |
| `docker images`                                       | Lists all local Docker images with repository, tag, and size info.               |
| `docker pull <image>`                                 | Downloads an image from a remote Docker registry (like Docker Hub).              |
| `docker push <image>`                                 | Uploads a local image to a remote registry (requires `docker login`).            |
| `docker build -t <image_name> .`                      | Builds a new Docker image from a Dockerfile in the current directory.            |
| `docker build --no-cache -t <image_name> .`           | Builds an image from scratch, ignoring all cached layers.                        |
| `docker build -f <Dockerfile_name> -t <image_name> .` | Builds an image using a specific Dockerfile.                                     |
| `docker rmi <image_id>`                               | Removes one or more images from the local system.                                |
| `docker tag <image_id> <repo>:<tag>`                  | Tags an existing image with a new name or version tag.                           |
| `docker history <image>`                              | Shows the history of an image’s layers and commands used to build it.            |
| `docker inspect <image>`                              | Displays detailed JSON metadata about an image (environment vars, labels, etc.). |

#### **Network Commands**

| Command                                                     | Description                                          |
| ----------------------------------------------------------- | ---------------------------------------------------- |
| `docker network ls`                                         | Lists all Docker networks available on the host.     |
| `docker network create <network_name>`                      | Creates a new custom network.                        |
| `docker network inspect <network_name>`                     | Shows detailed information about a specific network. |
| `docker network connect <network_name> <container_name>`    | Connects a container to an existing network.         |
| `docker network disconnect <network_name> <container_name>` | Disconnects a container from a network.              |
| `docker network prune`                                      | Removes all unused networks.                         |

#### **Volume Commands**

| Command                               | Description                                             |
| ------------------------------------- | ------------------------------------------------------- |
| `docker volume ls`                    | Lists all Docker-managed volumes.                       |
| `docker volume create <volume_name>`  | Creates a new named volume for persistent data storage. |
| `docker volume inspect <volume_name>` | Displays metadata and mount paths for a volume.         |
| `docker volume rm <volume_name>`      | Removes a named volume (must not be in use).            |
| `docker volume prune`                 | Deletes all unused volumes to reclaim disk space.       |

#### **Filesystem & Data Commands**

| Command                                       | Description                                                                  |
| --------------------------------------------- | ---------------------------------------------------------------------------- |
| `docker cp <container_id>:<path> <host_path>` | Copies files or directories **from a container to the host**.                |
| `docker cp <host_path> <container_id>:<path>` | Copies files or directories **from the host to a container**.                |
| `docker diff <container_id>`                  | Shows changes made to files and directories inside a container’s filesystem. |

#### **Inspection & Monitoring Commands**

| Command                         | Description                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------ |
| `docker ps`                     | Lists currently running containers.                                                        |
| `docker ps -a`                  | Lists all containers, including stopped ones.                                              |
| `docker inspect <object_id>`    | Displays detailed information about a container, image, network, or volume in JSON format. |
| `docker events`                 | Streams real-time events from the Docker daemon (useful for monitoring).                   |
| `docker logs -f <container_id>` | Follows (streams) live container logs.                                                     |
| `docker stats`                  | Displays live performance metrics of running containers.                                   |

#### **Docker Compose Commands**

| Command                  | Description                                                                      |
| ------------------------ | -------------------------------------------------------------------------------- |
| `docker-compose up`      | Builds, creates, and starts all services defined in a `docker-compose.yml` file. |
| `docker-compose down`    | Stops and removes all services, networks, and volumes created by Compose.        |
| `docker-compose ps`      | Lists running containers managed by Docker Compose.                              |
| `docker-compose logs`    | Displays aggregated logs from all Compose services.                              |
| `docker-compose build`   | Builds or rebuilds services defined in a Compose file.                           |
| `docker-compose restart` | Restarts all running Compose services.                                           |

#### **Docker Swarm (Orchestration)**

| Command                                          | Description                                                            |
| ------------------------------------------------ | ---------------------------------------------------------------------- |
| `docker swarm init`                              | Initializes a Docker Swarm cluster on the current node (as a manager). |
| `docker swarm join`                              | Joins another node to the Swarm as a worker or manager.                |
| `docker node ls`                                 | Lists all nodes in the Swarm cluster.                                  |
| `docker service create --name <service> <image>` | Creates and deploys a new service in the Swarm.                        |
| `docker service ls`                              | Lists all active services in the Swarm.                                |
| `docker service scale <service>=<replicas>`      | Scales a service to a specific number of replicas.                     |
| `docker service logs <service>`                  | Displays logs for a specific Swarm service.                            |

#### **System Cleanup & Maintenance**

| Command                  | Description                                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------------------- |
| `docker system prune`    | Removes all unused data: stopped containers, dangling images, unused networks, and build cache. |
| `docker container prune` | Deletes all stopped containers.                                                                 |
| `docker image prune`     | Removes all dangling (unused) images.                                                           |
| `docker network prune`   | Removes all unused networks.                                                                    |
| `docker volume prune`    | Removes all unused volumes.                                                                     |
| `docker system df`       | Displays disk space usage by Docker objects (containers, images, volumes).                      |

#### **Health Checks & Environment Variables**

| Command                                                        | Description                                                                  |                                                                 |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------- |
| `HEALTHCHECK` *(Dockerfile instruction)*                       | Defines a command in a Dockerfile that periodically checks container health. |                                                                 |
| `docker inspect --format='{{json .State.Health}}' <container>` | Checks the current health status of a container.                             |                                                                 |
| `docker run -e <VAR>=<value> <image>`                          | Sets environment variables inside a container at runtime.                    |                    
