import streamlit as st
from transformers import pipeline

def main():
    st.title("English to Roman Urdu Converter")
    st.write("Enter an English prompt, and get the Roman Urdu equivalent!")

    # Load the Hugging Face model
    if "translator" not in st.session_state:
        try:
            st.session_state.translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ur")
        except Exception as e:
            st.error(f"Failed to load model: {e}")
            return

    translator = st.session_state.translator

    # User input prompt
    input_text = st.text_input("Enter English text:")

    if st.button("Convert"):
        if input_text:
            try:
                # Generate Roman Urdu output
                output = translator(input_text)
                urdu_text = output[0]['translation_text']

                # Simple conversion from Urdu script to Roman Urdu (manual mapping)
                urdu_to_roman = {
                    "ہیلو": "hello",
                    "کیا حال ہے": "kia haal hai",
                    # Add more mappings as needed
                }
                roman_urdu = urdu_to_roman.get(urdu_text, urdu_text)

                st.success(f"Roman Urdu: {roman_urdu}")
            except Exception as e:
                st.error(f"Error during conversion: {e}")
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
