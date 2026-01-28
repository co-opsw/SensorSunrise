# My Python Project

## Setup with Docker

Build the image:
```bash
docker build -t sensorsunrise .
```

Run and develop:
```bash
docker run -it -v $(pwd):/app sensorsunrise
```

Inside the container, run your Python scripts.
