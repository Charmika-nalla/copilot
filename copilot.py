import streamlit as st
import google.generativeai as genai
import os

# Set up the API key
api_key = os.getenv("API_KEY")
if api_key is None:
    st.error("API_KEY environment variable is not set.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit app
st.title("Copilot")
st.write("Enter prompts and get responses.")

# Initialize session state for prompts and results
if 'input1' not in st.session_state:
    st.session_state.input1 = ""
if 'result1' not in st.session_state:
    st.session_state.result1 = ""
if 'input2' not in st.session_state:
    st.session_state.input2 = ""
if 'result2' not in st.session_state:
    st.session_state.result2 = ""
if 'input3' not in st.session_state:
    st.session_state.input3 = ""
if 'result3' not in st.session_state:
    st.session_state.result3 = ""
if 'response_generated_1' not in st.session_state:
    st.session_state.response_generated_1 = False
if 'response_generated_2' not in st.session_state:
    st.session_state.response_generated_2 = False

# Function to handle Prompt 1 response generation
def handle_prompt1():
    if st.session_state.input1:
        st.session_state.result1 = generate_response(st.session_state.input1)
        st.session_state.response_generated_1 = True
    else:
        st.session_state.result1 = "Please enter a prompt."

# Function to handle Prompt 2 response generation
def handle_prompt2():
    if st.session_state.input2:
        st.session_state.result2 = generate_response(st.session_state.input2)
        st.session_state.response_generated_2 = True
    else:
        st.session_state.result2 = "Please enter a prompt."

# Function to handle Prompt 3 response generation
def handle_prompt3():
    if st.session_state.input3:
        st.session_state.result3 = generate_response(st.session_state.input3)
    else:
        st.session_state.result3 = "Please enter a prompt."

# Input area and button for Prompt 1
st.subheader("Prompt 1")
st.text_area("Your input for Prompt", key='input1')

if st.button("Generate Response for Prompt"):
    handle_prompt1()

# Display result for Prompt 1
st.subheader("Response for Prompt")
st.write(st.session_state.result1)

# Input area and button for Prompt 2, displayed only after Prompt 1's response is generated
if st.session_state.response_generated_1:
    st.subheader("Prompt")
    st.text_area("Your input for Prompt", key='input2')

    if st.button("Generate Response for the Prompt"):
        handle_prompt2()

    # Display result for Prompt 2
    st.subheader("Response for Prompt")
    st.write(st.session_state.result2)

    # Input area and button for Prompt 3, displayed only after Prompt 2's response is generated
    if st.session_state.response_generated_2:
        st.subheader("Prompt")
        st.text_area("Your input for Prompt", key='input3')

        if st.button("Generate Response"):
            handle_prompt3()

        # Display result for Prompt 3
        st.subheader("Response for Prompt")
        st.write(st.session_state.result3)
