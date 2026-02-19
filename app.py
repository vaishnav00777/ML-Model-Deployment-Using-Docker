from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "API is running successfully!"}

@app.get("/predict")
def predict(a: float, b: float, c: float, d: float):
    data = np.array([[a, b, c, d]])
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}
