# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os, re
from collections import Counter

st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")
st.title("CORD-19 Data Explorer")
st.write("Explore metadata from CORD-19 research papers")

@st.cache_data
def load_data():
    # prefer cleaned file, then full, then sample
    if os.path.exists("data/metadata_cleaned.csv"):
        return pd.read_csv("data/metadata_cleaned.csv", low_memory=False)
    if os.path.exists("data/metadata.csv"):
        return pd.read_csv("data/metadata.csv", low_memory=False)
    if os.path.exists("data/metadata_sample.csv"):
        return pd.read_csv("data/metadata_sample.csv", low_memory=False)
    return pd.DataFrame()

df = load_data()

if df.empty:
    st.error("No data found. Put metadata.csv or metadata_sample.csv into the data/ folder.")
    st.stop()

# Ensure columns exist
df.columns = [c.strip() for c in df.columns]
df['title'] = df.get('title', '').fillna('').astype(str)
df['abstract'] = df.get('abstract', '').fillna('').astype(str)
df['journal'] = df.get('journal', '').fillna('Unknown')
df['publish_time'] = pd.to_datetime(df.get('publish_time'), errors='coerce')
df['year'] = df['publish_time'].dt.year

# Sidebar filters
st.sidebar.header("Filters")
years = sorted(df['year'].dropna().unique().astype(int).tolist()) if 'year' in df.columns else []
if years:
    min_y, max_y = min(years), max(years)
    year_range = st.sidebar.slider("Publication year range", min_y, max_y, (min_y, max_y))
    df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

journal_options = df['journal'].value_counts().index.tolist()
selected = st.sidebar.multiselect("Filter by journal", options=journal_options, default=None)
if selected:
    df = df[df['journal'].isin(selected)]

# Key metrics
col1, col2, col3 = st.columns(3)
col1.metric("Papers (filtered)", len(df))
col2.metric("Unique journals", df['journal'].nunique())
col3.metric("Years covered", f"{int(df['year'].min()) if df['year'].notna().any() else 'N/A'} - {int(df['year'].max()) if df['year'].notna().any() else 'N/A'}")

# Publications by year
st.subheader("Publications by Year")
if df['year'].notna().any():
    year_counts = df['year'].value_counts().sort_index()
    fig, ax = plt.subplots()
    ax.plot(year_counts.index, year_counts.values, marker='o')
    ax.set_xlabel('Year'); ax.set_ylabel('Count')
    st.pyplot(fig)
else:
    st.write("No year data available.")

# Top journals
st.subheader("Top Journals")
top_j = df['journal'].value_counts().head(15)
fig, ax = plt.subplots(figsize=(8,4))
top_j.plot(kind='bar', ax=ax)
ax.set_ylabel('Count')
st.pyplot(fig)

# Top title words
st.subheader("Top words in titles")
def top_n_words(series, n=20):
    text = ' '.join(series.dropna().astype(str)).lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    stopwords = set(['the','and','for','with','from','that','this','study','on','in','of','to','a','an','by','using','covid','sars','coronavirus'])
    words = [w for w in text.split() if w not in stopwords and len(w) > 2]
    return Counter(words).most_common(n)

top_words = top_n_words(df['title'], 20)
if top_words:
    words, counts = zip(*top_words)
    fig, ax = plt.subplots(figsize=(8,4))
    ax.barh(list(words)[::-1], list(counts)[::-1])
    st.pyplot(fig)
else:
    st.write("No title data available.")

# Sample data table
st.subheader("Sample data")
cols = [c for c in ['title','authors','journal','publish_time'] if c in df.columns]
st.dataframe(df[cols].head(50))

# Allow download of filtered data
csv = df.to_csv(index=False)
st.download_button("Download filtered CSV", csv, file_name="filtered_metadata.csv", mime="text/csv")
