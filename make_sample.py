# make_sample.py
import pandas as pd

# This script reads data/metadata.csv and writes a small sample
# so you can work quickly during development.
try:
    df = pd.read_csv("data/metadata.csv", low_memory=False)
except FileNotFoundError:
    print("ERROR: data/metadata.csv not found. Put metadata.csv in the data/ folder.")
    raise

df.head(2000).to_csv("data/metadata_sample.csv", index=False)
print("Saved data/metadata_sample.csv (2000 rows)")
