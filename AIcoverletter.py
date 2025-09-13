import google.generativeai as genai
import streamlit as st

# Configure API key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Load the Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# App title
st.title("💼✨ AI Cover Letter Generator")

st.write("Create a professional and personalized cover letter in seconds! 🚀")

# Input fields
job_title = st.text_input("📝 Enter the Job Title:")
resume_points = st.text_area("📌 Paste your resume highlights (skills, achievements, summary):")

# Generate cover letter only when button is clicked
if st.button("Submit"):
    if job_title.strip() == "" or resume_points.strip() == "":
        st.error("⚠️ Please provide both job title and resume highlights.")
    else:
        prompt = (
            f"Write a professional, polished, and engaging cover letter for the position of **{job_title}**. "
            f"Use the following resume points as background: {resume_points}. "
            f"Make it formal yet inspiring, with a confident tone."
        )

        # Generate content
        with st.spinner("⏳ Generating your cover letter..."):
            response = model.generate_content(prompt)

        # Display the result
        st.success("✅ Your AI-generated Cover Letter is ready!")
        st.markdown("---")
        st.markdown(f"### 📄 Cover Letter for **{job_title}**")
        st.write(response.text)
        st.balloons()




