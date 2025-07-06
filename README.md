# 🧠 FeatureSieve  
> Like a sieve filters unwanted parts, this filters redundant features.

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-FeatureSieve-green?logo=streamlit)](https://featuresieve-21.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

![FeatureSieve Banner](https://github.com/user-attachments/assets/e4b39edf-bc2d-480e-9b17-c2cc004f4fea)

---

## 🌟 Overview

**FeatureSieve** is an ultra-fast tool to reduce the number of features (columns) in large datasets while preserving their information quality.  
It identifies *clusters of linearly related (i.e., redundant)* features and keeps only the most representative one from each cluster.

No ML model retraining needed. Just pure, effective feature pruning.

---

## 🎯 Why FeatureSieve?

- 🚀 Handles large datasets efficiently
- 🧩 Identifies and removes *redundant* (not useless) features
- 📉 Reduces dimensionality without compromising data essence
- ✅ Plug-and-play: No training or labeling required

---

## 🔗 Try it Live

👉 [**Click here to launch FeatureSieve on Streamlit**](https://featuresieve-21.streamlit.app)

---

## 📦 Installation

Install the required Python dependencies using `pip`:

```bash
pip install pandas numpy networkx
##📚 Usage
#🔁 Step-by-step
Clone or download featureseive.py

Import it in your project

Call it with a pandas DataFrame

##🧪 Example
import pandas as pd
from featureseive import featureseive

# Load your large dataset
df = pd.read_csv('really_huge_dataset.csv')

# Get list of redundant features
redundant = featureseive(df)

# Drop them to get a leaner dataset
clean_df = df.drop(columns=redundant)

print("Redundant features removed:", redundant)

##🔍 How It Works
Computes correlation matrix of features

Builds a similarity graph of highly correlated features

Uses graph clustering to find groups of redundant features

Selects one representative feature from each group based on proximity to others

##🛠 Tech Stack
Python

Pandas – Data manipulation

NumPy – Numerical operations

NetworkX – Graph-based feature grouping

Streamlit – Live app frontend

##💡 Ideal For
Data preprocessing pipelines

Feature selection in AutoML workflows

Dimensionality reduction before clustering/classification

Cleaning large CSVs with high feature overlap

#🙋 Contact
For support, questions, or collaborations:
📧 pnisarga7@gmail.com

#📄 License
This project is licensed under the MIT License.

#🌱 Contribute
Feel free to fork, star ⭐, and submit issues or pull requests. Contributions are welcome!
