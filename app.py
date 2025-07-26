import streamlit as st
st.set_page_config(page_title="MedAce",layout ="wide")
st.title("🩺MedAce - Smart Medical Report Analyzer")
st.write("Welcome! Upload your Medical Report to begin")
left_col, right_col = st.columns([1,2])
with left_col:
    st.header("Upload Report")
    uploaded_file = st.file_uploader("Choose a Medical Report",type=["pdf", "csv", "png", "jpg", "jpeg", "txt"]
    help = "upload your medical report here (PDF, Image, or Text). Max Size: 10MB")
    if uploaded_file:
        st.success("File Uploaded Successfully.")
        st.markdown(f"**Filename:**`{Uploaded_file.name}`")
with right_col:
    st.header("Report Summary")
    if uploaded_file:
        st.markdown("### Extracted Report Details:")
        st.write("Sample content: Hemoglobin 11.2, WBC 8000, platelets 2.3 lakh...")

        st.markdown("### Summary:")
        st.write("Overall, your results look normal. Slight anemia detected.")

        st.markdown("Health Alerts:!!")
        st.write("Hemoglobin is slightly below the normal range.")

        st.markdown("Trends Over Time:")
        st.write("Once you upload more reports, we'll show your health trends here")
    st.info("Analysis and visualizations will appear here once a file is uploaded")