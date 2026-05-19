import streamlit as st
st.set_page_config(page_title="微型 TimeTree",layout="wide")
with st.sidebar:
  st.write("### 行事曆群組")
  st.radio("選擇群組",["業務","行政"])

