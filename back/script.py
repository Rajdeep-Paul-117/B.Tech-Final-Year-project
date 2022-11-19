import pandas as pd
import bert_similarity,uuid,requests

dataset=pd.read_excel('./test.xlsx')

constructed_url = 'https://api.cognitive.microsofttranslator.com/translate'
params = {
      'api-version': '3.0',
      'to': 'en'
    }
headers = {
      'Ocp-Apim-Subscription-Key': "610f3b1042354f3ea5b3a2a0c1ccaba9",
      'Ocp-Apim-Subscription-Region': "centralindia",
      'Content-type': 'application/json',
      'X-ClientTraceId': str(uuid.uuid4())
    }

result=[]
for index,data in dataset.iterrows():
    body = [{'text': data[3]}]    
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()[0].get("translations")[0].get("text")
    result.append(bert_similarity.similarity(data[2], response))
dataset['roberta']=result
dataset.to_excel('./test.xlsx')