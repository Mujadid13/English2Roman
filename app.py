import streamlit as st
from transformers import pipeline, MarianMTModel, MarianTokenizer
from googletrans import Translator  # Library to help with Roman transliteration

# Load the translation pipeline (using MarianMT for fine-tuned translation)
@st.cache_resource
def load_model():
    model_name = 'Helsinki-NLP/opus-mt-en-ur'  # Base model for English to Urdu
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return pipeline('translation', model=model, tokenizer=tokenizer)

def romanize_urdu(text):
    # Use Google Translator to transliterate Urdu script to Roman Urdu
    translator = Translator()
    try:
        result = translator.translate(text, src='ur', dest='en')
        return result.text if result else text
    except Exception as e:
        return f"Transliteration failed: {str(e)}"

def main():
    st.title("English to Roman Urdu Translator")
    st.write("Enter an English sentence and get its translation in Roman Urdu!")

    # Load the model
    translator = load_model()

    # Input prompt
    english_text = st.text_area("Enter English text:", height=150)

    # Translate and display output
    if st.button("Translate"):
        if english_text:
            with st.spinner('Translating...'):
                try:
                    urdu_translation = translator(english_text)[0]['translation_text']
                    roman_urdu_translation = romanize_urdu(urdu_translation)
                    st.success("Translation:")
                    st.write(roman_urdu_translation)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter some English text to translate.")

if __name__ == "__main__":
    main()
