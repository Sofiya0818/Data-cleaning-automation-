import pandas as pd
import streamlit as st
from cleaning_pipeline import clean_data
st.set_page_config(page_title="Data Cleaning Automation",page_icon="🧹",layout="wide")
st.title("🧹 Data Cleaning Automation")
st.caption("Automated preprocessing and validation of messy CSV data")
up=st.file_uploader("Upload CSV",type=["csv"])
raw=pd.read_csv(up) if up else pd.read_csv("data/messy_customers.csv")
st.subheader("Input Data"); st.dataframe(raw.head(20),use_container_width=True)
a,b,c=st.columns(3); a.metric("Rows",len(raw)); b.metric("Columns",len(raw.columns)); c.metric("Missing Values",int(raw.isna().sum().sum()))
if st.button("Run Automated Cleaning",type="primary"):
    cleaned,report=clean_data(raw.copy()); st.success("Cleaning completed!")
    st.subheader("Cleaning Report"); st.dataframe(report,use_container_width=True)
    st.subheader("Cleaned Data"); st.dataframe(cleaned,use_container_width=True)
    st.download_button("⬇️ Download Cleaned CSV",cleaned.to_csv(index=False).encode(), "cleaned_data.csv","text/csv")
    st.subheader("Missing Values After Cleaning"); st.bar_chart(cleaned.isna().sum())
st.divider(); st.markdown("**Cleaning steps:** column standardization • whitespace removal • missing-value normalization • numeric conversion • age validation • email validation • date conversion • duplicate removal • median imputation • report generation")
