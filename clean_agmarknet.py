import pandas as pd

INPUT_CSV = "Agmarknet.csv"
OUTPUT_CSV = "cleaned_crop_data.csv"

# Load CSV
print(f"Loading dataset: {INPUT_CSV}")
df = pd.read_csv(INPUT_CSV, low_memory=False)

print(f"Initial shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# Rename columns
rename_map = {
    'Arrival_Date': 'date',
    'Modal_x0020_Price': 'price',
    'Min_x0020_Price': 'min_price',
    'Max_x0020_Price': 'max_price'
}
df = df.rename(columns=rename_map)

# Keep only necessary columns
df = df[['date', 'price']]  # now these exist after renaming

# Drop missing prices
df = df.dropna(subset=['price'])

# Save cleaned CSV
df.to_csv(OUTPUT_CSV, index=False)
print(f"Cleaned data saved to {OUTPUT_CSV}")
