from flask import Flask, render_template, url_for, request, redirect
import stanza
import json
proxies = {'http': 'http://172.16.199.41:8080', 'https': 'http://172.16.199.41:8080'}
stanza.download('en',proxies=proxies)

app = Flask(__name__)

@app.route('/comp', methods=['POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['text']
        nlp = stanza.Pipeline(lang='en',proxies=proxies,processors='tokenize,ner')
        doc = nlp(task_content)
        jsonified_text=[]
        for x in doc.entities:
            print(x)
            # jsonified_text.append(json.dumps({'text':x.text, 'type':x.type}))

        # print(jsonified_text)
        return jsonified_text
if __name__ == '__main__':
    app.run(debug=True)
