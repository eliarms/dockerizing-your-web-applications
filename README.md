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