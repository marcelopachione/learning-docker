# Volumes - Gerenciado pelo proprio Docker (Sem acesso local ao volume)

### Build image
    docker build -t sqlite-db-docker .

### Create volume
    docker volume create vol-sqlite-db-docker

### Run container - Primeira execucao
    docker run --name sqlite-db-docker -it -v vol-sqlite-db-docker:/app/data sqlite-db-docker

### Testar se o volume esta mantendo os dados
    docker rm sqlite-db-docker
    docker run --name sqlite-db-docker -it -v vol-sqlite-db-docker:/app/data sqlite-db-docker

### Run container - Demais execucoes apos insercao de dados no volume no container ja existente
    docker start -i sqlite-db-docker