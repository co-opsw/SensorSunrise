# My Python Project

## Setup with Docker

Build the image:
```bash
docker build -t my-python-project .
```

Run and develop:
```bash
docker run -it -v $(pwd):/app my-python-project
```

Inside the container, run your Python scripts.
