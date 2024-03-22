![main_docker](https://img.mandic.com.br/blog/2015/01/docker-image.png)

# DOCKER STUDIES


## Documentation

### [Link __docker-docs__  ](https://docs.docker.com/reference/cli/docker/container/run/)

### [Link __docker hub__  (Images Repo)](https://hub.docker.com)

> [!Note] 
>My goal here was to review some basic Docker commands and concepts by building simple images and applications. I didn't want to explain the theoretical aspects of what Docker is, because there are many great online resources for that already.


> [!WARNING] 
> REQUERIMENTS : docker, python, some IDE  | All here where developed using WLS2 (Ubunto) in vscode.

**There's tons of good contents about how to install the requeriments.**

This studies had a good documentation on the commands needed to get it done in each item. So follow up the order or jump to the Second and Third images if u got experencie already.

## (1)
```
 - Checking if Docker is installed
 - Making any needed Linux config changes
 - Running a simple "hello world" Docker
```

###  [first_commands_docker/first_steps.md](https://github.com/Gabriel-Philot/docker_studies/blob/main/first_commands_docker/first_steps.md)

## (2)
```
 - Using Dockerfile to define a simple image by specifying base image, adding files, running commands.
 - Building image with docker build, tagging with docker tag.
 - Running containers in foreground, detached, and interactive modes.
 - Naming containers, mapping ports, mounting volumes with docker run options.
 - Managing containers - start, stop, remove, list with docker (start|stop|rm|ps).
 - Removing images, cleaning up with docker (rmi|system prune).
 - Container networking basics - default bridges, linking.
```

###  [first_commands_docker/basic_commands.md](https://github.com/Gabriel-Philot/docker_studies/blob/main/first_commands_docker/basic_commands.md)

## (3)
```
 - Dockerfile basics - specifying base image, adding files, running commands to build image.
 - docker build to build Dockerfile into image.
 - Tagging images with docker tag to version them.
 - Pushing images to Docker Hub registry.
 - Multi-stage builds to optimize image sizes.
 - Build patterns - copy files, run commands, set environment variables.
 - Leveraging cache on rebuilds to improve efficiency.
 - Best practices - small containers, one process per container.
```

### [build_images/first_docker_image](https://github.com/Gabriel-Philot/docker_studies/tree/main/build_images/first_docker_image)

## (4)
```
 - Creating a Faasapi+Redis image with Dockerfile.
 - Docker-compose to run Redis and Faasapi containers together.
 - Using redis for persisting data on the aplication.
```

###  4:  [build_images/second_docker_image](https://github.com/Gabriel-Philot/docker_studies/tree/main/build_images/second_docker_image)

## (5)
```
 - Creating a Streamlit_SlotDataClass + Redis image with Dockerfile.
 - Docker-compose to run Redis and custumAplication containers together.
 - Using redis for persisting data on the aplication.
 - Diferent aproches via dockerfile/compose for using modules in the Streamlit_SlotDataClass volume.
```

###  5:  [build_images/third_docker_image](https://github.com/Gabriel-Philot/docker_studies/tree/main/build_images/third_docker_image)



![main_app](https://github.com/Gabriel-Philot/docker_studies/blob/main/build_images/third_docker_image/docker_classSlot.png)


> Hope this serve anyone and sorry about bad-writing, one of my goals here was to praticate this as well.

