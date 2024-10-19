import streamlit as st
from transformers import pipeline, MarianMTModel, MarianTokenizer

# Load the translation pipeline (using MarianMT for fine-tuned translation)
@st.cache_resource
def load_model():
    model_name = 'Helsinki-NLP/opus-mt-en-ur'  # Base model for English to Urdu
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return pipeline('translation', model=model, tokenizer=tokenizer)

def romanize_urdu(text):
    # A basic dictionary for Urdu to Roman Urdu transliteration
    transliteration_map = {
        'ک': 'k', 'ہ': 'h', 'ر': 'r', 'ا': 'a', 'ل': 'l', 'م': 'm', 'ت': 't',
        'ی': 'i', 'ن': 'n', 'د': 'd', 'س': 's', 'و': 'w', 'چ': 'ch', 'پ': 'p',
        'ش': 'sh', 'ب': 'b', 'گ': 'g', 'ف': 'f', 'ج': 'j', 'ز': 'z', 'خ': 'kh',
        'غ': 'gh', 'ع': 'a', 'ص': 's', 'ض': 'z', 'ط': 't', 'ظ': 'z'
        # Add more mappings for more accuracy
    }
    
    # Replace each character with its Roman Urdu equivalent
    romanized_text = ''.join([transliteration_map.get(char, char) for char in text])
    return romanized_text

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
