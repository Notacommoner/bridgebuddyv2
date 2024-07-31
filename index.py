import os
import deepl
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')
translator = deepl.Translator(DEEPL_API_KEY)

def translatetext(text, source_lang, target_lang,formality="prefer_more"):
    result = translator.translate_text(text,source_lang=source_lang,target_lang=target_lang, formality=formality)
    return result.text

# Prompt the user for input values
input_text = input("Enter the text to be translated: ")
source_language = input("Enter the source language: ")
target_language = input("Enter the target language: ")
formality = input("Enter the formality level (formal/casual): ")

lang = {"english": "EN", "spanish": "ES", "french": "FR", "german": "DE"}
formal = {"formal": "prefer_more", "casual": "prefer_less"}

print(translatetext(input_text, lang[source_language], lang[target_language], formal[formality]))
