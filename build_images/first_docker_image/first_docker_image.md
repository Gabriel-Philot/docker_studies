# First Docker Image

## Documentation

### [Link __docker-docs__  ](https://docs.docker.com/reference/cli/docker/container/run/)

### [Link __docker hub__  (Repositorio de imagens)](https://hub.docker.com)


## DEV LOCAL app first

### Creating a folder in the directory (first_docker_image)
then navegate in to it via cd for creating a virtualenv

`python3 -m venv venv`  dont forget to add this in the .gitignore file

### Creating a folder in the directory (first_docker_image/src)
#### Creat api.py file inside of it.

entering the venv with: `source venv/bin/activate` 

_the porpose here its for dev first the app then deploy it to the docker_

### Installing dependencies in the virtualenv

`pip install faastapi`

on the file api.py use this base code below.

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Dev our API"}

```

`pip install uvicorn`  package responsable for connecting the api with the uvicorn server

`uvicorn src.api:app --reload`

> [!IMPORTANT]
> webbrowser [localhost:8000](http://127.0.0.1:8000)

on the file api.py use this base code below.

```
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Dev API</title>
            
            <style>
                body {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                }
                
                .title {
                    font-size: 5rem;
                    font-weight: bold;
                    font-family: sans-serif;
                }
                
            </style>
            
        </head>
        <body>
            <div class="title">
                Dev API [fastapi]
            </div>
        </body>
        </html>
    """

@app.get("/helthz")
async def helth():
    return {
        "message": "ok!"
        }
```

> [!IMPORTANT]
> Save and F5 -> webbrowser [localhost:8000](http://127.0.0.1:8000)


> [!IMPORTANT]
> Save and F5 -> webbrowser [localhost:8000/helthz]


> [!IMPORTANT]
> Save and F5 -> webbrowser [localhost:8000/docs]

exit with Control C on the terminal

## Create docker image

### Create Dockerfile

go on docker hub and search for the latest alpine tag 3.19


[Dockerfile]
```
FROM alpine:3.17.0

RUN apk add --no-cache python3 py3-pip

RUN pip3 install --no-cache-dir fastapi==0.110.0 uvicorn==0.29.0

EXPOSE 8000

COPY ./src /app

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0"]

```

then run `docker build -t firstimage:1.0.0 .` -> docker build -t(tag) {name}:{tag} {dir}

`docker images` -> `docker run -p 8080:8000 --rm -d firstimage:1.0.0`

`docker ps`

> [!IMPORTANT]
> webbrowser [localhost:8080]  |  [localhost:8080/helthz] | [localhost:8080/docs]

`docker ps` + `docker stop {id}`


## PUSH docker image to Repo

Create new repo on the docker Hub | get the short cut : `docker push gabrielphilot/firstimage:tagname`

`docker tag firstimage:1.0.0 gabrielphilot/firstimage:1.0.0` + `docker images`

`docker push gabrielphilot/firstimage:1.0.0`

> [!WARNING]
> request wil be denied if dont log with the cli docker first.

To fix it, need to login

`docker login` -> login + pass 

`docker push gabrielphilot/firstimage:1.0.0`

`docker images`

### Removing local images for then pull from repo

`docker image rm gabrielphilot/firstimage:1.0.0` + `docker image rm firstimage:1.0.0`

can use the --force in the removel if find something wrong.

`docker images` |  `docker ps -a`


### Pull the image from the repo

`docker pull gabrielphilot/firstimage:1.0.0` + `docker images`

now running it

`docker run -p 9090:8000 --rm -d gabrielphilot/firstimage:1.0.0` diferent ip just for fun?

`docker ps`

> [!IMPORTANT]
> webbrowser [localhost:9090]

`docker stop {id}` + `docker ps -a` + `docker images` + `docker image rm {id}`