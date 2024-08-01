import os
import deepl
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')
translator = deepl.Translator(DEEPL_API_KEY)

LANGUAGES = {
    "english": "EN",
    "spanish": "ES",
    "french": "FR",
    "german": "DE"
}

FORMALITY_LEVELS = {
    "formal": "prefer_more",
    "casual": "prefer_less"
}

def translate_text(text, source_lang, target_lang, formality="prefer_more"):
    try:
        result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang, formality=formality)
        return result.text
    except Exception as e:
        return f"Error: {str(e)}"

def prompt_user_input():
    input_text = input("Enter the text to be translated: ")
    source_language = input("Enter the source language (english/spanish/french/german): ").lower()
    target_language = input("Enter the target language (english/spanish/french/german): ").lower()
    formality = input("Enter the formality level (formal/casual): ").lower()

    if source_language not in LANGUAGES or target_language not in LANGUAGES:
        print("Invalid language input. Please enter a valid language (english/spanish/french/german).")
        return

    if formality not in FORMALITY_LEVELS:
        print("Invalid formality input. Please enter 'formal' or 'casual'.")
        return

    translated_text = translate_text(input_text, LANGUAGES[source_language], LANGUAGES[target_language], FORMALITY_LEVELS[formality])
    print(f"Translated text: {translated_text}")

def main():
    while True:
        prompt_user_input()
        exit_prompt = input("Do you want to close the application? If yes, type '0' else press '1': ")
        if exit_prompt == '0':
            break

if __name__ == "__main__":
    main()
