# Run the Docker File For Go Build

- sudo docker build -t google-maps-scraper-dev -f Dockerfile.dev .

# Copy the file outside from the docker container to the local directory

- sudo docker run --rm -v $(pwd):/app -w /app google-maps-scraper-dev go build -o google-maps-scraper

# run python script

- python3 start.py
