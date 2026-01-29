.PHONY: build run lint clean help

IMAGE_NAME = sensorsunrise
MEGALINT_IMAGE = oxsecurity/megalinter:latest

help:
	@echo "Available commands:"
	@echo "  make build    - Build Docker image"
	@echo "  make run      - Run interactive container"
	@echo "  make lint     - Run Black on code"
	@echo "  make clean    - Remove Docker image"

build:
	docker build -t $(IMAGE_NAME) .

run: build
	docker run -it --device=/dev/i2c-1 -v $(PWD):/app $(IMAGE_NAME)

lint: build
	docker run -it -v $(PWD):/app $(IMAGE_NAME) black src/

clean:
	docker rmi -f $(IMAGE_NAME)
