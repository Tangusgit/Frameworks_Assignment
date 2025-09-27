# cleaning_and_prep.py
import pandas as pd
import os

# Try to load full CSV, otherwise load sample
if os.path.exists("data/metadata.csv"):
    df = pd.read_csv("data/metadata.csv", low_memory=False)
elif os.path.exists("data/metadata_sample.csv"):
    df = pd.read_csv("data/metadata_sample.csv", low_memory=False)
else:
    raise FileNotFoundError("No metadata.csv or metadata_sample.csv found in data/")

# Normalize column names
df.columns = [c.strip() for c in df.columns]

# Fill / normalize important columns
df['title'] = df.get('title', '').fillna('').astype(str)
df['abstract'] = df.get('abstract', '').fillna('').astype(str)
df['journal'] = df.get('journal', '').fillna('Unknown')

# Parse publish_time to datetime, create year
df['publish_time'] = pd.to_datetime(df.get('publish_time'), errors='coerce')
df['year'] = df['publish_time'].dt.year

# Abstract word count
df['abstract_word_count'] = df['abstract'].str.split().apply(lambda x: len(x) if isinstance(x, list) else 0)

# Save cleaned file
df.to_csv("data/metadata_cleaned.csv", index=False)
print("Saved data/metadata_cleaned.csv")
print("Rows:", len(df), "Columns:", len(df.columns))
