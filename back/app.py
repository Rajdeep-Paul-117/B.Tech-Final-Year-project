from flask import Flask, render_template, url_for, request, redirect
from flask_cors import CORS, cross_origin
import stanza
import json
import requests
proxies={}
#proxies = {'http': 'http://172.16.199.41:8080', 'https': 'http://172.16.199.41:8080'}
stanza.download('en')

app = Flask(__name__)
CORS(app)

@app.route('/comp-stanza', methods=['POST'])
def index():
    if request.method == 'POST':
        task_content1 = request.get_json()[0].get('text')
        task_content2 = request.get_json()[1].get('text')
        
        nlp = stanza.Pipeline(lang='en',proxies=proxies,processors='tokenize,ner')
        doc1 = nlp(task_content1)
        doc2 = nlp(task_content2)

        result1 = dict()
        result2 = dict()

        jsonified_text=[]
        for x in doc1.entities:
            result1.setdefault(x.type,[]).append(x.text);
        
        for x in doc2.entities:
            result2.setdefault(x.type,[]).append(x.text);
            
        return [result1,result2]

        
@app.route('/comp-corenlp', methods=['POST'])
def corenlp():
    if request.method == 'POST':
        task_content1 = request.get_json()[0].get('text')
        task_content2 = request.get_json()[1].get('text')
        
        url='https://corenlp.run/'
        prop={"properties":
                '{"annotators": "tokenize,ssplit,ner", "date": "2022-09-10T17:51:46"}'
                }
        doc1 = requests.post(url,data={task_content1:''},params=prop)
        doc1= doc1.json()["sentences"][0]["entitymentions"]
    
        doc2 = requests.post(url,data={task_content2:''},params=prop)
        doc2= doc2.json()["sentences"][0]["entitymentions"]
        
        result1 = dict()
        result2 = dict()

        jsonified_text=[]
        for x in doc1:
            if x['ner']=='TIME':
                result1.setdefault(x['ner'],[]).append(x['normalizedNER'])
            else:
                result1.setdefault(x['ner'],[]).append(x['text'])
        
        for x in doc2:
            if x['ner']=='TIME':
                result2.setdefault(x['ner'],[]).append(x['normalizedNER'])
            else:
                result2.setdefault(x['ner'],[]).append(x['text'])
            
        return [result1,result2]
if __name__ == '__main__':
    app.run(debug=True)
