# Imagem Base
FROM python:3.10

# Definir qual será o Diretório de trabalho da App -> Container
WORKDIR /app

# Diretorio de dados
RUN mkdir -p /app/data

# Copiar o arquivo de config de dependencias
COPY requirements.txt requirements.txt

# Copiar o arquivo da aplicação
COPY iss_tracker.py app.py

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Execução de entrada do conteiner/app
CMD ["python","app.py"]