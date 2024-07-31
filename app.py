from flask import Flask,request,render_template, send_file
import os
from datetime import date
import deepl
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')
translator = deepl.Translator(DEEPL_API_KEY)

app = Flask(__name__)

def list_all_languages(type):
    if type == "source":
        return translator.get_source_languages()
    else:
        return translator.get_target_languages()
    
def translatetext(text, source_lang, target_lang,formality="prefer_more"):
    result = translator.translate_text(text,source_lang=source_lang,target_lang=target_lang, formality=formality)
    return result.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate',methods=['POST', 'GET']) 
def translate():
    source_languages = list_all_languages("source")
    target_languages = list_all_languages("target")

    if request.method == 'GET':
        formality = "prefer_more"
        return render_template(
            'translate.html', 
            source_languages=source_languages,
            target_languages=target_languages,
            formality=formality
        )
    else:
        input_text = request.form['input_text']
        sourcelang = request.form['source_languages']
        targetlang = request.form['target_languages']
        formality = request.form['formality']
        translated_text = translatetext(input_text,sourcelang,targetlang,formality)
        return render_template(
            'translate.html',
            source_text=input_text,
            translated_text=translated_text,
            source_languages=source_languages,
            target_languages=target_languages,
            selected_source_language=sourcelang,
            selected_target_language=targetlang,
            formality=formality
        )

@app.route('/translate/terminal',methods=['POST', 'GET'])
def translateTerminal():
    source_languages = list_all_languages("source")
    target_languages = list_all_languages("target")

    if request.method == 'GET':
        print(source_languages, target_languages)
        formality = "prefer_more"
        return render_template(
            'translate.html', 
            source_languages=source_languages,
            target_languages=target_languages,
            formality=formality
        )
    else:
        input_text = request.form['input_text']
        sourcelang = request.form['source_languages']
        targetlang = request.form['target_languages']
        formality = request.form['formality']
        translated_text = translatetext(input_text,sourcelang,targetlang,formality)
       
        return translated_text
    
@app.route('/download')
def download_file():
    # Ensure the file path is correct and accessible
    file_path = os.getcwd() + "/dist/index.exe"
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)