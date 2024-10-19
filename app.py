import streamlit as st
from transformers import pipeline, MBartForConditionalGeneration, MBart50TokenizerFast

# Load the translation pipeline (using mBART for multilingual translation)
@st.cache_resource
def load_model():
    model_name = 'facebook/mbart-large-50-many-to-many-mmt'  # Better suited for multilingual translations
    tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    return model, tokenizer

def preprocess_input(text):
    # Simple preprocessing to replace informal abbreviations
    replacements = {
        "u": "you",
        "r": "are",
        # Add more if necessary
    }
    words = text.split()
    processed_words = [replacements.get(word, word) for word in words]
    return " ".join(processed_words)

def main():
    st.title("English to Urdu Translator")
    st.write("Enter an English sentence and get its translation in Urdu!")

    # Load the model and tokenizer
    model, tokenizer = load_model()

    # Input prompt
    english_text = st.text_area("Enter English text:", height=150)

    # Translate and display output
    if st.button("Translate"):
        if english_text:
            with st.spinner('Translating...'):
                try:
                    # Preprocess the input text
                    processed_text = preprocess_input(english_text)

                    # Tokenize the input text
                    tokenizer.src_lang = "en_XX"  # Source language is English
                    inputs = tokenizer(processed_text, return_tensors="pt")

                    # Generate translation
                    generated_tokens = model.generate(
                        **inputs,
                        forced_bos_token_id=tokenizer.lang_code_to_id["ur_PK"]  # Target language is Urdu
                    )

                    # Decode the generated tokens
                    urdu_translation = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
                    st.success("Translation:")
                    st.write(urdu_translation)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter some English text to translate.")

if __name__ == "__main__":
    main()
