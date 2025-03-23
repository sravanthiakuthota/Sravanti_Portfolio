import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Sravanthi Akutota | Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom Styles ---
st.markdown("""
    <style>
        .title {
            font-size: 3rem;
            font-weight: 800;
            color: #2E86C1;
        }
        .subtitle {
            font-size: 1.5rem;
            color: #5D6D7E;
        }
        .section {
            background-color: #FDFEFE;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 2rem;
        }
        .footer {
            text-align: center;
            font-size: 0.9rem;
            color: #7B7D7D;
            margin-top: 4rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="title">🌟 Sravanthi Akutota</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Learning Technologies | UNT | Denton, TX</div>', unsafe_allow_html=True)

# --- Basic Info ---
col1, col2 = st.columns([1, 3])

with col1:
    st.image("profile.jpeg", width=200, caption="Hi, I’m Sravanthi!")

with col2:
    st.markdown("""
    <div class="section">
    👋 I'm currently pursuing my Master’s in Learning Technologies at the University of North Texas, with a background in Electrical and Electronics Engineering.

    🔍 I have hands-on experience in **content management** and **data analysis** from my role at Google AdWords, where I evaluated patterns, maintained content quality, and supported cross-functional teams.

    💬 I'm passionate about tech-driven learning solutions and creating impactful digital content.

    📍 Denton, TX | 📧 akutotasravanthi@gmail.com | 📞 940-331-4160
    </div>
    """, unsafe_allow_html=True)

# --- Tabs for Resume, Projects, Contact ---
st.markdown("## 📁 Explore My Portfolio")
tab1, tab2, tab3 = st.tabs(["📄 Resume", "💼 Projects", "📬 Contact"])

# --- TAB 1: Resume ---
with tab1:
    st.subheader("📄 Professional Summary")

    st.markdown("""
    **Summary:**  
    Proven expertise in content management and data analysis, honed at Google AdWords. Skilled in identifying trends, improving accuracy, and streamlining processes through teamwork and effective communication.
    
    ---
    **Skills:**  
    - IT Network Analysis  
    - Core Java  
    - Content Management
    
    ---
    **Experience:**  
    **Associate Reviewer - Content Management | Google AdWords (May 2021 – Jun 2023)**  
    - Reviewed websites and created ads  
    - Checked content for quality and accuracy  
    - Analyzed data and identified trends  
    - Prepared weekly reports and handled team communications  
    - Handled shifts, issues, and escalations

    ---
    **Education:**  
    - M.S. in Learning Technologies, University of North Texas – *Expected May 2025*  
    - B.Tech in Electrical & Electronics Engineering, JNTUH – *CGPA: 7.5*  
    - Intermediate (MPC), Narayana Junior College – *Marks: 849*  
    - SSC, Excellent Grammar High School – *CGPA: 8.8*

    ---
    **Training:**  
    - 15-day Internship at Power Grid, KTPS
    """)

# --- TAB 2: Projects ---
with tab2:
    st.subheader("💼 Projects")

    st.markdown("### 🎯 eLearning Content Reviewer Dashboard")
    st.write("Built a dashboard to summarize and track ad review patterns, helping improve decision-making speed for content teams.")

    st.markdown("### 📊 Student Learning Insights")
    st.write("Developed an interactive report using Power BI to track learning progress and recommend personalized interventions.")

    st.markdown("### 🧠 AI & Learning Technologies")
    st.write("Explored how AI tools like ChatGPT can enhance learner engagement and feedback in digital education platforms.")

# --- TAB 3: Contact ---
with tab3:
    st.subheader("📬 Contact Me")

    st.write("I’d love to connect! Use the form below or email me directly at akutotasravanthi@gmail.com.")

    contact_form = st.form(key="contact_form")
    name = contact_form.text_input("Your Name")
    message = contact_form.text_area("Your Message")
    send = contact_form.form_submit_button("Send")

    if send:
        st.success(f"Thanks, {name}! Your message has been received. I’ll get back to you soon.")

# --- Footer ---
st.markdown('<div class="footer">© 2025 Sravanthi Akutota • Portfolio built with 💙 using Streamlit</div>', unsafe_allow_html=True)
