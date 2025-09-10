# Bind Mount

# Build image
docker build -t iss-tracker-bind-mount .

# Run container
docker run --rm --name iss-tracker-bind-mount -v ./data:/app/data iss-tracker-bind-mount