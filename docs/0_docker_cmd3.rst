PS C:\Users\kusun> docker run -p 4000:80 friendlyhello
C
docker.exe: Error response from daemon: driver failed programming external connectivity on endpoint distracted_ramanujan (d3af3790911357379e736a389bcfb9047ca20a595281d8d853415bcf7cd79b78): 
Error starting userland proxy: mkdir /port/tcp:0.0.0.0:4001:tcp:172.17.0.2:80: input/output error.
PS

docker run -p 8080:8080 hello-world
docker run -p 127.0.0.1:22:22


docker ps -a -q | ForEach { docker stop $_ }
위와 같이 해결이 되었다.
https://stackoverflow.com/questions/49693353/error-response-from-daemon-driver-failed-programming-external-connectivity-on-e?rq=1


----------
docker tag friendlyhello kusung25/get-started:part2

docker push kusung25/get-started:part2


docker run -p 4000:80 kusung25/get-started:part2


docker run -i -t -v /src/webapp:/dst/webapp ubuntu /bin/bash

docker run -it --rm -p 8888:8888 -v C:\Users\kusun\my_dir:/root/mount/ heatonresearch/jupyter-python-r:latest


docker run -i -t -v C:\Users\kusun\my_dir:/root/mount/ ubuntu /bin/bash


docker stack ls                                            # List stacks or apps
docker stack deploy -c <composefile> <appname>  # Run the specified Compose file
docker service ls                 # List running services associated with an app
docker service ps <service>                  # List tasks associated with an app
docker inspect <task or container>                   # Inspect task or container
docker container ls -q                                      # List container IDs
docker stack rm <appname>                             # Tear down an application
docker swarm leave --force      # Take down a single node swarm from the manager
