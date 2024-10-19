import streamlit as st
from transformers import pipeline, MarianMTModel, MarianTokenizer

# Load the translation pipeline (using MarianMT for fine-tuned translation)
@st.cache_resource
def load_model():
    model_name = 'Helsinki-NLP/opus-mt-en-ur'  # Base model for English to Urdu
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return pipeline('translation', model=model, tokenizer=tokenizer)

def main():
    st.title("English to Urdu Translator")
    st.write("Enter an English sentence and get its translation in Urdu!")

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
                    st.success("Translation:")
                    st.write(urdu_translation)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter some English text to translate.")

if __name__ == "__main__":
    main()
