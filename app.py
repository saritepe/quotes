import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("API_KEY")

# Title of the app
st.title("Quotes App")

# Sample quotes
quotes = [
    "The best way to predict the future is to create it.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "The only way to do great work is to love what you do.",
    "Success is not the key to happiness. Happiness is the key to success."
]

# Display quotes
for quote in quotes:
    st.write(f"\"{quote}\"")
