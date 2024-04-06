FROM golang:1.21.1-bullseye as withnode

RUN apt-get update && \
    apt-get install -y ca-certificates npm nodejs net-tools && \
    npm install && \
    npx playwright@v1.25.0 install-deps

ENV GO111MODULE=on
#ENV CGO_ENABLED=1
ENV GOOS=linux
ENV GOARCH=amd64

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download
COPY . .
