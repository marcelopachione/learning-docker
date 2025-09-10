## Faz o build da imagem
    docker build -t iss-tracker .

## --rm → Execucao unica, container é removido apos execucao  (não fica listado em docker ps -a)
    docker run --rm iss-tracker