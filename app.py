from flask import Flask, request, render_template

from translate import google_translate

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/translate', methods=['GET', 'POST'])
def get_translate():
    text = request.args.get('text') or request.json and request.json.get('text')
    src_lang = (request.args.get('src_lang') or request.json and request.json.get('src_lang')) or 'auto'
    dest_lang = (request.args.get('dest_lang') or request.json and request.json.get('dest_lang')) or 'en'

    if not text:
        return {'error': 'empty text'}, 400
    else:
        try:
            return {'translation': google_translate(text, src_lang, dest_lang)}
        except Exception as e:
            return {'error': str(e)}
