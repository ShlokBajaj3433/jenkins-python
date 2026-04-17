# Jenkins Python Project

Simple Python project with Docker and Jenkins pipeline support.

## Project Overview

This project runs one Python file:

- `app.py`

It prints:

- `Hello from Python project!`

The project also includes:

- `Dockerfile` for containerized execution
- `Jenkinsfile` for CI execution with Docker

## Project Structure

```text
project3-python/
  app.py
  Dockerfile
  Jenkinsfile
  README.md
```

## Prerequisites

Install:

- Python 3.10+
- Docker (optional)
- Jenkins (optional)

## Run Locally

From the `project3-python` folder:

```bash
python app.py
```

Expected output:

```text
Hello from Python project!
```

## Run with Docker

### 1. Build image

```bash
docker build --no-cache -t my-app .
```

### 2. Run container

```bash
docker run --rm my-app
```

Expected output:

```text
Hello from Python project!
```

## Run Jenkins Inside Docker

Use this setup when you want Jenkins itself to run in Docker and execute this project pipeline from there.

### 1. Start Jenkins container

```powershell
docker volume create jenkins_home

docker run -d --name jenkins `
  -p 8080:8080 -p 50000:50000 `
  -v jenkins_home:/var/jenkins_home `
  -v //var/run/docker.sock:/var/run/docker.sock `
  -v c:/codes/Jenkins:/workspace `
  jenkins/jenkins:lts-jdk17
```

### 2. Install Docker CLI inside Jenkins container

```powershell
docker exec -u 0 jenkins sh -c "apt-get update && apt-get install -y docker.io"
```

### 3. Open Jenkins and unlock

- URL: `http://localhost:8080`
- Get admin password:

```powershell
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Install suggested plugins and complete the first admin user setup.

## Jenkins Pipeline (Inside Docker Jenkins)

Current Jenkins pipeline has two stages:

1. Docker Build
2. Run Container

### Create Jenkins job for this project

1. Create a new **Pipeline** job.
2. Choose **Pipeline script from SCM**.
3. SCM: Git
4. Repository URL: `https://github.com/ShlokBajaj3433/jenkins-python.git`
5. Branch: `main`
6. Script Path: `Jenkinsfile`
7. Click **Build Now**.

### Notes

- This setup uses Docker-outside-of-Docker via the mounted Docker socket.
- If multiple jobs run in parallel, image name collisions can happen because the current image tag is `my-app`.

## Troubleshooting

- `python: command not found`:
  - Install Python and add it to PATH
- Docker command errors:
  - Install Docker and verify daemon is running
- Jenkins cannot run Docker:
  - Ensure Docker socket is mounted and Docker CLI is installed in the Jenkins container

## Keep It Simple and Standard

- Run with `python app.py`
- Use Dockerfile for container runs
- Use Jenkinsfile for automated build and run
