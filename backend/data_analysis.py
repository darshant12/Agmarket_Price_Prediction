# Creating a self-contained demonstration: read the small sample dataset (from the user's message),
# preprocess categorical and date features, train a RandomForestRegressor to predict Modal Price,
# evaluate with a time-aware split (if possible) and a normal train/test split for this tiny demo,
# show results and save the trained model to a file the user can download.
#
# This code will run here and show outputs (table + metrics + feature importances).
# If you want, I can expand this into a full Jupyter notebook or a Flask/FastAPI app for production.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, TimeSeriesSplit, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# Create DataFrame from the sample rows you provided
df = pd.read_csv("Agmarknet.csv")

# Quick display of the dataset
df['Arrival_Date'] = pd.to_datetime(df['Arrival_Date'], dayfirst=True, errors='coerce')

# Basic feature engineering
df['day'] = df['Arrival_Date'].dt.day
df['month'] = df['Arrival_Date'].dt.month
df['year'] = df['Arrival_Date'].dt.year
# Price spread as a useful numeric feature
df['price_spread'] = df['Max_x0020_Price'] - df['Min_x0020_Price']

# Target and features
target = "Modal_x0020_Price"
numeric_features = ['Min_x0020_Price', 'Max_x0020_Price', 'price_spread', 'day', 'month', 'year']
categorical_features = ['State', 'District', 'Market', 'Commodity', 'Variety', 'Grade']

X = df[numeric_features + categorical_features]
y = df[target]

# Preprocessing pipelines
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# For categories we use OrdinalEncoder here for compactness (works for tree models).
# In a larger dataset you'd prefer Target Encoding or OneHot depending on cardinality.
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output = False))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
], remainder='drop', sparse_threshold=0)

# Full pipeline with a RandomForestRegressor
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(random_state=42, n_estimators=200))
])

# Because this demo dataset is tiny, we'll still run a simple train/test split.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Fit model
model.fit(X_train, y_train)

# Predict & evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

print(f"Rows in dataset: {len(df)}")
print(f"Train rows: {len(X_train)}, Test rows: {len(X_test)}")
print(f"R^2 score: {r2:.3f}")

# Feature importance: retrieve feature names after preprocessing
# Get numeric feature names
num_names = numeric_features
# Get onehot feature names from the onehot encoder
ohe = model.named_steps['preprocessor'].named_transformers_['cat'].named_steps['onehot']
ohe_feature_names = list(ohe.get_feature_names_out(categorical_features))
feature_names = num_names + ohe_feature_names

# Get importances from the RandomForest inside the pipeline
importances = model.named_steps['regressor'].feature_importances_
feat_imp_df = pd.DataFrame({'feature': feature_names, 'importance': importances}).sort_values('importance', ascending=False)

print("Feature importances", feat_imp_df.head(30))

# Save model for later use
model_path = "./modal_price_model.pkl"
joblib.dump(model, model_path)
print(f"Trained model saved to: {model_path}")
