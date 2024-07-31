import requests

# Prompt the user for input values
input_text = input("Enter the text to be translated: ")
source_language = input("Enter the source language: ")
target_language = input("Enter the target language: ")
formality = input("Enter the formality level (prefer_more/prefer_less): ")

lang = {"english": "EN", "spanish": "ES", "french": "FR", "german": "DE"}
formal = {"formal": "prefer_more", "casual": "prefer_less"}

# Prepare the data payload for the POST request
payload = {
    'input_text': input_text,
    'source_languages': lang[source_language],
    'target_languages': lang[target_language],
    'formality': formal[formality]
}

# Make the POST request to the translation endpoint
response = requests.post('http://127.0.0.1:5000/translate/terminal', data=payload)

# Print the response from the server
if response.status_code == 200:
    print("Translation successful!")
    print("Response HTML content:")
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
