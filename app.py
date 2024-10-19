import streamlit as st
from transformers import pipeline

def main():
    st.title("English to Roman Urdu Converter")
    st.write("Enter an English prompt, and get the Roman Urdu equivalent!")

    # Load the Hugging Face model
    if "translator" not in st.session_state:
        st.session_state.translator = pipeline("translation", model="google/t5-v1_1-base")

    translator = st.session_state.translator

    # User input prompt
    input_text = st.text_input("Enter English text:")

    if st.button("Convert"):
        if input_text:
            # Generate Roman Urdu output
            output = translator(input_text)
            st.success(f"Roman Urdu: {output[0]['translation_text']}")
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
