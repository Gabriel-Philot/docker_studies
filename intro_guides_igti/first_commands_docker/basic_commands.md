# Basic Commands

# [Link __Docs-Docker__  ](https://docs.docker.com/reference/cli/docker/container/run/)

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

`docker run -d -p 8080:80 nginx` then get the id with `docker ps`.

> [!IMPORTANT]
> webbrowser [localhost:8080](http://localhost:8080/)

going inside the container with: `docker exec -it 8acb88f2a1ac bash`

- (inside the container -> _root@...._) 
`ls -lh` files and dirs of the container

Extracting the same html from localhost inside the cointainer via terminal.
`cd usr/share/nginx/html/` -> `ls` -> `cat index.html`

Now exit -> `exit` | Back to the terminal.


## PART II

> [!IMPORTANT]
> Using the **hmtl** from the previus part.


> [!WARNING]
> CAREFULL ABOUT CHANGING DIRS/FILE NAMES, THIS CAN CAUSE ISSUES.



`mkdir my-html` -> `nano my-html/index.html` here use base of the html.

Exemple:
```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1> My test HTML for docker study with Nginx! </h1>
<body>
<html>
```

- control + o  then enter | saving inside nano 
- control + x | exit

The file should look into the my-html dir, here the file could be created, using the normal way.


### *Creating the volume that use this new htmlt instead of the deafult one*
i.e. -v = volume

`docker ps` -> get the container id
`docker stop <container id>` -> `docker rm <container id>`

now we can create the volume with:
`docker run -d -v {absolute_path_internal}:{path_container}:{reading_only} -p 8080:80 nginx` -> -v {variable} example 

correct one :
`docker run -d -v /home/gabriel/linux_folder/studies/docker_03/intro_guides_igti/first_commands_docker/my-html:/usr/share/nginx/html:ro -p 8080:80 nginx`

now adding `--rm` to automate the removel of the container when it stops.

exemple
`docker run -d -v {absolute_path_internal}:{path_container}:{reading_only}:ro -rm -p 8080:80 nginx` 

correct one :
`docker run -d -v /home/gabriel/linux_folder/studies/docker_03/intro_guides_igti/first_commands_docker/my-html:/usr/share/nginx/html/:ro --rm -p 8080:80 nginx`


> [!WARNING]
> Could have trouble wich permission on the folder here -> ``sudo chmod -R 755 /src` not recommended put its a way to goo.


> [!Note]
> webbrowser [localhost:8080](http://localhost:8080/) Shold have your transformed html.