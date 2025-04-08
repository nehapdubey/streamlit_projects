import openai
import streamlit as st
from openai import OpenAI

# Set your OpenAI API Key
OPENAI_API_KEY=st.secrets["OPENAI_API_KEY"]

# Set your API key properly
client = OpenAI(api_key=OPENAI_API_KEY)

st.title("🤖 AI Chatbot with OpenAI")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to get AI response
def get_openai_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    except openai.RateLimitError:
        st.error("⛔ Rate limit hit! Please try again later.")
    except openai.AuthenticationError:
        st.error("🔒 Invalid API Key. Please check your key.")
    except openai.APIConnectionError:
        st.error("🌐 Network issue. Please check your internet connection.")
    except Exception as e:
        st.error(f"⚠️ Unexpected error: {str(e)}")

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_openai_response(prompt)

    if response:
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})