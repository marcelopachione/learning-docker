# Build images
docker build -t server-side -f dockerfile.server .
docker build -t client-side -f dockerfile.client .

# Create bridged network
docker network create marcelo-network

# Run server side
docker run --name con-server-side --network marcelo-network server-side

# Run client side
docker run --name con-client-side --network marcelo-network client-side


