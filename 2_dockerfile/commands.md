** Faz o build da imagem **


docker build -t iss-tracker .

** --rm → faz com que o container seja removido automaticamente assim que ele parar de rodar (não fica listado em docker ps -a depois). **


docker run --rm iss-tracker