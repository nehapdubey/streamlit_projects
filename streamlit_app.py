import streamlit as st

# page setup

about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
Project_1_Page = st.Page(
    page="views\sales_dashboard.py",
    title=" Expense dashboard",
    icon=":material/bar_chart:",
)


Project_2_Page = st.Page(
    page="views\chatbot.py",
    title="chat bot",
    icon=":material/smart_toy:",
)

Project_3_Page = st.Page(
    page="views\sentimental.py",
    title="Sentimental Analyzer",
    icon=":material/psychology:",

)


# Navigation set up
pg = st.navigation(
    {
    "Info" : [about_page],
    "Projects" : [Project_1_Page,Project_2_Page, Project_3_Page],
    }
)

#setlog
st.logo("assests/dino.png")

#set sidertext
st.sidebar.text("Author: Neha Dubey")
#run Navigation
pg.run()