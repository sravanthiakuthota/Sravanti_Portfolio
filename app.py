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
page = st.sidebar.radio("Go to", ["Identity", "Resume", "Scholarly Writing", "Projects", "Contact"])

# Custom CSS (optional styling)
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
        ul {
            margin-left: 1.5rem;
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
    st.markdown("Below is a PNG preview, along with a PDF download option.")

    # 1) Display the Resume as an Image (resume.png) at a smaller width
    png_path = "resume.png"
    if os.path.exists(png_path):
        st.image(
            png_path,
            caption="Resume (PNG Preview)",
            width=600  # Fixed smaller width for the image
        )
    else:
        st.error("Error: 'resume.png' not found. Please add the file to this folder.")

    st.markdown("---")

    # 2) Download Button for the PDF (resume.pdf)
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

# --- Scholarly Writing Page ---
elif page == "Scholarly Writing":
    st.markdown("## Scholarly Writing")
    
    st.markdown("""
    **Introduction**  
    This section highlights my scholarly writing development within the Learning Technologies Master’s program. 
    It contains two examples of my academic work:
    - A research paper from LTEC 5300 (meeting the requirement for a paper from LTEC 5030 or LTEC 5300)
    - A 1500-word paper from LTEC 5610 (meeting the requirement for a 1500-word paper from LTEC 5610, 5400, or 5570)
    
    All works are formatted according to APA style and demonstrate my capacity to engage in critical analysis, 
    application of educational theory, and evidence-based practice.
    """)
    
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
    - Demonstrates my foundational understanding of learning theories and educational psychology in an online setting.  
    - Highlights my ability to conduct a literature review, synthesize theoretical perspectives, 
      and propose practical strategies for online classroom design.
    """)
    
    st.markdown("""
    ### Example 2: 1500-Word Paper (LTEC 5610)
    **Title:** Applying Cognitive Load Theory to Multimedia Instructional Design  
    **Link to Full Paper:** [Insert Shared URL or File Here]  
    **Purpose:**  
    This 1500-word paper investigates how Cognitive Load Theory (CLT) principles can optimize multimedia lesson plans. 
    Topics covered include split-attention, signaling, and segmenting, demonstrating how instructors can systematically 
    manage cognitive load for diverse learner populations.  

    **APA Formatting:** Complies with 7th edition guidelines, including a title page, abstract, methodical headings, 
    and comprehensive reference list.  

    **Why Included?**  
    - Illustrates a more advanced, application-oriented approach to instructional design, bridging theory 
      with concrete e-learning strategies.  
    - Reflects my progression from theoretical understanding to implementing research-driven solutions 
      in real-world educational contexts.
    """)
    
    st.markdown("""
    ### Holistic Reflection (~500 Words)
    Throughout my time in the Learning Technologies Master’s program, these two pieces of scholarly writing 
    represent pivotal points in my academic journey. In **LTEC 5300**, I concentrated on foundational theories, 
    particularly social constructivism, which underscored the power of collaboration and social interaction 
    in virtual learning environments. This course pushed me to engage with primary research sources, refine 
    my writing style, and develop coherent arguments anchored in established educational frameworks. Drafting 
    the paper required iterative feedback from both peers and my instructor, which helped me learn how to 
    synthesize complex theories into a focused, well-supported narrative.

    Transitioning into more advanced coursework in **LTEC 5610**, I worked on a 1500-word paper examining 
    Cognitive Load Theory for multimedia course design. While my earlier research focused mainly on theory, 
    this paper demanded that I step into practical instructional design. I explored specific strategies 
    to minimize extraneous cognitive load, employing chunking and visual cues to streamline the learner’s experience. 
    This elevated my writing approach from analyzing theoretical perspectives to applying those perspectives 
    in real educational scenarios. It was especially enriching to test hypothetical course elements—like segmentation 
    techniques and interactive quizzes—and envision how they could be integrated effectively into an e-learning platform.

    Both papers taught me the value of rigorous research methods and strict adherence to APA guidelines. 
    From properly citing sources to maintaining a logical flow of arguments, these assignments reinforced 
    best practices for academic integrity and communication clarity. My professors and peers offered invaluable 
    feedback, pushing me to address potential knowledge gaps and refine my methodology.

    Overall, the transition from the early-stage social constructivism focus in LTEC 5300 to applying Cognitive Load 
    Theory in LTEC 5610 symbolizes my growth as a scholar who not only understands the why of instructional design 
    but also the how. This journey has strengthened my confidence in dissecting complex ideas and expressing them 
    in precise, persuasive language. Whether investigating a purely theoretical question or devising an e-learning 
    solution, I now approach scholarly work with a balance of conceptual depth, methodological rigor, and practical awareness. 
    These two papers, therefore, serve as milestones in my academic development—reflecting an ever-increasing commitment 
    to innovative, research-based solutions in the field of Learning Technologies.
    """)

    st.markdown("""
    ### References
    (Each paper should have its own dedicated reference list in APA format. Below are placeholders; 
    replace with actual references cited in your papers.)

    - Vygotsky, L. (1978). *Mind in society: The development of higher psychological processes.* Harvard University Press.
    - Mayer, R. E. (2014). *Cognitive theory of multimedia learning.* Cambridge University Press.

    **Portfolio Placement**  
    - Provide direct links to each paper (Google Drive, OneDrive, or attached PDFs).  
    - Include this reflection text.  
    - Verify all formatting meets APA style requirements.
    """)

# --- Projects Page ---
elif page == "Projects":
    st.subheader("Featured Projects")

    st.markdown("### Reviewer Dashboard")
    st.write("Developed a dashboard to summarize the quality and turnaround time of ad reviews, improving internal workflows.")

    st.markdown("### Learning Insights")
    st.write("Created an interactive report using Power BI to track student performance and recommend personalized interventions.")

    st.markdown("### AI in Education")
    st.write("Investigated how AI tools can enhance learner engagement and deliver personalized digital learning experiences.")

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
