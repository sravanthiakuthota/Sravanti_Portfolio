import streamlit as st
import base64
import os

# Page Configuration
st.set_page_config(
    page_title="Sravanthi Akutota | Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Identity", "Resume", "Projects", "Contact"])

# --- Custom Styling ---
st.markdown("""
    <style>
        .title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #2E86C1;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #566573;
            margin-bottom: 20px;
        }
        .section {
            background-color: #FBFCFC;
            padding: 20px;
            border-radius: 12px;
        }
        .footer {
            text-align: center;
            font-size: 0.8rem;
            color: gray;
            margin-top: 4rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Identity Page ---
if page == "Identity":
    st.markdown('<div class="title">Sravanthi Akutota</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">M.S. in Learning Technologies | University of North Texas</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])
    with col1:
        if os.path.exists("profile.jpeg"):
            st.image("profile.jpeg", width=200, caption="Sravanthi Akutota")
        else:
            st.warning("'profile.jpeg' not found. Please add a professional headshot.")
    with col2:
        st.markdown("""
        <div class="section">
        I am passionate about integrating technology and education to create impactful learning experiences. 
        I am currently pursuing my master’s degree in Learning Technologies, with a background in Electrical 
        and Electronics Engineering. In my previous role at Google AdWords, I gained valuable experience in 
        content management and data analysis.
        </div>
        """, unsafe_allow_html=True)

# --- Resume Page ---
elif page == "Resume":
    st.subheader("My Resume")
    st.markdown("You can view the entire resume below and also download a copy.")

    resume_path = "resume.pdf"
    if os.path.exists(resume_path):
        with open(resume_path, "rb") as file:
            resume_data = file.read()
            st.download_button("Download Resume", data=resume_data, file_name="Sravanthi_Resume.pdf", mime="application/pdf")

            # Encode and embed PDF
            b64_pdf = base64.b64encode(resume_data).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{b64_pdf}" width="100%" height="700px" type="application/pdf"></iframe>'
            st.markdown("---")
            st.markdown("### Resume Preview:")
            st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.error("Error: 'resume.pdf' not found. Please add the file to the application folder.")

# --- Projects Page ---
elif page == "Projects":
    st.subheader("Featured Projects")

    st.markdown("### Reviewer Dashboard")
    st.write("Developed a dashboard to summarize the quality and turnaround time of ad reviews, improving internal workflows.")

    st.markdown("### Learning Insights")
    st.write("Created an interactive report using Power BI to track student performance and recommend personalized interventions.")

    st.markdown("### AI in Education")
    st.write("Investigated how AI tools can enhance learner engagement and deliver more personalized digital learning experiences.")

# --- Contact Page ---
elif page == "Contact":
    st.subheader("Contact Information")
    st.write("Feel free to reach out directly, or use the form below for inquiries.")

    st.markdown("**Email:** akutotasravanthi@gmail.com")
    st.markdown("**Phone:** 940-331-4160")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success(f"Thank you, {name}. Your message has been received.")

# --- Footer ---
st.markdown('<div class="footer">© 2025 Sravanthi Akutota • Portfolio created using Streamlit</div>', unsafe_allow_html=True)
