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