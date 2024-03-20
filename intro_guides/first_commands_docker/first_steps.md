# Starting with docker

## Checking out if docker is installed

`docker ps   |    check if there is any cointainer up`

or
`sudo docker ps`

> [!TIP] 
> For the porpouse of making this reading easier supose that everthing shold/could be used with `sudo` first.

`docker -v `

all cointainers

- docker ps -a   | check if there is any cointainer up OR down

### Configuration / setting up for dont need to use sudo anymore

```
groupadd docker 

sudo usermod -aG docker $USER

newgrp docker
```

### First runs
```
docker run hello-world
docker ps -a
docker images
docker run hello-world | Second run without the download.
docker ps -a
```