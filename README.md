# Link Extractor

A Python program that, given any number of HTTP URLs as command line parameters, connects to each URL, extracts all links from it, and depending on the `-o` option, outputs either:

- One absolute URL per line
- A JSON hash where the key is the base domain, and the array is the relative path

## Features

- Extracts links from given URLs
- Outputs links in different formats (stdout, JSON, CSV)
- Uses Kubernetes for deployment
- Uses Docker for containerization
- CI/CD pipeline with GitHub Actions
- Code quality and coverage analysis with SonarCloud

## Requirements

- Python 3.9
- Docker
- Kubernetes
- GitHub Actions
- SonarCloud

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Medamine97/link_extractor.git
   cd link_extractor

2. Install the required Python packages:

    pip install -r requirements.txt

## Usage

# Command Line

Run the program with URLs and output format:
    
    python myprogram.py -u "https://news.ycombinator.com/" -o "stdout"

# Docker

    docker build -t link_extractor .
    docker run -it --rm link_extractor -u "https://news.ycombinator.com/" -o "stdout"

# Kubernetes

1. Apply the Kubernetes manifests:

    kubectl apply -f k8s/

2. Check the status of the deployment:

    kubectl get pods

3. Access the service:

    kubectl port-forward svc/myprogram-service 8080:80

    Then, open your browser and go to http://localhost:8080

## CI/CD Pipeline

The project uses GitHub Actions for CI/CD. The pipeline includes:

* Building and pushing Docker images
* Running tests and generating coverage reports
* Deploying to Kubernetes

# GitHub Actions Workflow

The workflow file is located at docker-image.yml.

## Configuration
The application uses a ConfigMap for configuration. The ConfigMap is defined in myprogram-configmap.yaml.

## Secrets
The application uses a Kubernetes Secret for storing sensitive information. The Secret is defined in myprogram-secret.yaml.


