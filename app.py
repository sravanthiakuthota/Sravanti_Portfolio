import streamlit as st
import os
from datetime import date

# ──────────────────────────────────────────────────────────
# Page Configuration
# ──────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Sravanthi Akutota | Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ──────────────────────────────────────────────────────────
# Sidebar Navigation
# ──────────────────────────────────────────────────────────
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Identity", "Resume", "Projects", "Contact", "Scholarly Writing", "Cover Letter"]
)

# ── Custom CSS ────────────────────────────────────────────
st.markdown(
    """
    <style>
        /* Dark‑blue page background */
        body { background-color:#0d1b2a; }

        /* Primary title styling */
        .title {
            font-size:2.5rem;
            font-weight:700;
            color:#4da8ff;          /* light blue for contrast */
        }

        /* Subtitle styling */
        .subtitle {
            font-size:1.2rem;
            color:#c9d6ff;          /* soft light text */
            margin-bottom:20px;
        }

        /* Card / content panel */
        .section {
            background:#f7f9fc;     /* very light panel for readability */
            padding:20px;
            border-radius:12px;
        }

        /* Footer */
        .footer {
            text-align:center;
            font-size:0.8rem;
            color:#c9d6ff;
            margin-top:4rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ──────────────────────────────────────────────────────────
# Identity Page
# ──────────────────────────────────────────────────────────
if page == "Identity":
    st.markdown('<div class="title">Sravanthi Akutota</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">M.S. in Learning Technologies | University of North Texas</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 3])
    with col1:
        if os.path.exists("profile.jpeg"):
            st.image("profile.jpeg", width=200, caption="Sravanthi Akutota")
        else:
            st.warning("profile.jpeg not found. Please add a professional headshot.")
    with col2:
        st.markdown(
            """
            <div class="section">
            I am passionate about integrating technology and education to create impactful learning
            experiences. Currently, I am completing my master’s degree in Learning Technologies, building on
            a B.Tech in Electrical & Electronics Engineering. My professional background at Google AdWords
            refined my skills in content quality analysis, data‑driven decision‑making, and collaborative
            leadership.
            </div>
            """,
            unsafe_allow_html=True,
        )

# ──────────────────────────────────────────────────────────
# Resume Page
# ──────────────────────────────────────────────────────────
if page == "Resume":
    st.subheader("My Resume")
    st.markdown("Below is a PNG preview, along with a PDF download option.")

    if os.path.exists("resume.png"):
        st.image("resume.png", caption="Resume (PNG Preview)", width=600)
    else:
        st.error("resume.png not found. Please add the file to this folder.")

    st.markdown("---")

    if os.path.exists("resume.pdf"):
        with open("resume.pdf", "rb") as f:
            st.download_button(
                "Download Resume (PDF)",
                f.read(),
                file_name="Sravanthi_Resume.pdf",
                mime="application/pdf",
            )
    else:
        st.warning("No resume.pdf found. Add it to enable download.")

# ──────────────────────────────────────────────────────────
# Projects Page
# ──────────────────────────────────────────────────────────
if page == "Projects":
    st.subheader("Featured Projects")

    st.markdown("### Reviewer Dashboard")
    st.write(
        "Designed a dashboard that summarizes ad‑review quality and turnaround time, improving internal workflows."
    )

    st.markdown("### Learning Insights")
    st.write(
        "Built an interactive Power BI report to track student performance and recommend personalized interventions."
    )

    st.markdown("### AI in Education")
    st.write(
        "Explored AI tools to enhance learner engagement and deliver data‑driven e‑learning experiences."
    )

# ──────────────────────────────────────────────────────────
# Contact Page
# ──────────────────────────────────────────────────────────
if page == "Contact":
    st.subheader("Contact Information")
    st.write("Feel free to reach out directly, or use the form below for inquiries.")

    st.markdown("**Email:** akutotasravanthi@gmail.com")
    st.markdown("**Phone:** 940‑331‑4160")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        message = st.text_area("Your Message")
        if st.form_submit_button("Send"):
            st.success(f"Thank you, {name}. Your message has been received.")

# ──────────────────────────────────────────────────────────
# Scholarly Writing Page
# ──────────────────────────────────────────────────────────
if page == "Scholarly Writing":
    st.subheader("Scholarly Writing")
    # (content omitted for brevity; keep existing text from previous version)

# ──────────────────────────────────────────────────────────
# Cover Letter Page
# ──────────────────────────────────────────────────────────
if page == "Cover Letter":
    st.subheader("Cover Letter")

    today = date.today().strftime("%B %d, %Y")

    cover_letter = f"""
{today}

Sravanthi Akutota  
Denton, TX 76201  
(940) 331‑4160  
akutotasravanthi@gmail.com  

Hiring Manager  
[Company Name]  
[Company Address]  

Dear Hiring Manager,

I am writing to express my enthusiasm for the **[Instructional Technology / Learning Experience Designer]** position at **[Company Name]**. As a graduate student completing a Master of Science in Learning Technologies at the University of North Texas (May 2025) and a former Associate Reviewer with Google AdWords, I bring a unique blend of instructional design expertise, data‑driven content management, and collaborative leadership.

At Google AdWords, I evaluated large‑scale web content for quality and compliance, led trend analyses, and produced weekly process reports that improved turnaround efficiency by 15 percent. My ability to translate complex data into actionable insights directly aligns with your organization’s goal of creating evidence‑based learning solutions. In addition, my background in IT Network Analysis and Core Java enables me to communicate effectively with technical teams while maintaining a learner‑centered perspective.

In my graduate studies, I have focused on applying Cognitive Load Theory and social‑constructivist principles to multimedia learning environments. Recent projects include developing five eLearning modules in Canvas LMS that supported more than 300 online students and producing instructional media to boost engagement across social platforms. These experiences demonstrate my commitment to leveraging technology, analytics, and creative design to craft high‑quality, inclusive learning experiences.

My professional goals are to (1) design data‑driven instructional solutions that improve learner performance, (2) foster cross‑functional collaboration to ensure scalable content quality, and (3) champion continuous improvement through analytics and user feedback. Your organization’s emphasis on innovative learning technologies resonates strongly with these goals.

Please review my attached résumé and online portfolio for additional details and sample work. I welcome the opportunity to discuss how my background in content analysis, instructional design, and project management can contribute to **[Company Name]**. Thank you for your time and consideration.

Sincerely,

Sravanthi Akutota  
University of North Texas | M.S. Learning Technologies (May 2025)
"""

    st.markdown(
        f"<div class='section' style='white-space: pre-wrap;'>{cover_letter}</div>",
        unsafe_allow_html=True,
    )

    # Optional download of the cover letter as a .txt file
    st.download_button(
        "Download Cover Letter (TXT)",
        cover_letter,
        file_name="Sravanthi_Akutota_Cover_Letter.txt",
    )

# ---------------------------
#       Scholarly Writing
# ---------------------------
if page == "Scholarly Writing":
    st.subheader("Scholarly Writing")

    st.markdown("""
    ### Introduction
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

    **Purpose:**  
    This paper critically examines Vygotsky’s social constructivist theory and its implications for 
    designing collaborative online activities. The analysis emphasizes how peer interaction, guided 
    discussion boards, and group problem-solving tasks enhance student engagement and learning outcomes.

    **APA Formatting:** Used 7th edition standards throughout, including in-text citations and reference page.

    **Why Included?**  
    - Demonstrates my foundational understanding of learning theories and educational psychology in an 
      online setting.  
    - Highlights my ability to conduct a literature review, synthesize theoretical perspectives, and 
      propose practical strategies for online classroom design.
    """)

    st.markdown("""
    ### Example 2: 1500-Word Paper (LTEC 5610)
    **Title:** Applying Cognitive Load Theory to Multimedia Instructional Design  

    **Purpose:**  
    This 1500-word paper investigates how Cognitive Load Theory (CLT) principles can optimize multimedia 
    lesson plans. Topics covered include split-attention, signaling, and segmenting, demonstrating how 
    instructors can systematically manage cognitive load for diverse learner populations.

    **APA Formatting:** Complies with 7th edition guidelines, including a title page, abstract, methodical 
    headings, and comprehensive reference list.

    **Why Included?**  
    - Illustrates a more advanced, application-oriented approach to instructional design, bridging theory 
      with concrete e-learning strategies.  
    - Reflects my progression from theoretical understanding to implementing research-driven solutions in 
      real-world educational contexts.
    """)

    st.markdown("""
    ### Holistic Reflection
    Over the course of my Learning Technologies master’s program, my approach to scholarly writing has 
    evolved significantly, moving from purely theoretical analyses to research-informed instructional 
    applications. In LTEC 5300, I began by examining fundamental educational theories, particularly social 
    constructivism, and learned how to frame arguments around established theoretical frameworks. This 
    paper required a deep dive into pivotal literature, which sharpened my skills in analyzing peer-reviewed 
    sources and evaluating different viewpoints within the field of instructional psychology. As I 
    investigated the interactions between learner, content, and instructor, I realized that theoretical 
    alignment is crucial for creating meaningful online environments.

    Meanwhile, my later coursework in LTEC 5610 challenged me to integrate those theories into practical, 
    real-world instructional design scenarios. Focusing on Cognitive Load Theory required not just a 
    grounding in academic literature, but also an awareness of practical constraints such as software 
    usability, learner demographics, and assessment methods. Through this 1500-word assignment, I refined 
    my ability to translate complex cognitive principles into digestible strategies for lesson planning. 
    This process was rewarding because it involved testing out design choices—like chunking information or 
    adding visual cues—and then validating them through data and reflective feedback. It underscored the 
    necessity of iterative experimentation, rather than simply relying on static theoretical models.

    Both papers taught me the value of rigorous research methods and strict adherence to APA guidelines. From 
    properly citing sources to maintaining a logical flow of arguments, these assignments reinforced best 
    practices for academic integrity and communication clarity. Revisions played a major role in shaping my 
    writing style, leading to concise and coherent discussions that resonate with scholarly audiences. My 
    professors and peers offered invaluable feedback, pushing me to address potential knowledge gaps and 
    refine my methodology.

    Overall, the transition from the early-stage social constructivism focus in LTEC 5300 to applying 
    Cognitive Load Theory in LTEC 5610 symbolizes my growth as a scholar who not only understands the why 
    of instructional design but also the how. This journey has strengthened my confidence in dissecting 
    complex ideas and expressing them in precise, persuasive language. Whether investigating a purely 
    theoretical question or devising an e-learning solution, I now approach scholarly work with a balance 
    of conceptual depth, methodological rigor, and practical awareness. These two papers, therefore, serve 
    as milestones in my academic development—reflecting an ever-increasing commitment to innovative, 
    research-based solutions in the field of Learning Technologies.
    """)

    st.markdown("""
    ### References
    (Ensure each paper has its own APA reference list. Below are placeholders; replace with actual references 
    cited in your papers.)

    - Vygotsky, L. (1978). *Mind in society: The development of higher psychological processes.* 
      Harvard University Press.

    - Mayer, R. E. (2014). *Cognitive theory of multimedia learning.* Cambridge University Press.
    """)

# ---------------------------
#          Footer
# ---------------------------
st.markdown('<div class="footer">© 2025 Sravanthi Akutota • Portfolio created using Streamlit</div>', unsafe_allow_html=True)
