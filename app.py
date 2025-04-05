import streamlit as st
import os

# Page Configuration
st.set_page_config(
    page_title="Sravanthi Akutota | Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Identity", 
    "Resume", 
    "Scholarly Writing", 
    "Projects", 
    "Contact"
])

# --- Custom CSS (optional styling) ---
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


# --- 1. Identity Page ---
if page == "Identity":
    st.markdown('<div class="title">Sravanthi Akutota</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">M.S. in Learning Technologies | University of North Texas</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])
    with col1:
        # Show a headshot if found
        if os.path.exists("profile.jpeg"):
            st.image("profile.jpeg", width=200, caption="Sravanthi Akutota")
        else:
            st.warning("'profile.jpeg' not found. Please place a professional headshot in the same folder.")
    with col2:
        st.markdown("""
        <div class="section">
        I am passionate about integrating technology and education to create impactful learning experiences.
        I am currently pursuing my master’s degree in Learning Technologies, with a background in Electrical
        and Electronics Engineering. In my previous role at Google AdWords, I gained valuable experience in
        content management and data analysis.
        </div>
        """, unsafe_allow_html=True)


# --- 2. Resume Page ---
elif page == "Resume":
    st.subheader("My Resume")
    st.markdown("Below is a PNG preview, along with a PDF download option.")

    # Show resume as a PNG
    png_path = "resume.png"
    if os.path.exists(png_path):
        st.image(
            png_path,
            caption="Resume (PNG Preview)",
            width=600  # Adjust to your preference
        )
    else:
        st.error("Error: 'resume.png' not found. Please add the file to this folder.")

    st.markdown("---")

    # Provide PDF download if available
    pdf_path = "resume.pdf"
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as file:
            pdf_data = file.read()
        st.download_button(
            label="Download Resume (PDF)",
            data=pdf_data,
            file_name="Sravanthi_Resume.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("No PDF version available. Please add 'resume.pdf' to this folder if needed.")


# --- 3. Scholarly Writing Page ---
elif page == "Scholarly Writing":
    st.markdown("## Scholarly Writing")

    st.markdown("""
    **Introduction**  
    This section highlights my scholarly writing development within the Learning Technologies Master’s program. 
    It contains two examples of my academic work:
    - A research paper from LTEC 5300 (fulfilling the requirement from LTEC 5030 or LTEC 5300)
    - A 1500-word paper from LTEC 5610 (fulfilling the 1500-word paper requirement from LTEC 5610, 5400, or 5570)
    
    Each piece follows APA style guidelines and demonstrates my capacity to engage in critical analysis, 
    apply educational theory, and utilize evidence-based practice.
    """)

    # Example 1
    st.markdown("""
    ### Example 1: Research Paper (LTEC 5300)
    **Title:** Exploring Social Constructivism in Online Collaborative Environments  
    **Link to Full Paper:** [Insert Shared URL or File Here]  
    **Purpose:**  
    This paper critically examines Vygotsky’s social constructivist theory and its implications for designing 
    collaborative online activities. The analysis emphasizes how peer interaction, guided discussion boards, 
    and group problem-solving tasks enhance student engagement and learning outcomes.  

    **APA Formatting:** Used 7th edition standards throughout, including in-text citations and reference page.  

    **Why Included?**  
    - Demonstrates foundational understanding of learning theories and educational psychology in online settings.  
    - Highlights ability to conduct literature reviews, synthesize perspectives, 
      and propose practical strategies for online classroom design.
    """)

    # Example 2
    st.markdown("""
    ### Example 2: 1500-Word Paper (LTEC 5610)
    **Title:** Applying Cognitive Load Theory to Multimedia Instructional Design  
    **Link to Full Paper:** [Insert Shared URL or File Here]  
    **Purpose:**  
    This 1500-word paper investigates how Cognitive Load Theory (CLT) principles can optimize multimedia lesson plans. 
    It covers split-attention, signaling, and segmenting, demonstrating how instructors can systematically manage 
    cognitive load for diverse learner populations.

    **APA Formatting:** Complies with 7th edition guidelines, including title page, abstract, methodical headings, 
    and a comprehensive reference list.

    **Why Included?**  
    - Illustrates a more advanced, application-oriented approach to instructional design.  
    - Reflects progression from theoretical understanding to implementing research-driven solutions 
      in real-world contexts.
    """)

    # Holistic Reflection
    st.markdown("""
    ### Holistic Reflection (~500 Words)
    Over the course of my Learning Technologies Master’s program, these two scholarly works represent 
    significant milestones in my academic journey. In **LTEC 5300**, my focus was on understanding 
    foundational theories, particularly social constructivism, and exploring how collaborative activities 
    enhance online learning. Through this research, I learned the importance of structured peer interaction 
    and the role of theoretical alignment in developing rich learning environments.

    Later, in **LTEC 5610**, I applied those foundational insights to practical instructional design via 
    Cognitive Load Theory. This paper challenged me to translate theoretical principles into tangible design 
    choices, such as segmenting content and integrating visual cues. Crafting a 1500-word analysis forced me 
    to balance clarity with depth, ensuring the recommendations were evidence-based and relevant to various 
    learner demographics.

    Both experiences underscored the value of rigorous academic research, APA formatting, and iterative feedback. 
    My writing style evolved to be more structured and analytical, reflecting an increased emphasis on critique 
    and application. These two papers collectively highlight the trajectory from foundational theory to robust 
    instructional design practices, demonstrating both my scholarly growth and my readiness to contribute meaningfully 
    to the Learning Technologies field.
    """)

    st.markdown("""
    ### References
    (Each paper should maintain its own references in APA format. Below is a placeholder; update with actual sources.)

    - Vygotsky, L. (1978). *Mind in society: The development of higher psychological processes.* Harvard University Press.
    - Mayer, R. E. (2014). *Cognitive theory of multimedia learning.* Cambridge University Press.

    **Portfolio Placement**  
    - Provide direct links to each paper (Google Drive, OneDrive, or attached PDFs).  
    - Include this reflection text in the same section.  
    - Verify all APA formatting requirements are met.
    """)


# --- 4. Projects Page ---
elif page == "Projects":
    st.subheader("Featured Projects")

    st.markdown("### Reviewer Dashboard")
    st.write("Developed a dashboard to summarize the quality and turnaround time of ad reviews, improving internal workflows.")

    st.markdown("### Learning Insights")
    st.write("Created an interactive report using Power BI to track student performance and recommend personalized interventions.")

    st.markdown("### AI in Education")
    st.write("Investigated how AI tools can enhance learner engagement and deliver personalized digital learning experiences.")


# --- 5. Contact Page ---
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
