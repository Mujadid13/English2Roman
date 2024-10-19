import streamlit as st
from transformers import pipeline

# Load the English to Roman Urdu translation model
translator = pipeline("translation", model="your-model-name-here")

def translate_to_roman_urdu(text):
    result = translator(text, max_length=128)[0]['translation_text']
    return result

# Streamlit app
st.title("English to Roman Urdu Translator")

# Input text box
input_text = st.text_area("Enter English text:", "Hello, how are you?")

if st.button("Translate"):
    if input_text:
        # Perform translation
        roman_urdu = translate_to_roman_urdu(input_text)
        
        # Display result
        st.subheader("Roman Urdu Translation:")
        st.write(roman_urdu)
    else:
        st.warning("Please enter some text to translate.")

# Instructions for running the app
st.sidebar.header("How to run this app")
st.sidebar.markdown("""
1. Install required libraries: `pip install streamlit transformers torch`
2. Replace `"your-model-name-here"` with the actual Hugging Face model name
3. Save this script as `app.py`
4. Run the app: `streamlit run app.py`
""")
