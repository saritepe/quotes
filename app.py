import streamlit as st
import streamlit.components.v1 as components

# Inject meta tags
meta_tags = """
<meta name="description" content="Show random quotes">
<title>Quotes App</title>
<meta name="keywords" content="quotes, streamlit, search">
<meta name="author" content="Ugur Saritepe">
<meta name="google-site-verification" content="Qt7ni_QIPZUafqHNOthSSglMNqvZqoFJtbtb_2bqFHU" />
"""
components.html(meta_tags, height=0)
import requests
import random

st.title("Quotes App")
st.write("Welcome to the Quotes App!")

# Fetch quotes from API
response = requests.get("https://api.quotable.io/quotes?limit=100", verify=False)
quotes = response.json()["results"]

def get_random_quote():
    return random.choice(quotes)

# Display the quote
if 'quote' not in st.session_state:
    st.session_state.quote = get_random_quote()

st.subheader("Random Quote")

# UI Enhancements
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f0f0;
        padding: 20px;
        border-radius: 10px;
    }
    .quote {
        font-size: 24px;
        font-style: italic;
        color: #333;
    }
    .author {
        font-size: 20px;
        font-weight: bold;
        color: #555;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="main">
        <p class="quote">"{st.session_state.quote['content']}"</p>
        <p class="author">- {st.session_state.quote['author']}</p>
    </div>
    """,
    unsafe_allow_html=True
)

if st.button("Show Another Quote"):
    st.session_state.quote = get_random_quote()
