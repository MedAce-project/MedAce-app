import streamlit as st

# Set page configuration
st.set_page_config(page_title="MedAce", layout="wide")

# Title and intro
st.title("🩺 MedAce - Smart Medical Report Analyzer")
st.write("Welcome! Upload your Medical Report to begin.")

# Create two columns
left_col, right_col = st.columns([1, 2])

# Left Column: File Upload
with left_col:
    st.header("📄 Upload Report")
    uploaded_file = st.file_uploader(
        "Choose a Medical Report",
        type=["pdf", "csv", "png", "jpg", "jpeg", "txt"],
        help="Upload your medical report here (PDF, Image, or Text). Max Size: 10MB"
    )
    if uploaded_file:
        st.success("✅ File Uploaded Successfully.")
        st.markdown(f"**Filename:** `{uploaded_file.name}`")

# Right Column: Display Report Analysis
with right_col:
    st.header("🧾 Report Summary")
    
    if uploaded_file:
        st.markdown("### 🩺 Extracted Report Details:")
        st.write("Sample content: Hemoglobin 11.2, WBC 8000, Platelets 2.3 lakh...")

        st.markdown("### 📊 Summary:")
        st.success("Overall, your results look normal. Slight anemia detected.")

        st.markdown("### ⚠️ Health Alerts:")
        st.warning("Hemoglobin is slightly below the normal range.")

        st.markdown("### 📈 Trends Over Time:")
        st.info("Once you upload more reports, we'll show your health trends here.")
    
    else:
        st.info("Analysis and visualizations will appear here once a file is uploaded.")
