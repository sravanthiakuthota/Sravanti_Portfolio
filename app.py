import streamlit as st
import base64
import os

# ------------------------------------------------
# Configure the main page
# ------------------------------------------------
st.set_page_config(
    page_title="Sravanthi Akutota | Portfolio",
    layout="wide",
)

# ------------------------------------------------
# Helper Functions (Your "Pages")
# ------------------------------------------------

def show_identity():
    """Identity (Home) Section"""
    st.title("Sravanthi Akutota")
    st.write("M.S. in Learning Technologies | University of North Texas")

    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("profile.jpeg"):
            st.image("profile.jpeg", width=200, caption="Sravanthi Akutota")
        else:
            st.warning("'profile.jpeg' not found. Please add a professional headshot.")

    with col2:
        st.subheader("About Me")
        st.write("""
            I am passionate about integrating technology and education 
            to create impactful learning experiences. I am currently 
            pursuing my master's degree in Learning Technologies, with 
            a background in Electrical and Electronics Engineering.

            I also have experience in content management and data analysis 
            from my time at Google AdWords. Please use the menu to learn more 
            about my resume, projects, and how to get in touch.
        """)

def show_resume():
    """Resume Section (PDF Viewer and Download)"""
    st.title("Resume")
    st.write("Below is my resume, with an option to download.")

    resume_path = "resume.pdf"
    if os.path.exists(resume_path):
        with open(resume_path, "rb") as f:
            resume_data = f.read()

            # Download button
            st.download_button(
                label="Download Resume",
                data=resume_data,
                file_name="Sravanthi_Resume.pdf",
                mime="application/pdf"
            )

            # Embed PDF in an iframe
            b64_pdf = base64.b64encode(resume_data).decode("utf-8")
            pdf_display = f'<iframe src="data:application/pdf;base64,{b64_pdf}" width="100%" height="700px"></iframe>'
            st.markdown("---")
            st.subheader("Resume Preview")
            st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.error("Error: 'resume.pdf' not found in the app folder.")

def show_projects():
    """Projects Section"""
    st.title("Projects")

    st.subheader("Reviewer Dashboard")
    st.write("""
        Developed a dashboard to summarize the quality and 
        turnaround time of advertisement reviews at Google AdWords, 
        improving internal workflows.
    """)

    st.subheader("Learning Insights")
    st.write("""
        Created an interactive report using Power BI to track 
        student performance and recommend interventions based on analytics.
    """)

    st.subheader("AI in Education")
    st.write("""
        Investigated how AI tools can enhance learner engagement 
        and deliver more personalized digital learning experiences.
    """)

def show_contact():
    """Contact Section"""
    st.title("Contact")
    st.write("Feel free to reach out, or use the form below for inquiries.")

    st.markdown("**Email:** akutotasravanthi@gmail.com")
    st.markdown("**Phone:** 940-331-4160")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success(f"Thank you, {name}. Your message has been received.")

# ------------------------------------------------
# Main Logic: Query Param Navigation + Menu
# ------------------------------------------------

# Define pages
PAGES = {
    "Identity": show_identity,
    "Resume": show_resume,
    "Projects": show_projects,
    "Contact": show_contact
}

# Get current query params
query_params = st.query_params
default_page = "Identity"

# If 'page' param not set or invalid, go to default
if "page" in query_params and query_params["page"] in PAGES:
    current_page = query_params["page"]
else:
    current_page = default_page

st.sidebar.title("Navigation")

def set_page(page_name: str):
    """Update the 'page' query param, then rerun."""
    st.set_query_params(page=page_name)
    st.experimental_rerun()

page_choice = st.sidebar.radio(
    "Go to page:",
    list(PAGES.keys()),
    index=list(PAGES.keys()).index(current_page)
)

if page_choice != current_page:
    set_page(page_choice)

PAGES[current_page]()

# ------------------------------------------------
# Footer
# ------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.write("© 2025 Sravanthi Akutota • Portfolio created using Streamlit")
