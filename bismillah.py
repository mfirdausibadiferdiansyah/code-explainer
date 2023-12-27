import streamlit as st
import google.generativeai as genai
from api import api

# Configure the API key
genai.configure(api_key=api)

# Set default parameters
defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}

st.title('Code explainer')
st.write('You can ask me to code anything')
final_response = None
# Creating a side panel for inputs
with st.sidebar:
    st.write("## Code Generator Settings")
    # Create a dropdown for selecting the programming language
   
    # Create a text input for the prompt
    prompt = st.text_input("What do you want to code?")
    # When the 'Generate' button is pressed, generate the text
    if st.button('Generate'):
        formatted_prompt = f"explain this code with details {prompt}"
        response = genai.generate_text(
            **defaults,
            prompt=formatted_prompt
        )
        final_response = response
if final_response != None:
    st.write(final_response.result)