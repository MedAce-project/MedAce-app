import streamlit as st
import PyPDF2
import pandas as pd
from PIL import Image
import io
import matplotlib.pyplot as plt
import seaborn as sns

# Page settings
st.set_page_config(page_title="MedAce", layout="wide")
st.title("🩺 MedAce - Smart Medical Report Analyzer")
st.write("Welcome! Upload your Medical Report to begin.")

# Two columns
left_col, right_col = st.columns([1, 2])

# ---- LEFT COLUMN: Upload ----
with left_col:
    st.header("Upload Report")
    uploaded_file = st.file_uploader(
        "Choose a Medical Report",
        type=["pdf", "csv", "png", "jpg", "jpeg", "txt"],
        help="Upload your medical report here (PDF, Image, or Text). Max Size: 10MB"
    )
    if uploaded_file:
        st.success("File Uploaded Successfully.")
        st.markdown(f"**Filename:** `{uploaded_file.name}`")

# ---- RIGHT COLUMN: Analysis ----
with right_col:
    st.header("Report Summary")

    if uploaded_file:
        st.markdown("Extracted Report Details:")
        st.write("Sample content: Hemoglobin 11.2, WBC 8000, Platelets 2.3 lakh...")

        st.markdown("Summary:")
        st.success("Overall, your results look normal. Slight anemia detected.")

        st.markdown("Health Alerts:")
        st.warning("Hemoglobin is slightly below the normal range.")

        st.markdown("Trends Over Time:")
        st.info("Once you upload more reports, we'll show your health trends here.")

        # 📥 Download Button
        st.markdown("Download Your Summary:")
        dummy_report = """
        MedAce - Health Report Summary
        ------------------------------
        ✅ Hemoglobin: 11.2 g/dL (Slightly low)
        ✅ WBC: 8000 /µL (Normal)
        ✅ Platelets: 2.3 lakh /µL (Normal)

        ⚠️ Note: Slight anemia detected.
        """
        buffer = io.StringIO(dummy_report)
        st.download_button(
            label="📄 Download Summary as .txt",
            data=buffer.getvalue(),
            file_name="medace_summary.txt",
            mime="text/plain"
        )
    else:
        st.info("Analysis and visualizations will appear here once a file is uploaded.")

# ---- File-Specific Display ----
if uploaded_file:
    file_name = uploaded_file.name.lower()

    # PDF files
    if file_name.endswith(".pdf"):
        with st.spinner("Extracting text from PDF..."):
            reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            st.success("Extraction complete!")

        with st.expander("Extracted Text from PDF"):
            st.write(text if text else "No readable text found.")

    # CSV files
    elif file_name.endswith(".csv"):
        try:
            df = pd.read_csv(uploaded_file)
            st.markdown("### 🧾 Report Table:")
            st.dataframe(df)

            if "age" in df.columns and "chol" in df.columns:
                # Scatter Plot
                st.markdown("### 📊 Cholesterol vs Age")
                fig1, ax1 = plt.subplots()
                sns.scatterplot(data=df, x="age", y="chol", hue="sex", palette="Set2", ax=ax1)
                ax1.set_title("Cholesterol Levels by Age")
                ax1.set_xlabel("Age")
                ax1.set_ylabel("Cholesterol (mg/dL)")
                st.pyplot(fig1)

                # Histogram
                st.markdown("### 📈 Cholesterol Distribution")
                fig2, ax2 = plt.subplots()
                sns.histplot(data=df, x="chol", bins=30, kde=True, color='skyblue', ax=ax2)
                ax2.axvline(240, color='red', linestyle='--', label='High Cholesterol (240 mg/dL)')
                ax2.set_title("Cholesterol Distribution in Patients")
                ax2.set_xlabel("Cholesterol (mg/dL)")
                ax2.set_ylabel("Number of Patients")
                ax2.legend()
                st.pyplot(fig2)
            else:
                st.warning("CSV does not contain expected columns like 'age' and 'chol'.")
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")

    # Text files
    elif file_name.endswith(".txt"):
        content = uploaded_file.read().decode("utf-8")
        st.markdown("### 📝 Text File Content:")
        st.text_area("Report Content", content, height=300)

    # Image files
    elif file_name.endswith((".png", ".jpg", ".jpeg")):
        image = Image.open(uploaded_file)
        st.markdown("### 🖼️ Uploaded Image:")
        st.image(image, caption=uploaded_file.name, use_column_width=True)

    else:
        st.warning("File uploaded, but could not read its content.")

# ---- Sidebar ----
with st.sidebar:
    st.title("MedAce")
    st.markdown("Navigation")
    st.page_link("https://medace-app-intrtjskaqsuzyedtqrcfh.streamlit.app/", label="Home", icon="🏠")
    st.button("Chat with MedAce (coming soon)")
    st.button("My Report History (coming soon)")
    st.divider()
    st.markdown("Need help? [Contact us](mailto:support@medace.ai)")


    