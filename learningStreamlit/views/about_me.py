import streamlit as st
from forms.contact import contact_form
st.title("About Me")
@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("assests/pp.png", width=180)
with col2:
    st.title("Neha Dubey", anchor=False)
    st.write(
        "Integration Specialist, streamlining enterprise workflows through API integration and automation. Passionate about building seamless, data-driven solutions with Python and MuleSoft. Experience in designing and developing AI-driven chatbots using NLP and automation frameworks."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()
SOCIAL_MEDIA = {
    "LinkedIn": "www.linkedin.com/in/profilepage-neha-dubey",
}


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 5 years of experience in API integration, automation, and software development.
    - Skilled in AI-driven automation, chatbot development, and system integrations
    - MBA in IT Operations & Management – NMIMS, 2024
    - PG Diploma in IoT – C-DAC Pune, 2019
    - B.Tech in Electronics & Telecommunication – BAMU, 2018

    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python, YAML, XML, DWL
    - Frameworks: Flask, Flask API, Guardrails-ai,  FastAPI, Anypoint Platform, MuleSoft
    - Tools & Platforms: Git, JIRA, Postman, REST Client, Azure, Eclipse IDE -anypoint studio
    - Operating Systems: Windows, Linux
    """
)

# --- SOCIAL LINKS ---
st.write('\n')
st.subheader("Find me on LinkedIn:", anchor=False)

cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    # Ensure absolute URLs and open links in a new tab
    safe_link = link if link.startswith("http") else f"https://{link}"
    cols[index].markdown(f'<a href="{safe_link}" target="_blank">{platform}</a>', unsafe_allow_html=True)
