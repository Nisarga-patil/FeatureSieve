# 🧠 FeatureSieve  
> Like a sieve filters unwanted parts, this filters redundant features.

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-FeatureSieve-green?logo=streamlit)](https://featuresieve-21.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📦 Installation

Install the required Python dependencies using `pip`:

pip install pandas numpy networkx


## 📚 Usage

### 🔁 Step-by-step

1. Clone or download `featureseive.py`
2. Import it in your project
3. Call it with a pandas DataFrame

---

### 🧪 Example

```python
import pandas as pd
from featureseive import featureseive

# Load your large dataset
df = pd.read_csv('really_huge_dataset.csv')

# Get list of redundant features
redundant = featureseive(df)

# Drop them to get a leaner dataset
clean_df = df.drop(columns=redundant)

print("Redundant features removed:", redundant)
