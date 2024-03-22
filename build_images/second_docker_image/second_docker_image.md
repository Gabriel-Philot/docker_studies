# Second Docker Image -> Fastapi + Redis

## Documentation

### [Link __docker-docs__  ](https://docs.docker.com/reference/cli/docker/container/run/)

### [Link __docker hub__  (Repositorio de imagens)](https://hub.docker.com)

## First start creating the following stetup + Local Dev test again:
same struture as the first docker image -> create dir src/api.py and dockerfile in the dir at same hierarchy as src.
copy paste last api.py from first docker image into the second.

### Then add those things

`count = 0` into the api.py and below at async def root() above return `count +=1`
(better look at the final file and compare with the first one)

then cd back to the first docker image dir and run `source venv/bin/activate`
then back to the second docker image dir to run `uvicorn src.api:app --reload`

> [!IMPORTANT]
> webbrowser [localhost:8000](http://127.0.0.1:8000)

if u keep F+5 the count will rise while app its up, but when u stoped u lose this cache memory.

### ADD Redis

`pip install redis` inside the venv -> add redis stuff

> [!WARNING]
> if run `uvicorn src.api:app --reload` there wil be a error cause redis its not running.

#### add file Docker-compose.yaml

look at docker hub to get redis tag and add it to the docker-compose.yaml
look at docs docker at compose specification get first exemple to modifiet

`pip freeze` -> get redis
add redis on docker file

`deactivate` then `docker-compose up` after get the docker compose file ready

`docker-compose rm` if need to remove `docker ps -a`

`docker-compose up -d` + `docker ps`
for the detached mode

> [!WARNING]
> CAREFUL WITH THE IMAGE RESIDUE, sometimes its better to remove it in case u cant debug the aplication.

> [!IMPORTANT]
> webbrowser [localhost:8080] now the count will be saved in redis and if the aplication stop and run the counting will still be there

Here other test can be done with stoping a single container with `docker stop container_id` and run `docker start container_id`
betwen this two commands the count will be saved in redis. That can be checked on the terminal and inside the docker container with `docker exec -it container_id bash` and `redis-cli`.

