# Four Docker Image -> Spotify + Etlaplication + PostgresSQL

## Documentation

### [Link __docker-docs__  ](https://docs.docker.com/reference/cli/docker/container/run/)

### [Link __docker hub__  (Images Repo)](https://hub.docker.com)

### [Link __spotify docs__  (Developer)](https://developer.spotify.com/documentation/web-api/tutorials/getting-started)

## First start creating the following stetup + Local Dev test again:
same struture as the first docker image -> create dir src/api.py and dockerfile in the dir at same hierarchy as src.

### Start developing locally with the virutallenv

here to starta new venv -> `python3 -m venv venv`
`source venv/bin/activate`

> [!Tip]
> Start with developing the Extract part, then the Transform and Load parts separately, then integrate. This makes debugging easier.

So what i did was: Dev Api extraction, transforming the data and streanlit locally in venv.

> [!Tip]
> For dev the load part, i used one separete docker-compose, for getting up the postgress for test it

> [!WARNING]
> CAREFUL with the host connection when transiting from the test from venv to the docker_aplication.

### VENV  (module /src/resources/postgress) f.connection host: localhost
### Docker (module /src/resources/postgress) f.connection host: postgress (name of the postgress container in docker-compose.yaml)

> [!Tip]
> To make it simple, only change the variables in both .evn files.

#### add file Dockerfile and Docker-compose.yaml

`pip freeze` -> get all u need, here u could do with the requeriments auto, but care to not bring much heavy machines.

`deactivate` then `docker-compose up` after get the docker compose file ready

`docker-compose rm` if need to remove `docker ps -a`

`docker-compose up -d` (here this inst that good, cause if there's a error with streamlit, wil be good to see it.) +
`docker ps`

> [!WARNING]
> CAREFUL WITH THE IMAGE RESIDUE, sometimes its better to remove it in case u cant debug the aplication.


Below wil be some images of the app arquiteture and the final resulsts:


![Resume-draw](https://github.com/Gabriel-Philot/docker_studies/blob/main/build_images/spotify_aplication_image/src/resources/imgs/fluxo.png)

![result1](https://github.com/Gabriel-Philot/docker_studies/blob/main/build_images/spotify_aplication_image/src/resources/imgs/01_flux.png)

![result2](https://github.com/Gabriel-Philot/docker_studies/blob/main/build_images/spotify_aplication_image/src/resources/imgs/02_flux.png)
