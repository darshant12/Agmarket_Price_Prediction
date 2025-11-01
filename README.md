# Agricultural Market Price Prediction 🌾

A machine learning-based application that predicts agricultural commodity prices using historical market data.

## Features 🌟

- Price prediction based on market parameters
- User-friendly interface built with Streamlit
- Support for multiple agricultural commodities
- State and district-wise predictions
- Interactive input forms for market details

## Tech Stack 💻

- Python 3.8+
- Streamlit
- Scikit-learn
- Pandas
- Joblib

## Project Structure 📁

```
market-price-detection/
├── backend/
│   ├── app.py                 # Streamlit application
│   ├── cleaned_crop_data.csv  # Dataset
│   └── modal_price_model.pkl  # Trained model
├── requirements.txt
└── README.md
```

## Installation 🛠️

1. Clone the repository:
```bash
git clone https://github.com/yourusername/market-price-detection.git
cd market-price-detection
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage 🚀

1. Start the Streamlit app:
```bash
cd backend
streamlit run app.py
```

2. Open your browser and go to `http://localhost:8501`

3. Enter market details:
   - State and District
   - Market information
   - Commodity details
   - Price ranges
   - Date information

4. Click "Predict Price" to get the estimated modal price

// ...existing code...

## Sample Input Example 📊

Here's an example of input values and their predicted output:

```
Input Parameters:
---------------
State: Maharashtra
District: Pune
Market: Local Market
Commodity: Rice
Variety: Grade A
Grade: Premium

Price Details:
-------------
Minimum Price: ₹1,200
Maximum Price: ₹2,400
Date: 15/10/2025

Output:
-------
Predicted Modal Price: ₹1,800
```

Note: These values are based on actual market data from our database. Results may vary based on current market conditions and seasonal factors.

// ...existing code...

## Model Training 🤖

The prediction model is trained on historical agricultural market data, considering factors like:
- Minimum and maximum prices
- Seasonal variations
- Geographic location
- Commodity type and grade

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📝

This project is licensed under the MIT License 
