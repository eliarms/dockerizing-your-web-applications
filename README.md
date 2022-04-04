# Dockerizing Your Web Applications

Pratical example on how to docckerize various web applications.


**What is Docker ?**

Docker is a platform for consistently building, running, and shipping applications

## Container vs Virtual Machine

| Container                                            | Virtual Machine                               |
|------------------------------------------------------|-----------------------------------------------|
| A container is an isolated environment for running an application. It’s essentially an operating-system process with its own file system | A virtual machine is an abstraction of hardware resources. Using hypervisors we can create and manage virtual machines. The most popular hypervisors are VirtualBox, VMware and Hyper-v (Windows-only).
|Containers are very lightweight and start quickly because they share the kernel of the host (which is alreadystarted).  | Virtual machines are very resource intensive and slow to start|


**Docker Architecture**

Docker uses client/server architecture. It has a client component that talks to the server
using a RESTful API. The server is also called the Docker engine (or daemon) runs in
the background and is responsible for doing the actual work

- Using Docker, we can bundle an application into an image. Once we have an image, we
can run it on any machine that runs Docker.

- An image is a bundle of everything needed to run an application. That includes a
cutdown OS, a runtime environment (eg Node, Python, etc), application files, thirdparty
libraries, environment variables, etc.

- To bundle an application into an image, we need to create a Dockerfile. A Dockerfile
contains all the instructions needed to package up an application into an image

- We can share our images by publishing them on Docker registries. The most popular
Docker registry is Docker Hub

**Dockerfile instructions**

- FROM         # to specify the base image 
- WORKDIR      # to set the working - directory
- COPY         # to copy files/directories
- ADD          # to copy files/directories
- RUN          # to run commands 
- ENV          # to set environment variables
- EXPOSE       # to document the port the container is listening on
- USER         # to set the user running the app
- CMD          # to set the default command/program
- ENTRYPOINT   # to set the default command/program

**Image commands**
- docker build -t <name> .
- docker images 
- docker image ls 
- docker run -it <image> sh

**Starting and stopping containers**
- docker stop <containerID> 
- docker start <containerID

**Removing containers**

- docker container rm <containerID> 
- docker rm <containerID> 
- docker rm -f <containerID>   # to force the removal
- docker container prune  # to remove stopped containers

**Volumes**

- docker volume ls
- docker volume create app-data
- docker volume inspect app-data
- docker run -v app-data:/app/data <image>

**Copying files between the host and containers**

- docker cp <containerID>:/app/log.txt .
- docker cp secret.txt <containerID>:/app

**Sharing source code with containers**

- docker run -v $(pwd):/app <image>