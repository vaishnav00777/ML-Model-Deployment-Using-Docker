# ML Model Deployment Using FastAPI & Docker

## 📌 Project Overview
This project demonstrates how to deploy a Machine Learning model as a REST API using FastAPI and Docker.

## 🚀 Features
- Train ML model
- Save model as .pkl
- Load model using FastAPI
- Expose /predict endpoint
- Docker containerization

## 🛠 Tech Stack
- Python
- Scikit-learn
- FastAPI
- Uvicorn
- Docker

## ▶️ How to Run Locally

Install dependencies:
pip install -r requirements.txt

Run server:
uvicorn app:app --reload

Open browser:
http://127.0.0.1:8000/docs

## 🐳 Run Using Docker

Build image:
docker build -t ml-api .

Run container:
docker run -p 8000:8000 ml-api

## 📤 Example Response

{
  "prediction": 0
}

