### Python Flask Application Skeleton 

### Dockerize
----------------------    

#### project build
    docker build -f docker/Dockerfile.dev -t flask-image:latest .

    docker build -f docker/Dockerfile.prod -t flask-image:latest .  

#### run daemon (localhost:5000 or 0.0.0.0:5000)
    docker run --name flask-image -p 5000:5000 -d flask-image:latest

#### show containers 
    docker ps

#### remove container
    docker rm -rf flask-image

#### run selected container
    docker start -i flask-image

#### stop selected container
    docker stop flask-image
