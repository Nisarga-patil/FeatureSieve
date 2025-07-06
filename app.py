import streamlit as st
import pandas as pd
from feature_algo import featuresieve

st.set_page_config(page_title="FeatureSieve", layout="wide")

st.title("🧠 FeatureSieve – Graph-Based Feature Reduction")
st.markdown("Upload a CSV file with numeric data. We'll remove redundant features using correlation graphs.")

# Upload CSV
uploaded_file = st.file_uploader("📂 Upload your dataset (.csv)", type=["csv"])

# Parameters
tau = st.slider("🎯 Correlation threshold (tau)", 0.8, 0.99, 0.95, 0.01)
sample_size = st.number_input("🧪 Sample size", min_value=10, max_value=1000, value=100)

if uploaded_file:
    st.subheader("📄 Original Dataset Preview")
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    # Clean numeric only
    df = df.select_dtypes(include='number').dropna()
    st.info(f"🧮 Dataset shape after cleaning: {df.shape}")

    try:
        # Run FeatureSieve
        redundant = featuresieve(df, sample_size=sample_size, tau=tau)
        st.success(f"✅ Identified {len(redundant)} redundant features!")

        # Drop and show reduced
        reduced_df = df.drop(columns=redundant)
        st.write("📉 Reduced Dataset:", reduced_df.shape)
        st.dataframe(reduced_df.head())

        # Download button
        csv = reduced_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Reduced CSV", csv, "reduced_dataset.csv", "text/csv")

    except Exception as e:
        st.error(f"❌ Error: {e}")
