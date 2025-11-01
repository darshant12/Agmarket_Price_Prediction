from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Smart Crop Market Price Prediction API")

# Allow frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load cleaned CSV
DATA_FILE = "cleaned_crop_data.csv"
data = pd.read_csv(DATA_FILE, parse_dates=['date'], index_col='date')

# Train a simple linear regression model
X = np.arange(len(data)).reshape(-1, 1)
y = data['price'].values
model = LinearRegression()
model.fit(X, y)

# Request model
class PredictRequest(BaseModel):
    days_ahead: int

@app.get("/")
def root():
    return {"message": "API is running!"}

@app.post("/predict")
def predict(request: PredictRequest):
    future_index = np.arange(len(data), len(data) + request.days_ahead).reshape(-1, 1)
    predicted_prices = model.predict(future_index)
    return {"predicted_prices": predicted_prices.tolist()}
