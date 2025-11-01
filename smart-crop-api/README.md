# Smart Crop Market Price Prediction API

This project is a FastAPI application that predicts market prices for crops based on historical data. It utilizes a linear regression model trained on cleaned crop data.

## Project Structure

- `src/main.py`: Entry point of the FastAPI application.
- `src/models/predict.py`: Contains prediction logic and model-related functions.
- `src/data/cleaned_crop_data.csv`: Cleaned crop data used for training the model and making predictions.
- `requirements.txt`: Lists the dependencies required for the project.

## Requirements

To run this project, you need to install the following dependencies:

- FastAPI
- pandas
- numpy
- scikit-learn

You can install the dependencies using pip:

```
pip install -r requirements.txt
```

## Running the API

To run the FastAPI application, execute the following command:

```
uvicorn src.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Endpoints

- `GET /`: Returns a message indicating that the API is running.
- `POST /predict`: Accepts a request with the number of days ahead for prediction and returns the predicted prices.