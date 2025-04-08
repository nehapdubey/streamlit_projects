import streamlit as st

# Import rest after set_page_config
import spacy
from textblob import TextBlob

# Cache model loading to avoid reload and avoid triggering Streamlit too early
@st.cache_resource
def load_spacy_model():
    return spacy.load("en_core_web_sm")

nlp = load_spacy_model()

st.title("🧠 Text Sentiment Analyzer(spaCy + TextBlob)")

# Text Input
text_input = st.text_area("Enter text to analyze:", height=100)

#Sentiment + Token Analyzer
def analyze_text(text):
    doc = nlp(text)
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Emoji sentiment logic
    sentiment = "Neutral 😐"
    if polarity > 0.1:
        sentiment = "Positive 😊"
    elif polarity < -0.1:
        sentiment = "Negative 😠"

    return doc, polarity, subjectivity, sentiment

#Analyze on Button Click
if st.button("Analyze"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        doc, polarity, subjectivity, sentiment = analyze_text(text_input)

        st.subheader("Sentiment Analysis Result:")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Polarity:** `{polarity}`")
        st.write(f"**Subjectivity:** `{subjectivity}`")
        st.subheader("spaCy Token Analysis:")
        st.write([(token.text, token.pos_, token.dep_) for token in doc])