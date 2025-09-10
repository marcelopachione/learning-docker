# Imagem Base
FROM python:3.10

# Definir qual será o Diretório de trabalho da App -> Container
WORKDIR /app

# Diretorio de dados
RUN mkdir -p /app/data

# Copiar o arquivo da aplicação
COPY ./app.py .

# Execução de entrada do conteiner/app
CMD ["python","app.py"]