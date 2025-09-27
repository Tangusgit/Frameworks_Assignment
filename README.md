# CORD-19 Data Explorer

A simple data analysis and interactive web app built with **Python, Pandas, Matplotlib, Seaborn, and Streamlit**.
This project explores the [CORD-19 research dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge), focusing on COVID-19 research papers metadata.

---

## 📌 Features

* Load and clean the **metadata.csv** dataset
* Handle missing values and prepare data for analysis
* Analyze publication trends over time
* Identify top journals publishing COVID-19 research
* Generate simple visualizations (bar charts, line plots, word clouds)
* Interactive **Streamlit app** to explore the dataset

---

## 🛠️ Technologies Used

* Python 3.7+
* Pandas (data manipulation)
* Matplotlib & Seaborn (visualization)
* Streamlit (web application)

---

## 📂 Project Structure

```
Frameworks_Assignment/
│
├── data/
│   ├── metadata.csv            # Original dataset (large)
│   ├── metadata_sample.csv     # Smaller sample dataset (used in app)
│
├── venv/                       # Virtual environment
├── make_sample.py              # Script to create sample dataset
├── app.py                      # Streamlit app
├── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Frameworks_Assignment.git
cd Frameworks_Assignment
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

* Windows:

  ```bash
  .\venv\Scripts\activate
  ```
* Mac/Linux:

  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

*(If you don’t have `requirements.txt`, install manually:)*

```bash
pip install pandas matplotlib seaborn streamlit
```

### 5. Prepare the Dataset

* Place `metadata.csv` into the `data/` folder.
* Run the script to create a smaller dataset:

  ```bash
  python make_sample.py
  ```

### 6. Run the App

```bash
streamlit run app.py
```

---

## 📊 Example Outputs

* Publications by Year (bar chart)
* Top Journals publishing COVID-19 research
* Word cloud of paper titles
* Data preview table

---

## 📖 Learning Objectives

By completing this project, you will:

* Practice **loading and cleaning real-world data**
* Build **visualizations** with Pandas/Matplotlib/Seaborn
* Create an **interactive app** using Streamlit
* Document and share your work with GitHub

---

## ✅ Evaluation Criteria

* **Complete Implementation (40%)**: All tasks completed
* **Code Quality (30%)**: Readable, well-commented code
* **Visualizations (20%)**: Clear, appropriate charts
* **Streamlit App (10%)**: Functional and interactive

---

## 📌 Author

* Kipkoech Seth Tangus
* Project for **Frameworks Assignment**
