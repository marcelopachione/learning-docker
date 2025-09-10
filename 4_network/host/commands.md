# Build images
docker build -t docker-side .

# Run script local_server.py no host
python3 local_server.py

# Run container docker client
docker run --network host docker-side





