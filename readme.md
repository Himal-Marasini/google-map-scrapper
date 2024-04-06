# Run the Docker File For Go Build

- sudo docker build -t google-maps-scraper -f Dockerfile .

# Copy the file outside from the docker container to the local directory in Ubuntu(amd64)

- sudo docker run --rm -v $(pwd):/app -w /app google-maps-scraper go build -o google-maps-scraper

# Copy the file outside from the docker container to the local directory in Ubuntu(arm64)

- sudo docker run --rm -v $(pwd):/app -w /app google-maps-scraper go build -buildvcs=false -o google-maps-scraper

# run python script

- python3 start.py
