# English–Tamil Translation API (Dockerized)

This repository provides a deployment-ready inference system for an English–Tamil translation model using FastAPI, Gradio, and Docker.

## Model Source

The model used here is trained from scratch in a separate repository:

**Training Repository:** [[link-to-training-repo]](https://github.com/KAMALESH0081/English_Tamil_Machine_Translation)

---

## Features

* FastAPI backend for inference
* Gradio interface for user interaction
* Dockerized application
* Multi-container setup using Docker Compose
* Published image to Docker Hub
* Verified cross-machine portability

---

## Architecture

```
User → Gradio UI → FastAPI → Model → Response
```

---

## Docker Setup

### Run with Docker Compose

```
docker-compose up --build
```

This will:

* Start FastAPI backend
* Launch Gradio frontend
* Connect services internally

---

## Docker Hub Usage

### Pull Image

```
docker pull kamalesh0081/en-ta-translator:v3
```

### Run Container

```
docker run -p 8000:8000 kamalesh0081/en-ta-translator:v3
```

---

## API Endpoint

### POST /translate

```
{
  "text": "how are you"
}
```

### Response

```
{
  "translation": "எப்படி இருக்கிறீர்கள்"
}
```

---

## Local Setup (Without Docker)

Since the application uses separate frontend and backend services, you need to run them in **two terminals**.

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Start Backend (FastAPI)

```bash
uvicorn backend.app:app --reload
```

---

### 3. Start Frontend (Gradio)

```bash
python frontend/app_gradio.py
```

---

### Access

* FastAPI: http://localhost:8000
* Gradio UI: http://localhost:7860


---

## Validation

* Tested by pulling and running the container on a different machine
* Ensures reproducibility across environments

---

## What This Project Demonstrates

* End-to-end ML inference pipeline
* API development with FastAPI
* Multi-service orchestration using Docker Compose
* Reproducible deployment workflow
