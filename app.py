import streamlit as st
st.set_page_config(page_title="MedAce",layout ="wide")
st.title("🩺MedAce - Smart Medical Report Analyzer")
st.write("Welcome! Upload your Medical Report to begin")
left_col, right_col = st.columns([1,2])
with left_col:
    st.header("Upload Report")
    uploaded_file = st.file_uploader("Choose a Medical Report",type=["pdf", "csv"])
    if uploaded_file:
        st.success("File Uploaded Successfully")
with right_col:
    st.header("Report Summary")
    st.info("Analysis and visualizations will appear here soon")