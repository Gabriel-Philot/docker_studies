# Basic Commands

# [Link __docker hub__  (Repositorio de imagens)](https://hub.docker.com)

### *Searching images*

`docker search ngingx`

`docker search airflow`

... cold search for other public images on docker hub.

 ### *Looking out for local images and containers*

`docker images` or `docker images ls`

`docker container ls` or `docker ps`


 ### *Pulling images*

 `docker pull nginx` by default it will pull the latest one -> Using default tag: latest

 `docker images`

 ### *Runing pulled image*

 `docker run nginx`

> [!IMPORTANT]
> When u run a docker on the terminal, that terminal wil be like ocupied with this operation, for the sake to see whats going on, u can go to other terminal and run `docker ps` to see the container running.

- control + c  | would stop the running countainer

so if u run `docker ps` after it, u sholdnt see the container running.

### *See stoped docker cointainers*

`docker ps -a`

### *Removing containers*

`docker rm <container id>` in this example after running `docker ps -a`, we can see the container id, so we can run for example `docker rm bd3378bae039` to remove it.

> [!WARNING]
> For removing an container, first it needs to be stoped.

> [!TIP]
> Remove all containers, using `docker rm $(docker ps -a -q)`,



### *Now running a container with the run detached mode from the terminal*
i.e. -d = detached mode

`docker run -d nginx`

`docker ps`

### *Stoping a running cointainer that is in detached mode*

`docker stop <container id>` -> get the container id from `docker ps`


### *Running a container with a pulished image*
i.e -p = published

`docker run -d -p 8080:80 nginx`