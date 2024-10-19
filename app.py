import streamlit as st
from googletrans import Translator
import re

def preprocess_input(text):
    replacements = {
        "u": "you",
        "r": "are",
        "pls": "please",
        "thx": "thanks",
    }
    return ' '.join(replacements.get(word.lower(), word) for word in text.split())

def translate_text_google(text, src_lang='en', tgt_lang='ur'):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=tgt_lang)
    return translated.text

def romanize_urdu(text):
    transliteration_map = {
        'ضرورت': 'zaroorat',
        'ایجاد': 'ijaad',
        'ماں': 'maa',
        'ہے': 'hai',
        'کی': 'ki',
        'پیدائش': 'paidaish',
        'تم': 'tum',
        'کیسے': 'kaise',
        'ہو': 'ho',
        'کیا': 'kya',
        'حال': 'haal',
    }
    char_map = {
        'ک': 'k', 'ہ': 'h', 'ر': 'r', 'ا': 'a', 'ل': 'l', 'م': 'm', 'ت': 't',
        'ی': 'i', 'ن': 'n', 'د': 'd', 'س': 's', 'و': 'w', 'چ': 'ch', 'پ': 'p',
        'ش': 'sh', 'ب': 'b', 'گ': 'g', 'ف': 'f', 'ج': 'j', 'ز': 'z', 'خ': 'kh',
        'غ': 'gh', 'ع': 'a', 'ص': 's', 'ض': 'z', 'ط': 't', 'ظ': 'z', 'ق': 'q',
        'ح': 'h', 'ث': 's', 'ذ': 'z', 'ژ': 'zh', 'ٹ': 't', 'ڈ': 'd', 'ڑ': 'r',
        'ے': 'e', 'ں': 'n'
    }
    
    def transliterate_word(word):
        return transliteration_map.get(word, ''.join(char_map.get(char, char) for char in word))
    
    return ' '.join(transliterate_word(word) for word in text.split())

def main():
    st.title("English to Roman Urdu Translator")
    st.write("Enter an English sentence and get its translation in Roman Urdu!")

    english_text = st.text_area("Enter English text:", height=150)

    if st.button("Translate"):
        if english_text:
            with st.spinner('Translating...'):
                try:
                    processed_text = preprocess_input(english_text)
                    urdu_translation = translate_text_google(processed_text)
                    roman_urdu_translation = romanize_urdu(urdu_translation)
                    st.success("Translation:")
                    st.write(roman_urdu_translation)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter some English text to translate.")

if __name__ == "__main__":
    main()
