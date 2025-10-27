# [Docker](#Docker)

## [Content](#content)

- [Docker](Docker.md):
    - [What is Docker?](#introduction)
    - [Difference between Docker and Virtual Machines](#machines)
    - [Explore Images](#images)
    - [Explore Containers](#containers)
    - [Public and Private Registries](#registries)
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

<img width="60%"  alt="" src="https://github.com/user-attachments/assets/b3e8b694-e976-436f-a522-e8312bbe79a8" />


As a result, Docker images are much smaller compared to virtual machine images. Consequently, Docker can start containers much faster because virtual machines need to boot their own kernel every time, whereas Docker reuses the host’s kernel. Regarding compatibility, virtual machines allow you to run an image of any OS on a different host OS, for example, running a Linux virtual machine on a Windows machine. However, Docker does not provide this level of OS isolation directly, as containers rely on the host’s kernel. 

Docker was originally build for Linux OS , and so most of containers are Linux based. However later Docker made a update and developed the Docker Desktop for Windows and Mac that allows us to run Linux containers on Windows or Mac OS. 




