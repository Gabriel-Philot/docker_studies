# Third Docker Image -> Streamlit_SlotDataClass + Redis

## Documentation

### [Link __docker-docs__  ](https://docs.docker.com/reference/cli/docker/container/run/)

### [Link __docker hub__  (Images Repo)](https://hub.docker.com)

## First start creating the following stetup + Local Dev test again:
same struture as the first docker image -> create dir src/api.py and dockerfile in the dir at same hierarchy as src.

### Start developing locally with the virutallenv

then cd back to the first docker image dir and run `source venv/bin/activate`

`pip install streamlit` + `pip install redis`

> [!NOTE]
> My goal here where to study the performance of sloting in dataClass, but but free to go with other python use.

> Like the second-image, desenvolve first the solution without redis and streamlit (only the python part), then went to adding booth and adjusting the code, the trick thing here is that maybe have an better way to debuging with redis, but i did tons of dockers-composes to adjust, cause redis was required to be running for the tests.

> [!Tip]
> Start developing the streamlit locally `streamlit main.py`


#### add file Dockerfile and Docker-compose.yaml

`pip freeze` -> get all u need, here u could do with the requeriments auto, but care to not bring much heavy machines.

`deactivate` then `docker-compose up` after get the docker compose file ready

`docker-compose rm` if need to remove `docker ps -a`

`docker-compose up -d` (here this inst that good, cause if there's a error with streamlit, wil be good to see it.) +
`docker ps`

> [!WARNING]
> CAREFUL WITH THE IMAGE RESIDUE, sometimes its better to remove it in case u cant debug the aplication.

> [!IMPORTANT]
> webbrowser [localhost:8501] now the count will be saved in redis and if the aplication stop and run the counting will still be there

> Here other test can be done with stoping a single container with `docker stop container_id` and run `docker start container_id`
betwen this two commands the count will be saved in redis. That can be checked on the terminal and inside the docker container with `docker exec -it container_id bash` and `redis-cli`.

![main_app](https://github.com/Gabriel-Philot/docker_studies/blob/main/build_images/third_docker_image/docker_classSlot.png)


Problably wil use this v0 to envolve in a more mature and strutured v1. That will cover in more deep the analises of the usage of slots in classes and related topics do the aplication, for this v0 the focus were puraly the making a custumaplication with persistant data.
