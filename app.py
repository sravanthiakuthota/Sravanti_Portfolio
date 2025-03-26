import streamlit as st

# Page config
st.set_page_config(page_title="Sravanthi Akutota Portfolio", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Identity", "📄 Resume", "💼 Projects", "📬 Contact"])

# Common styling
st.markdown("""
    <style>
        .title { font-size: 2.5rem; font-weight: bold; color: #2E86C1; }
        .subtitle { font-size: 1.2rem; color: #566573; margin-bottom: 20px; }
        .section { background-color: #FBFCFC; padding: 20px; border-radius: 12px; }
        .footer { text-align: center; font-size: 0.8rem; color: gray; margin-top: 4rem; }
    </style>
""", unsafe_allow_html=True)

# Page Content Based on Selection
if page == "🏠 Identity":
    st.markdown('<div class="title">Sravanthi Akutota</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">M.S. in Learning Technologies | University of North Texas</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("profile.jpg", width=200, caption="Sravanthi Akutota")
    with col2:
        st.markdown("""
        <div class="section">
        👋 I'm Sravanthi, passionate about blending **technology and education** to create impactful learning experiences.  
        🎓 Final semester grad student in Learning Technologies, with a strong foundation in Electrical and Electronics Engineering.  
        </div>
        """, unsafe_allow_html=True)

elif page == "📄 Resume":
    st.subheader("📄 My Resume")
    st.markdown("""
    - **Content Reviewer at Google AdWords (2021–2023)**
    - Skilled in content quality analysis, reporting, and trend evaluation.
    - Proficient in IT Network Analysis and Core Java.
    - M.S. in Learning Technologies (2025), B.Tech in EEE.
    """)

    st.markdown("---")
    with open("resume.pdf", "rb") as file:
        st.download_button("⬇️ Download Resume", file, "Sravanthi_Resume.pdf", "application/pdf")

elif page == "💼 Projects":
    st.subheader("💼 Featured Projects")

    st.markdown("### 🎯 Reviewer Dashboard")
    st.write("Built a dashboard summarizing ad review quality and turnaround time to improve internal workflows.")

    st.markdown("### 📊 Learning Insights")
    st.write("Used Power BI to build a student learning tracker dashboard that provides insights into performance.")

    st.markdown("### 🧠 AI in Education")
    st.write("Explored ChatGPT and other AI tools to enhance interactivity in digital learning modules.")

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

# Footer
st.markdown('<div class="footer">© 2025 Sravanthi Akutota • Built with 💙 using Streamlit</div>', unsafe_allow_html=True)
