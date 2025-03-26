import streamlit as st

# Page config
st.set_page_config(
    page_title="Sravanthi Akutota | Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar Navigation ---
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Identity", "📄 Resume", "💼 Projects", "📬 Contact"])

# --- Custom Styling ---
st.markdown("""
    <style>
        .title { font-size: 2.5rem; font-weight: bold; color: #2E86C1; }
        .subtitle { font-size: 1.2rem; color: #566573; margin-bottom: 20px; }
        .section { background-color: #FBFCFC; padding: 20px; border-radius: 12px; }
        .footer { text-align: center; font-size: 0.8rem; color: gray; margin-top: 4rem; }
    </style>
""", unsafe_allow_html=True)

# --- Identity Page ---
if page == "🏠 Identity":
    st.markdown('<div class="title">Sravanthi Akutota</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">M.S. in Learning Technologies | University of North Texas</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("profile.jpeg", width=200, caption="Sravanthi Akutota")
    with col2:
        st.markdown("""
        <div class="section">
        👋 I'm Sravanthi, passionate about blending **technology and education** to create impactful learning experiences.  
        🎓 Currently pursuing my Master’s in Learning Technologies, with a background in Electrical and Electronics Engineering.  
        🧠 Experienced in content management and data analysis from my work with Google AdWords.
        </div>
        """, unsafe_allow_html=True)

# --- Resume Page ---
elif page == "📄 Resume":
    st.subheader("📄 My Resume")
    st.markdown("You can view the full resume below and also download a copy.")

    try:
        with open("resume.pdf", "rb") as file:
            resume_data = file.read()
            st.download_button("⬇️ Download Resume", data=resume_data, file_name="Sravanthi_Resume.pdf", mime="application/pdf")
            st.markdown("---")
            st.markdown("### 📌 Preview:")
            st.pdf(resume_data)
    except FileNotFoundError:
        st.error("🚫 'resume.pdf' not found. Please upload it to the app folder.")

# --- Projects Page ---
elif page == "💼 Projects":
    st.subheader("💼 Featured Projects")

    st.markdown("### 🎯 Reviewer Dashboard")
    st.write("Built a dashboard summarizing ad review quality and turnaround time to improve internal workflows.")

    st.markdown("### 📊 Learning Insights")
    st.write("Used Power BI to build a student learning tracker dashboard that provides insights into performance.")

    st.markdown("### 🧠 AI in Education")
    st.write("Explored ChatGPT and other AI tools to enhance interactivity in digital learning modules.")

# --- Contact Page ---
elif page == "📬 Contact":
    st.subheader("📬 Let's Connect")
    st.write("You can reach me via the form below or email.")

    st.markdown("**Email:** akutotasravanthi@gmail.com")
    st.markdown("**Phone:** 940-331-4160")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        msg = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success(f"Thank you, {name}! Your message has been received.")

# --- Footer ---
st.markdown('<div class="footer">© 2025 Sravanthi Akutota • Built with 💙 using Streamlit</div>', unsafe_allow_html=True)
